import Drop7.Board as Board
import Drop7.Disk as Disk

wrapped_disk_value_1 = None
wrapped_disk_value_2 = None
wrapped_disk_value_3 = None
wrapped_disk_value_3_B = None
wrapped_disk_value_3_C = None
wrapped_disk_value_5 = None
visible_disk_value_1 = None
visible_disk_value_2 = None
visible_disk_value_2_B = None
visible_disk_value_3 = None
visible_disk_value_3_B = None
visible_disk_value_4 = None
visible_disk_value_6 = None
cracked_disk_value_1 = None
cracked_disk_value_1_B = None
cracked_disk_value_3 = None
cracked_disk_value_4 = None
test_board_4 = None
test_board_6 = None

def set_up():
    """
       This function initializes a large number of disks and two boards
       that can be used in tests. Such a test will then start with an
       invocation of this function
    """
    global\
        wrapped_disk_value_1, wrapped_disk_value_2, wrapped_disk_value_3, \
                wrapped_disk_value_3_C, wrapped_disk_value_3_B, wrapped_disk_value_5, \
        visible_disk_value_1, visible_disk_value_2, visible_disk_value_2_B, \
                visible_disk_value_3, visible_disk_value_3_B, visible_disk_value_4, \
                visible_disk_value_6, \
        cracked_disk_value_1, cracked_disk_value_1_B, cracked_disk_value_3, \
                cracked_disk_value_4, \
        test_board_4, test_board_6

    wrapped_disk_value_1 = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_2 = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_3 = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_B = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_C = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_5 = Disk.init_disk(Disk.WRAPPED, 5)

    visible_disk_value_1 = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_2 = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_2_B = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_3 = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_B = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_4 = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_6 = Disk.init_disk(Disk.VISIBLE, 6)

    cracked_disk_value_1 = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_1_B = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_3 = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_4 = Disk.init_disk(Disk.CRACKED, 4)

    test_board_4 = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (visible_disk_value_1, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_6 = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             [wrapped_disk_value_3_B, wrapped_disk_value_5],
             (visible_disk_value_6, visible_disk_value_3_B, wrapped_disk_value_1),
             (visible_disk_value_1, cracked_disk_value_1,
                    visible_disk_value_4, visible_disk_value_3),
             (cracked_disk_value_1_B,),
             [wrapped_disk_value_3_C, visible_disk_value_2_B]))




def test_Is_Proper_Board__Legal_Board(score, max_score):
    """Function is_proper_board: legal board."""
    max_score.value += 3
    try:
        set_up()
        basic_board = Board.init_board \
            (dimension=4, given_disks= \
                ((None, wrapped_disk_value_3,),
                 [],
                 (visible_disk_value_1, None, wrapped_disk_value_2, visible_disk_value_3)))
        assert Board.is_proper_board(basic_board)
        score.value += 3
    except:
        pass

def test_Is_Proper_Board__No_Board(score, max_score):
    """Function is_proper_board: no board."""
    max_score.value += 1
    try:
        assert not Board.is_proper_board(None)
        score.value += 1
    except:
        pass



def test_Is_Playable_Board__Legal_Board(score, max_score):
    """Function is_playable_board: legal board."""
    max_score.value += 5
    try:
        set_up()
        assert Board.is_playable_board(test_board_4)
        assert Board.is_playable_board(test_board_6)
        score.value += 5
    except:
        pass

def test_Is_Playable_Board__Non_Empty_Overflow_Row(score, max_score):
    """Function is_playable_board: non empty overflow row."""
    max_score.value += 5
    try:
        set_up()
        board = Board.init_board(2,
            ( (wrapped_disk_value_1,visible_disk_value_2,cracked_disk_value_1),) )
        assert Board.is_playable_board(board)
        score.value += 5
    except:
        pass

def test_Is_Proper_Board__Board_With_Gaps(score, max_score):
    """Function is_playable_board: gaps in columns."""
    max_score.value += 5
    try:
        board = Board.init_board(
            dimension=4, given_disks=\
                [[Disk.init_disk(Disk.VISIBLE, 1), None, Disk.init_disk(Disk.CRACKED,2)]])
        assert Board.is_proper_board(board)
        assert not Board.is_playable_board(board)
        score.value += 5
    except:
        pass

def test_Is_Proper_Board__Same_Disk_At_Several_Positions(score, max_score):
    """Function is_playable_board: same disk at several positions."""
    max_score.value += 10
    try:
        set_up()
        Board.set_disk_at(test_board_4, (4, 4), wrapped_disk_value_3)
        assert Board.is_proper_board(test_board_4)
        assert not Board.is_playable_board(test_board_4)
        score.value += 10
    except:
        pass



