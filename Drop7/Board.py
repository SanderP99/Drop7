# Boards are square areas of N rows and N columns.
#     - Rows and columns in boards are numbered starting from 1.
try:
    import Disk
    import Position
except:
    import Drop7.Disk as Disk
    import Drop7.Position as Position

from random import *


def is_proper_board(board):
    """
        Check whether the given board is a proper board. The function
        returns true iff all the conditions below are satisfied:
        - The given board may not be None, and its dimension
          must be a natural number.
        - Each cell of the given board either stores nothing (None),
          or it stores a proper disk for the given board.
        ASSUMPTIONS
        - None
    """
    if board is None:
        return False

    if dimension(board) <= 0:
        return False

    for column in range(1, dimension(board) + 1):
        for row in range(1, dimension(board) + 2):
            disk_to_check = get_disk_at(board, (column, row))
            if not (disk_to_check is None
                    or Disk.is_proper_disk(dimension(board), disk_to_check)):
                return False

    return True


def is_playable_board(board):
    """
        Check whether the given board is a playable board. The function
        returns true iff all the conditions below are satisfied:
        - The given board is a proper board.
        - If a cell stores a disk, all cells below also store
          a disk (i.e. there are no gaps in columns).
        - The same disk is not stored at several positions on the given board.
        ASSUMPTIONS
        - None
    """
    if not is_proper_board(board):  # No proper board
        return False

    for column in range(1, dimension(board) + 1):  # Check for disks that don't have all cells below disks
        none_count = 0
        for row in range(1, dimension(board) + 2):
            disk_to_check = get_disk_at(board, (column, row))

            if disk_to_check is None:
                none_count += 1

            elif none_count != 0:
                return False

    if has_same_disk_several_positions(board):
        return False

    return True


def has_same_disk_several_positions(board):
    """
        Check if the same disk appears multiple times on the same board
        Returns True is there is one or are multiple appearances, False if not
    """
    used_disks = list(board.values())

    for pos in range(len(used_disks) - 1, -1, -1):
        if used_disks[pos] is None:
            del used_disks[pos]

    for pos in range(len(used_disks)):
        for subpos in range(pos + 1, len(used_disks)):
            if used_disks[pos] is used_disks[subpos]:
                return True

    return False


def init_board(dimension, given_disks=()):
    """
        Return a new board with given dimension and filled with the given disks.

        - The collection of given disks is a sequence. The element at position I
          in that sequence specifies the disks to be loaded on column I+1 of the
          new board.
        - If there is no matching element for a column, no disks are loaded on
          that column.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The number of elements in the sequence of given disks is between 0
          and the given dimension.
        - Each element of the given sequence of disks is a sequence of
          disks for the new board. The length of each sequence of disks
          is less than or equal to the given dimension incremented with 1.
          Each disk must be a proper disk for the given board.
        NOTE
        - Notice that the resulting board will be a proper board, but not
          necessarily a playable board. Notice also that some disks on the board
          might satisfy the conditions to explode.
    """
    board = {}  # Create an empty board
    for column in range(1, dimension + 1):
        for row in range(1, dimension + 2):
            board[(column, row)] = None

    for column in range(len(given_disks)):  # Fill in the given disks
        for row in range(len(given_disks[column])):
            disk = given_disks[column][row]
            set_disk_at(board, (column + 1, row + 1), disk)

    return board


def get_board_copy(board):
    """
      Return a full copy of the given board.
      - The resulting copy contains copies of the disks stored
         on the original board.
      ASSUMPTIONS
      - The given board is a proper board.
    """
    copy_board = {}

    for column in range(1, dimension(board) + 1):
        for row in range(1, dimension(board) + 2):
            if get_disk_at(board, (column, row)) is None:
                set_disk_at(copy_board, (column, row), None)

            else:
                disk = Disk.get_disk_copy(get_disk_at(board, (column, row)))
                set_disk_at(copy_board, (column, row), disk)

    return copy_board


def dimension(board):
    """
        Return the dimension of the given board.
        - The dimension of a square board is its number of rows or equivalently
          its number of columns.
        - The function returns None if no dimension can be obtained from the given
          board. This is for instance the case if a string, a number, ... is passed
          instead of a board.
        ASSUMPTIONS
        - None (we must be able to use this function at times the thing that
          is given to us is not necessarily a proper board, e.g. in the function
          is_proper_board itself)
    """
    if not isinstance(board, dict):  # Check for wrong datatype
        return None
    else:
        column = 1
        while (column, 1) in board:
            column += 1

        board_dimension = column - 1
        return board_dimension


def get_disk_at(board, position):
    """
        Return the disk at the given position on the given board.
        - None is returned if there is no disk at the given position.
        - The function also returns None if no disk can be obtained from the given
          board at the given position. This is for instance the case if a string,
          a number, ... is passed instead of a board or a position, if the given
          position is outside the boundaries of the given board, ...
        ASSUMPTIONS
        - None (same remark as for the function dimension)
     """
    if not isinstance(position, (tuple, list)) or not isinstance(board, dict):
        return None

    else:
        return board[position]


