import collections
import tkinter
from tkinter import (Canvas,
                     Tk,
                     Label,
                     messagebox)

import Drop7
import Disk
import Board
import Position

DISK_SPACING = 20
DISK_SIZE = 50
GUI_UPDATE_DELAY_MS = 500

DrawContext = collections.namedtuple("DrawContext", [
    "canvas",
    "ovals",
    "next_oval_canvas",
    "next_oval",
    "next_text",
    "texts",
    "score",
    "turns",
    "columns"
])

def all_positions(board):
    """
    :param board:
    :return: generator for all positions on the board
    """
    position = (1, 1)
    while position is not None:
        yield position
        position = Position.next(Board.dimension(board), position)


def draw_disk(c, position, disk):
    (row, col) = position
    # For some reason the example code flips this?
    p = (col - 1, row - 1)
    draw_disk_on_canvas(c.canvas, c.ovals[p], c.texts[p], disk)


def draw_disk_on_canvas(canvas, oval, text, disk):
    state = Disk.get_state(disk)
    value = Disk.get_value(disk)

    state_colors = {
        Disk.VISIBLE: "green",
        Disk.CRACKED: "gray",
        Disk.WRAPPED: "black",
    }

    ##############################################################
    # Added to give the circles with different values a different color
    value_colors = {
        1: "green",
        2: "yellow",
        3: "orange",
        4: "red",
        5: "purple",
        6: "cyan",
        7: "blue",
    }

    if state == Disk.VISIBLE:
        canvas.itemconfig(oval, fill=value_colors[value])
    else:  #########################################################
        canvas.itemconfig(oval, fill=state_colors[state])


    if state == Disk.VISIBLE:
        canvas.itemconfig(text, text=value, fill="black")

    if state == Disk.CRACKED:
        canvas.itemconfig(oval, dash=(5, 3))


def draw_next_disk(c, disk):
    draw_disk_on_canvas(c.next_oval_canvas, c.next_oval, c.next_text, disk)


def draw_disks(c, board):
    for p in all_positions(board):
        disk = Board.get_disk_at(board, p)
        if disk is not None:
            draw_disk(c, p, disk)


def draw_score(c, score):
    c.score.set(score)


def draw_turns(c, turns, turns_per_level):
    c.turns.set("%s / %s to the next level" % (turns, turns_per_level))


def draw_game_state(draw_context, game_state):
    reset_ovals_and_texts(draw_context)
    draw_disks(draw_context, game_state["board"])
    draw_score(draw_context, game_state["score"])
    draw_turns(draw_context, game_state["current_nb_turns"],
               game_state["turns_per_level"])
    draw_next_disk(draw_context, game_state["next_disk"])
    update_gui()


def reset_ovals_and_texts(c):
    c.next_oval_canvas.itemconfig(c.next_oval, fill="white", dash=())
    c.next_oval_canvas.itemconfig(c.next_text, text="", fill="white")
    for oval in c.ovals.values():
        c.canvas.itemconfig(oval, fill="white", dash=())
    for text in c.texts.values():
        c.canvas.itemconfig(text, text="", fill="white")


def add_disk(draw_context, game_state, column):
    gs = game_state
    board = gs["board"]

    if not Board.can_accept_disk(board):
        messagebox.showerror("Finished", "Board can no longer accept this disk!")
    elif not Board.is_playable_board(board):
        messagebox.showerror("Finished", "Board is not playable!")
    elif Board.is_full_column(board,column):
        messagebox.showerror("Finished", "Column is full.")
    else:
        disk_to_drop = gs["next_disk"]
        gs["score"] += Drop7.drop_disk_at(board,disk_to_drop,column)
        gs["current_nb_turns"] += 1

        if gs["current_nb_turns"] == gs["turns_per_level"]:
            gs["score"] += 1000 // gs["turns_per_level"]
            Board.inject_bottom_row_wrapped_disks(board)
            Drop7.drop_disk_at(board)
            gs["current_nb_turns"] = 0
            gs["turns_per_level"] = max(gs["turns_per_level"] - 1, 10)

        gs["next_disk"] = Disk.get_random_disk(Board.dimension(board),
                                               {Disk.VISIBLE, Disk.WRAPPED})
        draw_game_state(draw_context, game_state)