def test_Init_Board__No_Disks(score, max_score):
    """Function init_board: no disks."""
    max_score.value += 4
    try:
        board = Board.init_board(dimension=2)
        assert Board.dimension(board) == 2
        score.value += 2
        assert (Board.get_disk_at(board, (1, 1)) is None)
        assert (Board.get_disk_at(board, (1, 2)) is None)
        assert (Board.get_disk_at(board, (2, 1)) is None)
        assert (Board.get_disk_at(board, (2, 2)) is None)
        score.value += 2
    except:
        pass

def test_Init_Board__All_Disks(score, max_score):
    """Function init_board: all disks."""
    max_score.value += 5
    try:
        set_up()
        board = Board.init_board \
            (dimension=2, given_disks= \
                ((visible_disk_value_1, wrapped_disk_value_2, visible_disk_value_2_B),
                 (cracked_disk_value_1, visible_disk_value_2, wrapped_disk_value_1)))
        assert Board.dimension(board) == 2
        score.value += 1
        assert Board.get_disk_at(board, (1, 1)) == visible_disk_value_1
        assert Board.get_disk_at(board, (1, 2)) == wrapped_disk_value_2
        assert Board.get_disk_at(board, (1, 3)) == visible_disk_value_2_B
        assert Board.get_disk_at(board, (2, 1)) == cracked_disk_value_1
        assert Board.get_disk_at(board, (2, 2)) == visible_disk_value_2
        assert Board.get_disk_at(board, (2, 3)) == wrapped_disk_value_1
        score.value += 4
    except:
        pass

def test_Init_Board__Partial_Fill(score, max_score):
    """Function init_board: partial fill."""
    max_score.value += 7
    try:
        set_up()
        assert Board.dimension(test_board_4) == 4
        score.value += 1
        assert (Board.get_disk_at(test_board_4, (1, 1)) == wrapped_disk_value_3)
        assert (Board.get_disk_at(test_board_4, (1, 2)) == None)
        assert (Board.get_disk_at(test_board_4, (1, 3)) == None)
        assert (Board.get_disk_at(test_board_4, (1, 4)) == None)
        assert (Board.get_disk_at(test_board_4, (2, 1)) == None)
        assert (Board.get_disk_at(test_board_4, (2, 2)) == None)
        assert (Board.get_disk_at(test_board_4, (2, 3)) == None)
        assert (Board.get_disk_at(test_board_4, (2, 4)) == None)
        assert (Board.get_disk_at(test_board_4, (3, 1)) == visible_disk_value_1)
        assert (Board.get_disk_at(test_board_4, (3, 2)) == cracked_disk_value_1)
        assert (Board.get_disk_at(test_board_4, (3, 3)) == wrapped_disk_value_2)
        assert (Board.get_disk_at(test_board_4, (3, 4)) == visible_disk_value_3)
        assert (Board.get_disk_at(test_board_4, (4, 1)) == None)
        assert (Board.get_disk_at(test_board_4, (4, 2)) == None)
        assert (Board.get_disk_at(test_board_4, (4, 3)) == None)
        assert (Board.get_disk_at(test_board_4, (4, 4)) == None)
        score.value += 6
    except:
        pass



def test_Get_Board_Copy__Single_Case(score, max_score):
    """Function get_board_copy: single case."""
    max_score.value += 13
    try:
        set_up()
        overflow_disk = Disk.init_disk(Disk.VISIBLE, 3)
        Board.set_disk_at(test_board_4, (3,5), overflow_disk)
        copy = Board.get_board_copy(test_board_4)
        assert Board.dimension(copy) == 4
        score.value += 1
        assert (Board.get_disk_at(copy, (1, 1)) == Disk.init_disk(Disk.WRAPPED,3))
        assert Board.get_disk_at(copy, (1, 1)) is not wrapped_disk_value_3
        assert (Board.get_disk_at(copy, (1, 2)) == None)
        assert (Board.get_disk_at(copy, (1, 3)) == None)
        assert (Board.get_disk_at(copy, (1, 4)) == None)
        assert (Board.get_disk_at(copy, (2, 1)) == None)
        assert (Board.get_disk_at(copy, (2, 2)) == None)
        assert (Board.get_disk_at(copy, (2, 3)) == None)
        assert (Board.get_disk_at(copy, (2, 4)) == None)
        assert (Board.get_disk_at(copy, (3, 1)) == Disk.init_disk(Disk.VISIBLE, 1))
        assert Board.get_disk_at(copy, (3, 1)) is not visible_disk_value_1
        assert (Board.get_disk_at(copy, (3, 2)) == Disk.init_disk(Disk.CRACKED, 1))
        assert Board.get_disk_at(copy, (1, 1)) is not cracked_disk_value_1
        assert (Board.get_disk_at(copy, (3, 3)) == Disk.init_disk(Disk.WRAPPED, 2))
        assert Board.get_disk_at(copy, (1, 1)) is not wrapped_disk_value_2
        assert (Board.get_disk_at(copy, (3, 4)) == Disk.init_disk(Disk.VISIBLE, 3))
        assert Board.get_disk_at(copy, (1, 1)) is not visible_disk_value_3
        assert (Board.get_disk_at(copy, (3, 5)) == Disk.init_disk(Disk.VISIBLE, 3))
        assert Board.get_disk_at(copy, (3, 5)) is not overflow_disk
        assert (Board.get_disk_at(copy, (4, 1)) == None)
        assert (Board.get_disk_at(copy, (4, 2)) == None)
        assert (Board.get_disk_at(copy, (4, 3)) == None)
        assert (Board.get_disk_at(copy, (4, 4)) == None)
        score.value += 2
        # Checking that the copy has its own data structure.
        Board.set_disk_at(test_board_4, (4, 1), Disk.init_disk(Disk.WRAPPED, 2))
        assert not Board.has_disk_at(copy,(4,1))
        score.value += 5
        # Checking that the copy stores copies of the disks.
        disk = Board.get_disk_at(test_board_4, (1, 1))
        Disk.set_state(disk,Disk.VISIBLE)
        assert Disk.get_state(Board.get_disk_at(copy,(1,1))) == Disk.WRAPPED
        score.value += 5
    except:
        pass