def set_disk_at(board, position, disk):
    """
        Fill the cell at the given position on the given board with the given disk.
        - The disk nor any other disk will yet explode, even if the conditions
          for having an explosion are satisfied.
        - The given disk may be None, in which case the disk, if any, at the given
          position is removed from the given board, WITHOUT disks at higher positions
          in the column dropping down one position.
        ASSUMPTIONS
        - The given board is a proper board, the given position is a proper
          proper position for the given board and the given disk is a proper
          disk for the given board.
    """
    board[position] = disk


def has_disk_at(board, position):
    """
        Check whether a disk is stored at the given position on the given board.
        - The function returns false if no disk can be obtained from the given
          board at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for that board.
    """
    if board[position] is None:
        return False
    return True


def is_full_column(board, column):
    """
       Check whether the non-overflow part of the given column on the given board
       is completely filled with disks.
       - The overflow cell of a full column may also contain a disk, but it may
         also be empty.
        ASSUMPTIONS
        - The given board is a proper board, and the given column is a proper column
          for that board.
    """
    for row in range(1, dimension(board) + 1):
        if not has_disk_at(board, (column, row)):
            return False

    return True


def is_full(board):
    """
       Check whether the non-overflow part of the  given board is completely
       filled with disks.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for column in range(1, dimension(board) + 1):
        if not is_full_column(board, column):
            return False

    return True


def can_accept_disk(board):
    """
        Check whether the given board can accept an additional disk.
        - True if and only if (1) all overflow cells of the given board are free,
          and (2) at least one of the cells in the non-overflow portion of the
          given board is free.
        ASSUMPTIONS
        - The given board is a proper board.

    """
    if not is_full(board):
        for column in range(1, dimension(board) + 1):
            if has_disk_at(board, (column, dimension(board) + 1)):
                return False
        return True
    return False


def add_disk_on_column(board, disk, column):
    """
        Add the given disk on top of the given column of the given board.
        - The disk is registered at the lowest free position in the given column.
          Nothing happens if the given column is completely filled, including the
          overflow cell of that column.
        - The disk nor any other disk will yet explode, even if the conditions for
          having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for the given board, and the given disk is a proper disk for the given board.
    """
    if not is_full_column(board, column) or not has_disk_at(board, (column, dimension(board) + 1)):
        for row in range(1, dimension(board) + 2):
            if not has_disk_at(board, (column, row)):
                set_disk_at(board, (column, row), disk)
                return board
    return board


def inject_disk_in_column(board, disk, column):
    """
        Inject the given disk at the bottom of the given column of the given board.
        - The disk is registered in the bottom cell of the given column, i.e., in the
          cell at row 1.
        - All disks already in the given column are shifted up one position.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for that board whose overflow cell is free, and the given disk is a
          proper disk for the given board.
    """
    disks_in_column = []

    for row in range(1, dimension(board) + 1):
        list.append(disks_in_column, board[(column, row)])

    set_disk_at(board, (column, 1), disk)
    for row in range(2, dimension(board) + 2):
        set_disk_at(board, (column, row), disks_in_column[row - 2])

    return board


def inject_bottom_row_wrapped_disks(board):
    """
        Insert a bottom row of wrapped disks in the given board.
        - All disks already in the board are shifted up one position.
        - No disk on the given board will explode yet, even if the conditions
          for having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a playable board that can accept a disk.
    """
    for column in range(1, dimension(board) + 1):
        value_disk = randint(1, dimension(board))
        disk = [Disk.WRAPPED, value_disk]
        inject_disk_in_column(board, disk, column)


def remove_disk_at(board, position):
    """
        Remove the disk at the given position from the given board.
        - All disks above the removed disk drop one position down.
        - Nothing happens if no disk is stored at the given position.
        - No disk will explode yet, even if the conditions for having an
          explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, and the given position is
          a proper position for that board.
        NOTE
        - This function must be implemented in a RECURSIVE way.
    """
    dim = dimension(board)
    position_above = Position.up(dim, position)

    if position_above is None or not has_disk_at(board, position_above):
        set_disk_at(board, position, None)
        return board

    else:
        set_disk_at(board, position, get_disk_at(board, position_above))
        return remove_disk_at(board, position_above)


def get_length_vertical_chain(board, position):
    """
        Return the length of the vertical chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a playable board and the given position is a
          proper position for the given
          board.
        NOTE
        - This function must be implemented in a RECURSIVE way.
    """
    if not has_disk_at(board, position):  # No disk at given position
        return 0

    result = get_length_vertical_chain_above(board, position) + position[1]
    # Result is the chain above added with the one below

    return result


def get_length_vertical_chain_above(board, position):
    """
        Return the length of the vertical chain of disks above the
        given position. Zero is returned if no disk is stored just on top of the
        given position.
    """
    row = position[1]

    if row == dimension(board) + 1 or board[Position.up(dimension(board), position)] is None:
        # If there is no disk above
        return 0
    if row >= dimension(board):  # If the position is the overflow position
        return 1
    else:
        result = 1 + get_length_vertical_chain_above(board, (Position.up(dimension(board), position)))
        return result


def get_length_horizontal_chain(board, position):
    """
        Return the length of the horizontal chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    if not has_disk_at(board, position):  # Return 0 if position stores no disk
        return 0

    else:
        length = 1 + get_length_horizontal_chain_to_left(board, position) + get_length_horizontal_chain_to_right(board,
                                                                                                                 position)
        return length  # Length is 1 for the position added with the chain to the left and right