def draw_board(root):
    """
      Create the graphical user interface.
    """
    # board = Board.init_board(7, ((Disk.init_disk(Disk.VISIBLE, 4),),))
    board = Board.init_board(7, ())
    game_state = {
        "score": 0,
        "turns_per_level": 20,
        "current_nb_turns": 0,
        "board": board,
        "next_disk": Disk.get_random_disk(Board.dimension(board),
                                          {Disk.VISIBLE, Disk.WRAPPED})
    }
    dimension = Board.dimension(board)

    # provide the title that will be shown in the header
    root.title("Drop 7")

    score_variable = create_variable_frame(root, "Score:")
    turn_variable = create_variable_frame(root, "Turns to next level:")

    next_oval_canvas, next_oval, next_text = create_next_oval(root)

    canvas = Canvas(root, bg="white",
                    height=dimension * (
                            DISK_SIZE + DISK_SPACING) + DISK_SPACING,
                    width=dimension * (DISK_SIZE + DISK_SPACING) + DISK_SPACING)

    columns = create_columns(canvas, dimension)
    ovals, texts = create_ovals(canvas, dimension, dimension)
    draw_context = DrawContext(canvas, ovals, next_oval_canvas, next_oval,
                               next_text, texts, score_variable, turn_variable,
                               columns)

    bind_interface(draw_context,
                   lambda column: add_disk(draw_context, game_state, column))

    canvas.pack()

    draw_game_state(draw_context, game_state)


def create_next_oval(root):
    canvas = Canvas(root, bg="orange",
                    height=DISK_SIZE + 2 * DISK_SPACING,
                    width=DISK_SIZE + 2 * DISK_SPACING)
    oval = canvas.create_oval(
        0,
        2 * DISK_SPACING + DISK_SIZE,
        0,
        2 * DISK_SPACING + DISK_SIZE,
        width=1,
        fill="yellow")

    text = canvas.create_text(
        DISK_SPACING + DISK_SIZE / 2,
        DISK_SPACING + DISK_SIZE / 2,
        justify=tkinter.CENTER,
        anchor=tkinter.CENTER,
    )
    canvas.pack()
    return canvas, oval, text


def create_variable_frame(root, label):
    frame = tkinter.Frame(root)
    frame.pack()
    text_label = Label(frame, text=label, bg="white", fg="black",
                       font=("", 28))
    text_label.grid(row=0, column=0)
    variable = tkinter.StringVar()
    label = Label(frame, textvariable=variable, bg="white",
                  fg="black",
                  font=("", 28))
    label.grid(row=0, column=1)
    return variable


def create_columns(canvas, dimension):
    column_height = DISK_SPACING + dimension * (
            DISK_SPACING + DISK_SIZE) + DISK_SIZE
    side_column_width = 1.5 * DISK_SPACING + DISK_SIZE
    left = canvas.create_rectangle(0, 0, side_column_width, column_height)

    def col_x(c):
        return (side_column_width) + c * (DISK_SPACING + DISK_SIZE)

    middle = [
        canvas.create_rectangle(
            col_x(col),
            0,
            col_x(col + 1),
            column_height,
        ) for col in range(0, dimension - 2)]

    right = canvas.create_rectangle(col_x(dimension - 2), 0,
                                    col_x(dimension - 2) + side_column_width,
                                    column_height)

    columns = [left] + middle + [right]

    return columns


def bind_interface(draw_context, on_column_click):
    canvas = draw_context.canvas


    for pos in draw_context.ovals.keys():
        row, col = pos
        o = draw_context.ovals[(row, col)]
        c = draw_context.columns[col]
        t = draw_context.texts[(row, col)]

        bind_for_column(canvas, t, c, col, on_column_click)
        bind_for_column(canvas, o, c, col, on_column_click)
        bind_for_column(canvas, c, c, col, on_column_click)


def bind_for_column(canvas, element, column, columnNr, on_column_click):
    o = element
    c = column
    canvas.tag_bind(o, "<Button-1>",
                    lambda event, column=columnNr: on_column_click(column + 1))
    canvas.tag_bind(o, "<Leave>",
                    lambda event, c=c: canvas.itemconfig(c, fill="white"))
    canvas.tag_bind(o, "<Enter>",
                    lambda event, c=c: canvas.itemconfig(c, fill="red"))

def create_ovals(canvas, board_width, board_height):
    """
      Return a matrix containing ovals that are correctly initialized
      at their required location and coloured.
    """
    ovals = {}
    texts = {}

    for row in range(board_height - 1, -1, -1):
        for col in range(board_width):
            flipped_row = board_height - row - 1

            oval = canvas.create_oval(
                DISK_SPACING + col * (DISK_SPACING + DISK_SIZE),
                DISK_SPACING + row * (DISK_SPACING + DISK_SIZE),
                DISK_SPACING + col * (DISK_SPACING + DISK_SIZE) + DISK_SIZE,
                DISK_SPACING + row * (DISK_SPACING + DISK_SIZE) + DISK_SIZE,
                width=1)
            ovals[(flipped_row, col)] = oval

            text = canvas.create_text(
                DISK_SPACING + DISK_SIZE / 2 + col * (DISK_SPACING + DISK_SIZE),
                DISK_SPACING + DISK_SIZE / 2 + row * (DISK_SPACING + DISK_SIZE),
                text="0",
                justify=tkinter.CENTER,
                anchor=tkinter.CENTER,
            )
            texts[(flipped_row, col)] = text

    return ovals, texts

def update_gui():
    root.update_idletasks()
    root.after(GUI_UPDATE_DELAY_MS)


root = Tk()
draw_board(root)
root.mainloop()