def test_dimension__ImproperBoard(score,max_score):
    """Function dimension: improper board."""
    max_score.value += 1
    try:
        assert Board.dimension("abc") is None
        score.value += 1
    except:
        pass



def test_Get_Disk_At__Effective_Disk(score, max_score):
    """Function get_disk_at: effective disk."""
    max_score.value += 7
    try:
        set_up()
        assert Board.get_disk_at(test_board_4, (1, 1)) == wrapped_disk_value_3
        score.value += 1
        # Checking whether the actual disk is returned (and not a copy)
        wrapped_disk_value_7 = wrapped_disk_value_3
        Disk.set_value(wrapped_disk_value_7,7)
        assert Board.get_disk_at(test_board_4, (1, 1)) == wrapped_disk_value_7
        score.value += 6
    except:
        pass

def test_Get_Disk_At__No_Disk(score, max_score):
    """Function get_disk_at: no disk."""
    max_score.value += 1
    try:
        set_up()
        assert Board.get_disk_at(test_board_4, (1, 3)) is None
        score.value += 1
    except:
        pass

def test_getDiskAt__ImproperBoardOrPosition(score,max_score):
    """Function get_disk_at: improper board or improper position."""
    max_score.value += 1
    try:
        set_up()
        assert Board.get_disk_at("abc",(1,1)) is None
        assert Board.get_disk_at(test_board_4,"xyz") is None
        score.value += 1
    except:
        pass



def test_Set_Disk_At__Adjacent_Disk(score, max_score):
    """Function set_disk_at: adjacent disk."""
    max_score.value += 7
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.set_disk_at(test_board_4, (1, 2), disk)
        assert Board.get_disk_at(test_board_4, (1, 2)) == disk
        score.value += 1
        # Checking whether the actual disk is registered (and not a copy)
        Disk.set_state(disk,Disk.WRAPPED)
        assert Board.get_disk_at(test_board_4, (1, 2)) == disk
        score.value += 6
    except:
        pass

def test_Set_Disk_At__Non_Adjacent_Disk(score, max_score):
    """Function set_disk_at: non adjacent disk."""
    max_score.value += 1
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.set_disk_at(test_board_4, (1, 4), disk)
        assert Board.get_disk_at(test_board_4, (1, 4)) == disk
        score.value += 1
    except:
        pass

def test_Set_Disk_At__No_Disk(score, max_score):
    """Function set_disk_at: no disk."""
    max_score.value += 2
    try:
        set_up()
        Board.set_disk_at(test_board_4, (3, 2), None)
        assert Board.get_disk_at(test_board_4, (3, 2)) == None
        score.value += 2
    except:
        pass



def test_Has_Disk_At__Effective_Disk(score, max_score):
    """Function has_disk_at: effective disk."""
    max_score.value += 1
    try:
        set_up()
        assert Board.has_disk_at(test_board_4, (1, 1))
        score.value += 1
    except:
        pass

def test_Has_Disk_At__No_Disk(score, max_score):
    """Function has_disk_at: no disk."""
    max_score.value += 1
    try:
        set_up()
        assert not Board.has_disk_at(test_board_4, (1, 3))
        score.value += 1
    except:
        pass



def test_is_Full_Column__NotFull(score, max_score):
    """Function is_full_column: column not full."""
    max_score.value += 1
    try:
        set_up()
        assert not Board.is_full_column(test_board_4, 1)
        assert not Board.is_full_column(test_board_4, 2)
        assert not Board.is_full_column(test_board_4, 4)
        score.value += 1
    except:
        pass