def get_length_horizontal_chain_to_left(board, position):
    """
        Return the length of the horizontal chain of disks to the left of the
        given position. Zero is returned if no disk is stored just left of the
        given position.
    """
    length = 0
    row = position[1]

    for column in range(position[0] - 1, 0, -1):  # Chain to the left
        if has_disk_at(board, (column, row)):
            length += 1
        else:
            return length  # Return if there is a None
    return length  # Return if there isn't a None


def get_length_horizontal_chain_to_right(board, position):
    """
        Return the length of the horizontal chain of disks to the right of the
        given position. Zero is returned if no disk is stored just right of the
        given position.
    """
    length = 0
    row = position[1]

    for column in range(position[0] + 1, dimension(board) + 1, 1):
        if has_disk_at(board, (column ,row)):
            length += 1
        else:
            return length  # Return if there is a None
    return length  # Return if there isn't a None


def is_to_explode(board, position):
    """
        Return a boolean indicating whether the disk, if any, at the given
        position on the given board satisfies the conditions to explode.
        - True if and only if (1) the disk at the given position is visible, and
          (2) the number of the disk is equal to the length of the horizontal chain
          and/or the vertical chain involving that position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    if not has_disk_at(board, position):
        return False

    vertical = get_length_vertical_chain(board, position)
    # Get the length of the vertical chain
    horizontal = get_length_horizontal_chain(board, position)  # Get the length of the horizontal chain

    disk = get_disk_at(board, position)  # Get the disk at the position

    state = Disk.get_state(disk)
    value = Disk.get_value(disk)

    if state == Disk.VISIBLE and (value == horizontal or value == vertical):
        return True

    return False


def get_all_positions_to_explode(board, start_pos=(1, 1)):
    """
        Return a frozen set of all positions on the given board that
        have a disk that satisfies the conditions to explode, starting
        from the given position and proceeding to the top of the board
        using the next function.
        - The function returns the empty set if the given start position
          is None.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given start position is either None or it is a proper position
          for the given board.
        NOTE
        - The second parameter should not be included in the code that
          is given to the students. They must learn to extend functions
          with extra parameters with a default value. The documentation
          of the function must be changed in view of that.
    """
    if start_pos is None:  # Starting position is None
        return frozenset()

    else:
        if is_to_explode(board, start_pos):
            result = frozenset(((start_pos),))
        else:
            result = frozenset()

    return result | get_all_positions_to_explode(board, Position.next(dimension(board), start_pos))


def crack_disks_at(board, positions):
    """
        Crack all disks at the given positions on the given board.
        - Wrapped disks will become cracked, and cracked disks will become
          visible.
        - Some positions may not contain any disk, or may contain non-crackable
          disks.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """
    all_positions_to_crack = list(positions)

    for position in all_positions_to_crack:
        if has_disk_at(board, position):
            disk = get_disk_at(board, position)
            state = Disk.get_state(disk)

            if state == Disk.WRAPPED:  # If the disk is wrapped it should become cracked
                Disk.set_state(disk, Disk.CRACKED)

            elif state == Disk.CRACKED:  # If the disk is cracked it should become visible
                Disk.set_state(disk, Disk.VISIBLE)

    return board


def remove_all_disks_at(board, positions):
    """
        Remove all disks at the given positions on the given board.
        - All disks on top of disks that are removed drop down.
        - Positions in the given collection of positions at which no disk
          is stored, are ignored.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """
    if len(list(positions)) == 0:
        return board
    positions_to_remove = sorted(positions, reverse=True)
    # Reversed sorted list to start with the higher positions to avoid disks falling down and changing position

    for position in positions_to_remove:
        remove_disk_at(board, position)
    return board


### BOARD HELPER FUNCTIONS ###

def print_board(board):
    """
        Print the given board.
        ASSUMPTIONS
        - The given board must be a proper board.
    """
    assert is_proper_board(board)
    # Formatting could be used to improve the layout.
    for row in range(dimension(board) + 1, 0, -1):
        print(end="|")
        for col in range(1, dimension(board) + 1):
            disk = get_disk_at(board, (col, row))
            if disk is None:
                print('   ', end=" |", )
            else:
                status, value = disk
                if status == Disk.WRAPPED:
                    print('%2s' % '\u2B24', end=" |")
                elif status == Disk.CRACKED:
                    print('%4s' % '\u20DD', end=" |")
                else:  # numbered disk
                    print('%3s' % value, end=" |", )
        print()
        if row == dimension(board) + 1:
            print("|" + "----|" * dimension(board))
    print()