def test_is_Full_Column__Full(score, max_score):
    """Function is_full_column: column full."""
    max_score.value += 1
    try:
        set_up()
        assert Board.is_full_column(test_board_4, 3)
        Board.set_disk_at(test_board_4,(3,5),Disk.init_disk(Disk.VISIBLE,2))
        assert Board.is_full_column(test_board_4, 3)
        score.value += 1
    except:
        pass



def test_is_Full___NotFull(score, max_score):
    """Function is_full: board not full."""
    max_score.value += 1
    try:
        set_up()
        empty_board = Board.init_board(3)
        allmost_full_board = Board.init_board(2,[
            [visible_disk_value_1,visible_disk_value_2],
            [cracked_disk_value_1]]
        )
        assert not Board.is_full(test_board_4)
        assert not Board.is_full(test_board_6)
        assert not Board.is_full(empty_board)
        assert not Board.is_full(allmost_full_board)
        score.value += 1
    except:
        pass

def test_is_Full___Full(score, max_score):
    """Function is_full: board full."""
    max_score.value += 1
    try:
        set_up()
        board1 = Board.init_board(1,((visible_disk_value_1,),))
        board2 = Board.init_board(2,(
            (visible_disk_value_1,visible_disk_value_2),
            (cracked_disk_value_1,wrapped_disk_value_1) )
        )
        assert Board.is_full(board1)
        assert Board.is_full(board2)
        score.value += 1
    except:
        pass



def test_can_Accept_Disk___True_Case(score, max_score):
    """Function can_accept_disk: true case."""
    max_score.value += 2
    try:
        set_up()
        board = Board.init_board(2,(
            (visible_disk_value_1,visible_disk_value_2),
            (cracked_disk_value_1,) )
        )
        assert Board.can_accept_disk(board)
        score.value += 2
    except:
        pass

def test_can_Accept_Disk___Overflow_Cell_With_Disk(score, max_score):
    """Function can_accept_disk: overflow cell with disk."""
    max_score.value += 2
    try:
        set_up()
        board = Board.init_board(2,(
            (None,None,cracked_disk_value_1_B),
            (None,) )
        )
        assert not Board.can_accept_disk(board)
        score.value += 2
    except:
        pass

def test_can_Accept_Disk___No_Free_Cell(score, max_score):
    """Function can_accept_disk: no free cell."""
    max_score.value += 2
    try:
        set_up()
        board = Board.init_board(2,(
            (cracked_disk_value_1_B,visible_disk_value_2),
            (wrapped_disk_value_1,wrapped_disk_value_2) )
        )
        assert not Board.can_accept_disk(board)
        score.value += 2
    except:
        pass



def test_Add_Disk_On_Column__Empty_Column(score, max_score):
    """Function add_disk_on_column: empty column."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.add_disk_on_column(test_board_4, disk, 2)
        assert Board.get_disk_at(test_board_4, (2, 1)) == disk
        score.value += 2
    except:
        pass

def test_Add_Disk_On_Column__Partial_Column(score, max_score):
    """Function add_disk_on_column: partial column."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.add_disk_on_column(test_board_4, disk, 1)
        assert Board.get_disk_at(test_board_4, (1, 2)) == disk
        score.value += 2
    except:
        pass

def test_Add_Disk_On_Column__Full_Column_Empty_Overflow_Cell(score, max_score):
    """Function add_disk_on_column: full column with empty overflow cell."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.add_disk_on_column(test_board_4, disk, 3)
        assert Board.get_disk_at(test_board_4, (3, 5)) == disk
        score.value += 2
    except:
        pass

def test_Add_Disk_On_Column__Full_Column_Filled_Overflow_Cell(score, max_score):
    """Function add_disk_on_column: full column with empty overflow cell."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.set_disk_at(test_board_4, (3,5), disk)
        Board.add_disk_on_column(test_board_4, Disk.init_disk(Disk.CRACKED,2), 3)
        assert Board.get_disk_at(test_board_4, (3, 5)) == disk
        score.value += 2
    except:
        pass



def test_Inject_Disk_In_Column__Empty_Column(score, max_score):
    """Function inject_disk_in_column: empty column."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.inject_disk_in_column(test_board_4, disk, 2)
        assert Board.get_disk_at(test_board_4, (2, 1)) == disk
        score.value += 2
    except:
        pass

def test_Inject_Disk_In_Column__Partial_Column(score, max_score):
    """Function inject_disk_in_column: partial column."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.inject_disk_in_column(test_board_4, disk, 1)
        assert Board.get_disk_at(test_board_4, (1, 1)) == disk
        assert Board.get_disk_at(test_board_4, (1, 2)) == wrapped_disk_value_3
        score.value += 2
    except:
        pass

def test_Inject_Disk_In_Column__Full_Column_Empty_Overflow_Cell(score, max_score):
    """Function inject_disk_in_column: full column with empty overflow cell."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,2)
        Board.inject_disk_in_column(test_board_4, disk, 3)
        assert Board.get_disk_at(test_board_4, (3, 1)) == disk
        assert Board.get_disk_at(test_board_4, (3, 2)) == visible_disk_value_1
        assert Board.get_disk_at(test_board_4, (3, 3)) == cracked_disk_value_1
        assert Board.get_disk_at(test_board_4, (3, 4)) == wrapped_disk_value_2
        assert Board.get_disk_at(test_board_4, (3, 5)) == visible_disk_value_3
        score.value += 2
    except:
        pass



def test_Insert_Bottom_Row_Wrapped_Disks__Single_Case(score, max_score):
    """Function inject_bottom_row_wrapped_disks: single case."""
    max_score.value += 4
    try:
        set_up()
        Board.inject_bottom_row_wrapped_disks(test_board_4)
        assert Disk.get_state(Board.get_disk_at(test_board_4, (1, 1))) == Disk.WRAPPED
        assert Board.get_disk_at(test_board_4, (1, 2)) == wrapped_disk_value_3
        assert not Board.has_disk_at(test_board_4,(1,3))
        assert Disk.get_state(Board.get_disk_at(test_board_4, (2, 1))) == Disk.WRAPPED
        assert not Board.has_disk_at(test_board_4,(2,2))
        assert Disk.get_state(Board.get_disk_at(test_board_4, (3, 1))) == Disk.WRAPPED
        assert Board.get_disk_at(test_board_4, (3, 2)) == visible_disk_value_1
        assert Board.get_disk_at(test_board_4, (3, 5)) == visible_disk_value_3
        assert Disk.get_state(Board.get_disk_at(test_board_4, (4, 1))) == Disk.WRAPPED
        assert not Board.has_disk_at(test_board_4,(4,2))
        score.value += 4
    except:
        pass



def test_Remove_Disk_At__No_Disk(score, max_score):
    """Function remove_disk_at: no disk at position."""
    max_score.value += 2
    try:
        set_up()
        Board.remove_disk_at(test_board_4, (2, 4))
        assert not Board.has_disk_at(test_board_4, (2, 4))
        assert not Board.has_disk_at(test_board_4, (2, 1))
        score.value += 2
    except:
        pass

def test_Remove_Disk_At__Overflow_Disk(score, max_score):
    """Function remove_disk_at: overflow disk."""
    max_score.value += 2
    try:
        set_up()
        disk = Disk.init_disk(Disk.VISIBLE,4)
        Board.set_disk_at(test_board_4,(3,5),disk)
        Board.remove_disk_at(test_board_4, (3, 5))
        assert not Board.has_disk_at(test_board_4, (3, 5))
        assert Board.get_disk_at(test_board_4, (3, 4)) == visible_disk_value_3
        score.value += 2
    except:
        pass

def test_Remove_Disk_At__Top_Disk(score, max_score):
    """Function remove_disk_at: top disk."""
    max_score.value += 2
    try:
        set_up()
        Board.remove_disk_at(test_board_4, (3, 4))
        assert not Board.has_disk_at(test_board_4, (3, 4))
        assert Board.get_disk_at(test_board_4, (3, 3)) == wrapped_disk_value_2
        score.value += 2
    except:
        pass

def test_Remove_Disk_At__Intermediate_Disk(score, max_score):
    """Function remove_disk_at: intermediate disk."""
    max_score.value += 5
    try:
        set_up()
        Board.remove_disk_at(test_board_4, (3, 2))
        assert Board.get_disk_at(test_board_4, (3, 2)) == wrapped_disk_value_2
        assert not Board.has_disk_at(test_board_4, (3, 3)) == visible_disk_value_3
        score.value += 5
    except:
        pass

def test_Remove_Disk_At__Bottom_Disk(score, max_score):
    """Function remove_disk_at: bottom disk."""
    max_score.value += 5
    try:
        set_up()
        Board.remove_disk_at(test_board_4, (3, 1))
        assert Board.get_disk_at(test_board_4, (3, 1)) == cracked_disk_value_1
        assert Board.get_disk_at(test_board_4, (3, 2)) == wrapped_disk_value_2
        assert not Board.has_disk_at(test_board_4, (3, 3)) == visible_disk_value_3
        score.value += 5
    except:
        pass



def test_Get_Length_Vertical_Chain__No_Disk(score, max_score):
    """Function get_length_vertical_chain: no disk at position."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_vertical_chain(test_board_6, (1, 3)) == 0
        assert Board.get_length_vertical_chain(test_board_6, (5, 6)) == 0
        score.value += 2
    except:
        pass

def test_Get_Length_Vertical_Chain__Length_1(score, max_score):
    """Function get_length_vertical_chain: chain of length 1."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_vertical_chain(test_board_6, (1, 1)) == 1
        score.value += 2
    except:
        pass

def test_Get_Length_Vertical_Chain__Medium_Length(score, max_score):
    """Function get_length_vertical_chain: chain of medium length."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_vertical_chain(test_board_6, (3, 1)) == 3
        score.value += 2
    except:
        pass

def test_Get_Length_Vertical_Chain__Maximum_Length(score, max_score):
    """Function get_length_vertical_chain: chain of maximum length."""
    max_score.value += 3
    try:
        set_up()
        Board.set_disk_at(test_board_4,(3,5),Disk.init_disk(Disk.CRACKED,4))
        assert Board.get_length_vertical_chain(test_board_4, (3, 2)) == 5
        score.value += 3
    except:
        pass



def test_Get_Length_Horizontal_Chain__No_Disk(score, max_score):
    """Function get_length_horizontal_chain: no disk at position."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_horizontal_chain(test_board_6, (1, 2)) == 0
        assert Board.get_length_horizontal_chain(test_board_6, (4, 6)) == 0
        score.value += 2
    except:
        pass

def test_Get_Length_Horizontal_Chain__Length1(score, max_score):
    """Function get_length_horizontal_chain: chain of length 1."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_horizontal_chain(test_board_6, (4, 4)) == 1
        score.value += 2
    except:
        pass

def test_Get_Length_Horizontal_Chain__Medium_Length(score, max_score):
    """Function get_length_horizontal_chain: chain of medium length."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_horizontal_chain(test_board_6, (3, 2)) == 3
        score.value += 2
    except:
        pass

def test_Get_Length_Horizontal_Chain__Maximum_Length(score, max_score):
    """Function get_length_horizontal_chain: chain of maximum length."""
    max_score.value += 2
    try:
        set_up()
        assert Board.get_length_horizontal_chain(test_board_6, (2, 1)) == 6
        score.value += 2
    except:
        pass



def test_Is_To_Explode__No_Disk(score, max_score):
    """Function is_to_explode: no disk at position."""
    max_score.value += 2
    try:
        set_up()
        assert not Board.is_to_explode(test_board_6, (1, 3))
        score.value += 2
    except:
        pass

def test_Is_To_Explode__Disk_Not_Visible(score, max_score):
    """Function is_to_explode: disk at position not visible."""
    max_score.value += 4
    try:
        set_up()
        assert not Board.is_to_explode(test_board_6, (2, 2))
        assert not Board.is_to_explode(test_board_6, (5, 1))
        score.value += 4
    except:
        pass

def test_Is_To_Explode__No_Matching_Chain(score, max_score):
    """Function is_to_explode: value of disk at position differs from chain lengths."""
    max_score.value += 4
    try:
        set_up()
        assert not Board.is_to_explode(test_board_6, (4, 4))
        assert not Board.is_to_explode(test_board_6, (4, 1))
        score.value += 4
    except:
        pass

def test_Is_To_Explode__Matching_Horizontal_Chain(score, max_score):
    """Function is_to_explode: value of disk at position matches length of horizontal chain."""
    max_score.value += 6
    try:
        set_up()
        assert Board.is_to_explode(test_board_6, (3, 1))
        assert Board.is_to_explode(test_board_6, (3, 2))
        score.value += 6
    except:
        pass

def test_Is_To_Explode__Matching_Vertical_Chain(score, max_score):
    """Function is_to_explode: value of disk at position matches length of vertical chain."""
    max_score.value += 6
    try:
        set_up()
        assert Board.is_to_explode(test_board_6, (4, 3))
        assert Board.is_to_explode(test_board_6, (6, 2))
        assert Board.is_to_explode(test_board_6, (3, 2))
        score.value += 6
    except:
        pass



def test_Get_All_Positions_To_Explode__No_Disks_To_Explode(score, max_score):
    """Function mark_all_positions_to_explode: no disks to explode."""
    max_score.value += 4
    try:
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((Disk.init_disk(Disk.WRAPPED,3),),
                 [Disk.init_disk(Disk.WRAPPED,3), Disk.init_disk(Disk.WRAPPED, 2)],
                 (Disk.init_disk(Disk.VISIBLE,5), Disk.init_disk(Disk.VISIBLE, 4), Disk.init_disk(Disk.WRAPPED, 1)),
                 (Disk.init_disk(Disk.VISIBLE, 1), Disk.init_disk(Disk.CRACKED, 1), Disk.init_disk(Disk.VISIBLE, 3), Disk.init_disk(Disk.VISIBLE, 3)),
                 ([]),
                 [Disk.init_disk(Disk.WRAPPED,3), Disk.init_disk(Disk.VISIBLE, 3)]))
        assert Board.get_all_positions_to_explode(board) == frozenset()
        score.value += 4
    except:
        pass

def test_Get_All_Positions_To_Explode__Several_Disks_To_Explode(score, max_score):
    """Function get_all_positions_to_explode: several disks to explode."""
    max_score.value += 8
    try:
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((Disk.init_disk(Disk.VISIBLE, 4),),
                 [Disk.init_disk(Disk.WRAPPED,3), Disk.init_disk(Disk.VISIBLE, 2)],
                 (Disk.init_disk(Disk.VISIBLE, 5), Disk.init_disk(Disk.VISIBLE, 4),
                    Disk.init_disk(Disk.WRAPPED, 1)),
                 (Disk.init_disk(Disk.VISIBLE, 4), Disk.init_disk(Disk.CRACKED, 1),
                    Disk.init_disk(Disk.VISIBLE, 2), Disk.init_disk(Disk.VISIBLE, 4)),
                 ([]),
                 [Disk.init_disk(Disk.WRAPPED,3), Disk.init_disk(Disk.VISIBLE, 3),
                  Disk.init_disk(Disk.WRAPPED,2), Disk.init_disk(Disk.CRACKED,2),
                  Disk.init_disk(Disk.WRAPPED,4), Disk.init_disk(Disk.CRACKED,5),
                  Disk.init_disk(Disk.VISIBLE,1)]))
        assert Board.get_all_positions_to_explode(board) == \
               frozenset({(1,1), (2,2), (4,1), (4,3), (4,4), (6,7) })
        score.value += 8
    except:
        pass



def test_Crack_Disks_At__No_Positions(score,max_score):
    """Function crack_disks_at: empty collection of positions."""
    max_score.value += 1
    try:
        set_up()
        Board.crack_disks_at(test_board_6,set())
        assert Disk.get_state(Board.get_disk_at(test_board_6,(1,1))) == Disk.WRAPPED
        assert Disk.get_state(Board.get_disk_at(test_board_6,(4,2))) == Disk.CRACKED
        score.value += 1
    except:
        pass


def test_Crack_Disks_At__Several_Positions(score,max_score):
    """Function crack_disks_at: non-empty collection of positions."""
    max_score.value += 6
    try:
        set_up()
        Board.set_disk_at(test_board_6,(4,5),Disk.init_disk(Disk.WRAPPED,3))
        Board.set_disk_at(test_board_6,(4,6),Disk.init_disk(Disk.CRACKED,2))
        Board.set_disk_at(test_board_6,(4,7),Disk.init_disk(Disk.CRACKED,6))
        Board.crack_disks_at(test_board_6,set([(1,1),(4,2),(4,1),(4,7),(5,3)]))
        assert Disk.get_state(Board.get_disk_at(test_board_6,(1,1))) == Disk.CRACKED
        assert Disk.get_state(Board.get_disk_at(test_board_6,(4,2))) == Disk.VISIBLE
        assert Disk.get_state(Board.get_disk_at(test_board_6,(4,1))) == Disk.VISIBLE
        assert not Board.has_disk_at(test_board_6,(5,3))
        assert Disk.get_state(Board.get_disk_at(test_board_6,(4,7))) == Disk.VISIBLE
        score.value += 6
    except:
        pass



def test_Remove_All_Disks_At__PositionsInDifferentColumns(score,max_score):
    """Function remove_all_disks_at: positions in different columns."""
    max_score.value += 6
    try:
        set_up()
        Board.set_disk_at(test_board_6,(4,5),Disk.init_disk(Disk.WRAPPED,3))
        Board.set_disk_at(test_board_6,(4,6),Disk.init_disk(Disk.CRACKED,2))
        Board.set_disk_at(test_board_6,(4,7),Disk.init_disk(Disk.CRACKED,6))
        Board.remove_all_disks_at(test_board_6,set([(1,1),(2,2),(4,2)]))
        assert not Board.has_disk_at(test_board_6,(1,1))
        assert Board.get_disk_at(test_board_6,(2,1)) == wrapped_disk_value_3_B
        assert not Board.has_disk_at(test_board_6,(2,2))
        assert Board.get_disk_at(test_board_6,(4,1)) == visible_disk_value_1
        assert Board.get_disk_at(test_board_6,(4,2)) == visible_disk_value_4
        assert Board.get_disk_at(test_board_6,(4,3)) == visible_disk_value_3
        assert not Board.has_disk_at(test_board_6,(4,7))
        score.value += 6
    except:
        pass

def test_Remove_All_Disks_At__FreePositions(score,max_score):
    """Function remove_all_disks_at: free positions."""
    max_score.value += 3
    try:
        set_up()
        Board.remove_all_disks_at(test_board_6,set([(1,2),(4,2),(5,3)]))
        assert not Board.has_disk_at(test_board_6,(1,2))
        assert Board.get_disk_at(test_board_6,(1,1)) == wrapped_disk_value_3
        assert not Board.has_disk_at(test_board_6,(5,3))
        score.value += 3
    except:
        pass

def test_Remove_All_Disks_At__SeveralPositionsInSameColumn(score,max_score):
    """Function remove_all_disks_at: several positions in same column."""
    max_score.value += 10
    try:
        set_up()
        Board.remove_all_disks_at(test_board_6,set([(2,1),(2,2),(3,1),(3,3),(4,2),(4,4)]))
        assert not Board.has_disk_at(test_board_6,(2,1))
        assert not Board.has_disk_at(test_board_6,(2,2))
        assert Board.get_disk_at(test_board_6,(3,1)) == visible_disk_value_3_B
        assert not Board.has_disk_at(test_board_6,(3,2))
        assert Board.get_disk_at(test_board_6,(4,1)) == visible_disk_value_1
        assert Board.get_disk_at(test_board_6,(4,2)) == visible_disk_value_4
        assert not Board.has_disk_at(test_board_6,(4,3))
        score.value += 10
    except:
        pass



board_test_functions = \
    {
        test_Is_Proper_Board__Legal_Board,
        test_Is_Proper_Board__Board_With_Gaps,
        test_Is_Proper_Board__No_Board,
        test_Is_Proper_Board__Same_Disk_At_Several_Positions,
        test_Is_Playable_Board__Legal_Board,
        test_Is_Playable_Board__Non_Empty_Overflow_Row,
        test_Init_Board__No_Disks,
        test_Init_Board__All_Disks,
        test_Init_Board__Partial_Fill,
        test_Get_Board_Copy__Single_Case,
        test_dimension__ImproperBoard,
        test_Get_Disk_At__Effective_Disk,
        test_Get_Disk_At__No_Disk,
        test_getDiskAt__ImproperBoardOrPosition,
        test_Has_Disk_At__Effective_Disk,
        test_Has_Disk_At__No_Disk,
        test_is_Full_Column__NotFull,
        test_is_Full_Column__Full,
        test_is_Full___NotFull,
        test_is_Full___Full,
        test_can_Accept_Disk___True_Case,
        test_can_Accept_Disk___Overflow_Cell_With_Disk,
        test_can_Accept_Disk___No_Free_Cell,
        test_Set_Disk_At__Adjacent_Disk,
        test_Set_Disk_At__Non_Adjacent_Disk,
        test_Set_Disk_At__No_Disk,
        test_Add_Disk_On_Column__Empty_Column,
        test_Add_Disk_On_Column__Partial_Column,
        test_Add_Disk_On_Column__Full_Column_Empty_Overflow_Cell,
        test_Add_Disk_On_Column__Full_Column_Filled_Overflow_Cell,
        test_Inject_Disk_In_Column__Empty_Column,
        test_Inject_Disk_In_Column__Partial_Column,
        test_Inject_Disk_In_Column__Full_Column_Empty_Overflow_Cell,
        test_Insert_Bottom_Row_Wrapped_Disks__Single_Case,
        test_Remove_Disk_At__No_Disk,
        test_Remove_Disk_At__Overflow_Disk,
        test_Remove_Disk_At__Top_Disk,
        test_Remove_Disk_At__Intermediate_Disk,
        test_Remove_Disk_At__Bottom_Disk,
        test_Get_Length_Horizontal_Chain__No_Disk,
        test_Get_Length_Horizontal_Chain__Length1,
        test_Get_Length_Horizontal_Chain__Medium_Length,
        test_Get_Length_Horizontal_Chain__Maximum_Length,
        test_Get_Length_Vertical_Chain__No_Disk,
        test_Get_Length_Vertical_Chain__Length_1,
        test_Get_Length_Vertical_Chain__Medium_Length,
        test_Get_Length_Vertical_Chain__Maximum_Length,
        test_Is_To_Explode__No_Disk,
        test_Is_To_Explode__Disk_Not_Visible,
        test_Is_To_Explode__No_Matching_Chain,
        test_Is_To_Explode__Matching_Horizontal_Chain,
        test_Is_To_Explode__Matching_Vertical_Chain,
        test_Get_All_Positions_To_Explode__No_Disks_To_Explode,
        test_Get_All_Positions_To_Explode__Several_Disks_To_Explode,
        test_Crack_Disks_At__No_Positions,
        test_Crack_Disks_At__Several_Positions,
        test_Remove_All_Disks_At__PositionsInDifferentColumns,
        test_Remove_All_Disks_At__FreePositions,
        test_Remove_All_Disks_At__SeveralPositionsInSameColumn,
    }
