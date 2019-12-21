import Drop7.Position as Position
import Drop7.Disk as Disk
import Drop7.Board as Board
import Drop7.Drop7 as Drop7

wrapped_disk_value_1 = None
wrapped_disk_value_1_B = None
wrapped_disk_value_1_C = None
wrapped_disk_value_1_D = None
wrapped_disk_value_2 = None
wrapped_disk_value_2_B = None
wrapped_disk_value_2_C = None
wrapped_disk_value_2_D = None
wrapped_disk_value_2_E = None
wrapped_disk_value_3 = None
wrapped_disk_value_3_B = None
wrapped_disk_value_3_C = None
wrapped_disk_value_3_D = None
wrapped_disk_value_3_E = None
wrapped_disk_value_4 = None
wrapped_disk_value_4_B = None
wrapped_disk_value_5 = None
visible_disk_value_1 = None
visible_disk_value_1_B = None
visible_disk_value_2 = None
visible_disk_value_2_B = None
visible_disk_value_3 = None
visible_disk_value_3_B = None
visible_disk_value_3_C = None
visible_disk_value_3_D = None
visible_disk_value_4 = None
visible_disk_value_4_B = None
visible_disk_value_4_C = None
visible_disk_value_5 = None
visible_disk_value_5_B = None
visible_disk_value_5_C = None
visible_disk_value_5_D = None
visible_disk_value_5_E = None
visible_disk_value_5_F = None
visible_disk_value_5_G = None
visible_disk_value_6 = None
visible_disk_value_6_B = None
cracked_disk_value_1 = None
cracked_disk_value_1_B = None
cracked_disk_value_2 = None
cracked_disk_value_2_B = None
cracked_disk_value_3 = None
cracked_disk_value_3_B = None
cracked_disk_value_4 = None
cracked_disk_value_4_B = None
cracked_disk_value_4_C = None
cracked_disk_value_5 = None
test_board_4 = None
test_board_4_alias = None
test_board_6 = None
test_board_6_alias = None


def set_up():
    global \
        wrapped_disk_value_1, wrapped_disk_value_1_B, wrapped_disk_value_1_C, \
        wrapped_disk_value_1_D, wrapped_disk_value_2, wrapped_disk_value_2_B, \
        wrapped_disk_value_2_C, wrapped_disk_value_2_D, wrapped_disk_value_2_E, \
        wrapped_disk_value_3, wrapped_disk_value_3_C, wrapped_disk_value_3_D, \
        wrapped_disk_value_3_B, wrapped_disk_value_3_E, wrapped_disk_value_4, \
        wrapped_disk_value_4_B, wrapped_disk_value_5, \
        visible_disk_value_1, visible_disk_value_1_B, visible_disk_value_2, \
        visible_disk_value_2_B, visible_disk_value_3, visible_disk_value_3_B, \
        visible_disk_value_3_C, visible_disk_value_3_D, visible_disk_value_4, \
        visible_disk_value_4_B, visible_disk_value_4_C, visible_disk_value_5, \
        visible_disk_value_5_B, visible_disk_value_5_C, visible_disk_value_5_D, \
        visible_disk_value_5_E, visible_disk_value_5_F, visible_disk_value_5_G, \
        visible_disk_value_6, visible_disk_value_6_B, \
        cracked_disk_value_1, cracked_disk_value_1_B, cracked_disk_value_2, \
        cracked_disk_value_2_B, cracked_disk_value_3, cracked_disk_value_3_B, \
        cracked_disk_value_4, cracked_disk_value_4_B, cracked_disk_value_4_C, \
        cracked_disk_value_5, \
        test_board_4, test_board_4_alias, test_board_6, test_board_6_alias

    wrapped_disk_value_1 = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_B = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_C = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_D = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_2 = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_B = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_C = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_D = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_E = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_3 = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_B = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_C = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_D = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_E = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_4 = Disk.init_disk(Disk.WRAPPED, 4)
    wrapped_disk_value_4_B = Disk.init_disk(Disk.WRAPPED, 4)
    wrapped_disk_value_5 = Disk.init_disk(Disk.WRAPPED, 5)

    visible_disk_value_1 = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_1_B = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_2 = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_2_B = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_3 = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_B = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_C = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_D = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_4 = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_4_B = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_4_C = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_5 = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_B = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_C = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_D = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_E = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_F = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_G = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_6 = Disk.init_disk(Disk.VISIBLE, 6)
    visible_disk_value_6_B = Disk.init_disk(Disk.VISIBLE, 6)

    cracked_disk_value_1 = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_1_B = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_2 = Disk.init_disk(Disk.CRACKED, 2)
    cracked_disk_value_2_B = Disk.init_disk(Disk.CRACKED, 2)
    cracked_disk_value_3 = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_3_B = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_4 = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_4_B = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_4_C = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_5 = Disk.init_disk(Disk.CRACKED, 5)

    test_board_4 = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (cracked_disk_value_2, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_4_alias = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (cracked_disk_value_2, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_6 = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             (wrapped_disk_value_3_B, visible_disk_value_4),
             (visible_disk_value_5, visible_disk_value_4_B, visible_disk_value_1),
             (visible_disk_value_1_B, cracked_disk_value_1, visible_disk_value_6,
              wrapped_disk_value_3_C, cracked_disk_value_1_B),
             (),
             (wrapped_disk_value_3_D, visible_disk_value_3)))

    test_board_6_alias = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             (wrapped_disk_value_3_B, visible_disk_value_4),
             (visible_disk_value_5, visible_disk_value_4_B, visible_disk_value_1),
             (visible_disk_value_1_B, cracked_disk_value_1, visible_disk_value_6,
              wrapped_disk_value_3_C, cracked_disk_value_1_B),
             (),
             (wrapped_disk_value_3_D, visible_disk_value_3)))



# Auxiliary functions
def are_identical_boards(board1, board2):
    """
        Check whether the given boards are identical.
        - The given boards must have the same dimension, and they must reference
          the same disk at each position.
        ASSUMPTIONS
        - Both given boards are proper boards.
    """
    assert Board.is_proper_board(board1)
    assert Board.is_proper_board(board2)
    if Board.dimension(board1) != Board.dimension(board2):
        return False
    position = (1, 1)
    while position is not None:
        if Board.get_disk_at(board1, position) is not Board.get_disk_at(board2, position):
            return False
        position = Position.next(Board.dimension(board1), position)
    return True

def are_equal_boards(board1, board2):
    """
        Check whether the given boards are equal.
        - The given boards must have the same dimension, and they must have
          identical disks at each position.
        ASSUMPTIONS
        - Both given boards are proper boards.
    """
    assert Board.is_proper_board(board1)
    assert Board.is_proper_board(board2)
    if Board.dimension(board1) != Board.dimension(board2):
        return False
    position = (1, 1)
    while position is not None:
        if Board.get_disk_at(board1, position) != Board.get_disk_at(board2, position):
            return False
        position = Position.next(Board.dimension(board1), position)
    return True



def test_Drop_Disk_At__NoExplosions(score, max_score):
    """Function drop_disk_at: no explosions, no cracking disks."""
    max_score.value += 5
    try:
        set_up()
        disk_to_drop = Disk.init_disk(Disk.WRAPPED, 4)
        assert Drop7.drop_disk_at(test_board_6, disk_to_drop, 2) == 0
        assert Board.get_disk_at(test_board_6, (2, 3)) is disk_to_drop
        assert Board.get_disk_at(test_board_6, (2, 2)) is visible_disk_value_4
        assert Board.get_disk_at(test_board_6, (3, 3)) is visible_disk_value_1
        score.value += 5
    except:
        pass

def test_Drop_Disk_At__ExplodingDisk_NoCrackingDisksBecomingVisible(score, max_score):
    """Function drop_disk_at: dropped disk exploding, no cracked disks becoming visible."""
    max_score.value += 5
    try:
        set_up()
        disk_to_drop = Disk.init_disk(Disk.VISIBLE, 6)
        assert Drop7.drop_disk_at(test_board_6, disk_to_drop, 5) == 2
        assert not Board.has_disk_at(test_board_6, (5, 1))
        assert Board.get_disk_at(test_board_6, (4, 1)) is visible_disk_value_1_B
        assert Board.get_disk_at(test_board_6, (6, 1)) is wrapped_disk_value_3_D
        assert Disk.get_state(wrapped_disk_value_3_D) == Disk.CRACKED
        score.value += 5
    except:
        pass

def test_Drop_Disk_At__OtherDiskExploding_NoCrackedDisksBecomingVisible(score, max_score):
    """Function drop_disk_at: other disk exploding, no cracked disks becoming visible."""
    max_score.value += 10
    try:
        set_up()
        Board.set_disk_at(test_board_6, (4, 2), wrapped_disk_value_1)
        disk_to_drop = Disk.init_disk(Disk.WRAPPED, 6)
        assert Drop7.drop_disk_at(test_board_6, disk_to_drop, 3) == 2
        assert not Board.has_disk_at(test_board_6, (3, 4))
        assert Board.get_disk_at(test_board_6, (3, 1)) is visible_disk_value_5
        assert Board.get_disk_at(test_board_6, (3, 2)) is visible_disk_value_1
        assert Board.get_disk_at(test_board_6, (3, 3)) == disk_to_drop
        assert Board.get_disk_at(test_board_6, (2, 2)) == visible_disk_value_4
        assert Board.get_disk_at(test_board_6, (4, 2)) is wrapped_disk_value_1
        assert Disk.get_state(wrapped_disk_value_1) == Disk.CRACKED
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__OtherDiskExploding_SomeDisksBecomingVisible_NotCausingExplosions(score, max_score):
    """Function drop_disk_at: other disk exploding, some cracked disks becoming visible without causing other explosions."""
    max_score.value += 10
    try:
        set_up()
        disk_to_drop = Disk.init_disk(Disk.WRAPPED, 3)
        assert Drop7.drop_disk_at(test_board_6, disk_to_drop, 4) == 2
        assert not Board.has_disk_at(test_board_6, (4, 6))
        assert Board.get_disk_at(test_board_6, (4, 2)) is cracked_disk_value_1
        assert Disk.get_state(cracked_disk_value_1) == Disk.VISIBLE
        assert Board.get_disk_at(test_board_6, (4, 3)) is wrapped_disk_value_3_C
        assert Disk.get_state(wrapped_disk_value_3_C) == Disk.CRACKED
        assert Board.get_disk_at(test_board_6, (4, 4)) is cracked_disk_value_1_B
        assert Board.get_disk_at(test_board_6, (4, 5)) is disk_to_drop
        assert Board.get_disk_at(test_board_6, (3, 3)) == visible_disk_value_1
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__OtherDiskExploding_SomeDisksBecomingVisible_CausingAnotherExplosion(score, max_score):
    """Function drop_disk_at: disk exploding, some cracked disks becoming visible causing a single additional explosion."""
    max_score.value += 10
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_3_B, wrapped_disk_value_4),
                 (wrapped_disk_value_5, visible_disk_value_4, cracked_disk_value_2),
                 (visible_disk_value_1, cracked_disk_value_1, visible_disk_value_5,
                  cracked_disk_value_3,),
                 (),
                 (wrapped_disk_value_3_C, visible_disk_value_3)))
        disk_to_drop = Disk.init_disk(Disk.WRAPPED, 3)
        assert Drop7.drop_disk_at(board, disk_to_drop, 4) == 6
        assert not Board.has_disk_at(board, (4, 5))
        assert Board.get_disk_at(board, (4, 2)) is cracked_disk_value_1
        assert Disk.get_state(cracked_disk_value_1) == Disk.VISIBLE
        assert Board.get_disk_at(board, (4, 3)) == cracked_disk_value_3
        assert Disk.get_state(cracked_disk_value_3) == Disk.VISIBLE
        assert Board.get_disk_at(board, (4, 4)) == disk_to_drop
        assert not Board.has_disk_at(board, (3, 3))
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__SeveralExplodingDisks_SameColumn(score, max_score):
    """Function drop_disk_at: several exploding disks in the same column."""
    max_score.value += 10
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_3_B, wrapped_disk_value_4),
                 (wrapped_disk_value_5, visible_disk_value_4, cracked_disk_value_4),
                 (visible_disk_value_5, cracked_disk_value_3, visible_disk_value_5_B, cracked_disk_value_3_B),
                 (),
                 (wrapped_disk_value_3_C, visible_disk_value_3)))
        disk_to_drop = Disk.init_disk(Disk.WRAPPED, 3)
        assert Drop7.drop_disk_at(board, disk_to_drop, 4) == 12
        assert not Board.has_disk_at(board, (4, 5))
        assert not Board.has_disk_at(board, (4, 4))
        assert not Board.has_disk_at(board, (4, 3))
        assert not Board.has_disk_at(board, (4, 2))
        assert Board.get_disk_at(board, (4, 1)) is disk_to_drop
        assert Disk.get_state(disk_to_drop) == Disk.CRACKED
        assert Board.get_disk_at(board, (3, 3)) is cracked_disk_value_4
        assert Disk.get_state(cracked_disk_value_4) == Disk.VISIBLE
        assert Board.get_disk_at(board, (3, 2)) is visible_disk_value_4
        assert Board.get_disk_at(board, (3, 1)) is wrapped_disk_value_5
        assert Disk.get_state(wrapped_disk_value_5) == Disk.VISIBLE
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__SeveralExplodingDisks_DifferentColumns_NotCausingOtherExplosions(score, max_score):
    """Function drop_disk_at: several exploding disks in different columns not causing other explosions."""
    max_score.value += 10
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_5, wrapped_disk_value_4, visible_disk_value_3, wrapped_disk_value_4_B),
                 (visible_disk_value_3_B, wrapped_disk_value_1),
                 (visible_disk_value_2, visible_disk_value_5, visible_disk_value_3_C, cracked_disk_value_5),
                 (),
                 (wrapped_disk_value_3_B, visible_disk_value_3_D)))
        disk_to_drop = Disk.init_disk(Disk.VISIBLE, 3)
        assert Drop7.drop_disk_at(board, disk_to_drop, 3) == 8
        assert not Board.has_disk_at(board, (3, 3))
        assert not Board.has_disk_at(board, (3, 2))
        assert Board.get_disk_at(board, (3, 1)) is wrapped_disk_value_1
        assert Disk.get_state(wrapped_disk_value_1) == Disk.CRACKED
        assert not Board.has_disk_at(board, (4, 4))
        assert Board.get_disk_at(board, (4, 3)) is cracked_disk_value_5
        assert Disk.get_state(cracked_disk_value_5) == Disk.VISIBLE
        assert Board.get_disk_at(board, (4, 2)) is visible_disk_value_5
        assert not Board.has_disk_at(board, (2, 4))
        assert Board.get_disk_at(board, (2, 3)) is wrapped_disk_value_4_B
        assert Disk.get_state(wrapped_disk_value_4_B) == Disk.CRACKED
        assert Board.get_disk_at(board, (2, 2)) is wrapped_disk_value_4
        assert Disk.get_state(wrapped_disk_value_4) == Disk.CRACKED
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__SeveralExplodingDisks_WrappedDiskAdjacentSeveralExplodingDisks(score, max_score):
    """Function drop_disk_at: Wrapped disk adjacent to several exploding disks."""
    max_score.value += 10
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_5, wrapped_disk_value_4, cracked_disk_value_1, wrapped_disk_value_4_B),
                 (wrapped_disk_value_3_B, cracked_disk_value_2),
                 (visible_disk_value_2, visible_disk_value_5, visible_disk_value_3, cracked_disk_value_5),
                 (),
                 (wrapped_disk_value_3_C, visible_disk_value_3_B)))
        disk_to_drop = Disk.init_disk(Disk.VISIBLE, 3)
        assert Drop7.drop_disk_at(board, disk_to_drop, 3) == 12
        assert not Board.has_disk_at(board, (4, 4))
        assert Board.get_disk_at(board, (4, 3)) is cracked_disk_value_5
        assert Disk.get_state(cracked_disk_value_5) == Disk.VISIBLE
        assert Board.get_disk_at(board, (4, 2)) is visible_disk_value_5
        assert not Board.has_disk_at(board, (3, 3))
        assert not Board.has_disk_at(board, (3, 2))
        assert Board.get_disk_at(board, (3, 1)) is wrapped_disk_value_3_B
        assert Disk.get_state(wrapped_disk_value_3_B) == Disk.CRACKED
        assert not Board.has_disk_at(board, (2, 4))
        assert Board.get_disk_at(board, (2, 3)) is wrapped_disk_value_4_B
        assert Disk.get_state(wrapped_disk_value_4_B) == Disk.CRACKED
        assert Board.get_disk_at(board, (2, 2)) is wrapped_disk_value_4
        assert Disk.get_state(wrapped_disk_value_4) == Disk.CRACKED
        score.value += 10
    except:
        pass

def test_Drop_Disk_At__SuccessiveExposions(score, max_score):
    """Function drop_disk_at: Successive explosions."""
    max_score.value += 40
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_5, cracked_disk_value_4, cracked_disk_value_1, wrapped_disk_value_4),
                 (cracked_disk_value_4_B, cracked_disk_value_3),
                 (cracked_disk_value_4_C, visible_disk_value_5, visible_disk_value_3, cracked_disk_value_5),
                 (),
                 (wrapped_disk_value_3_B, visible_disk_value_3_B)))
        disk_to_drop = Disk.init_disk(Disk.VISIBLE, 4)
        assert Drop7.drop_disk_at(board, disk_to_drop, 4) == 2 + 4 * 4 + 2 * 8 + 1 * 16
        assert not Board.has_disk_at(board, (4, 2))
        assert Board.get_disk_at(board, (4, 1)) is cracked_disk_value_5
        assert Disk.get_state(cracked_disk_value_5) == Disk.VISIBLE
        assert not Board.has_disk_at(board, (3, 1))
        assert not Board.has_disk_at(board, (2, 3))
        assert Board.get_disk_at(board, (2, 2)) is wrapped_disk_value_4
        assert Disk.get_state(wrapped_disk_value_4) == Disk.CRACKED
        assert Board.get_disk_at(board, (2, 1)) is wrapped_disk_value_5
        assert Disk.get_state(wrapped_disk_value_5) == Disk.VISIBLE
        score.value += 40
    except:
        pass

def test_Drop_Disk_At_NoDisk(score, max_score):
    """Function drop_disk_at: No disk."""
    max_score.value += 20
    try:
        set_up()
        the_board = Board.init_board(
            dimension=6, given_disks=
            ( (wrapped_disk_value_1,),
              (cracked_disk_value_2,cracked_disk_value_2_B),
              (visible_disk_value_4,),
              (visible_disk_value_4_B,),
              (cracked_disk_value_5,visible_disk_value_2))
        )
        assert Drop7.drop_disk_at(the_board) == 1*2 + 1*4 + 2*8 + 1*16 + 1*32 + 1*64
        for col in range(1,5):
            assert not Board.has_disk_at(the_board,(col,1))
        score.value += 20
    except:
        pass



def test_Best_Column_For_Disk_EmptyBoard(score, max_score):
    """Function best_column_for_disk: empty board."""
    max_score.value += 4
    try:
        set_up()
        board = Board.init_board(dimension=6)
        best_column,highest_score = Drop7.best_drop_for_disk(board, visible_disk_value_5)
        assert (best_column,highest_score) == (6,0)
        assert Board.get_disk_at(board,(6,1)) is visible_disk_value_5
        score.value += 4
    except:
        pass

def test_Best_Columns_For_Disk_SingleColumn(score, max_score):
    """Function best_columns_for_disk: single column"""
    max_score.value += 8
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((wrapped_disk_value_3,),
                 (wrapped_disk_value_5, cracked_disk_value_2, cracked_disk_value_1, wrapped_disk_value_4),
                 (wrapped_disk_value_4_B, cracked_disk_value_3),
                 (cracked_disk_value_4, visible_disk_value_5, visible_disk_value_3, cracked_disk_value_5),
                 (),
                 (wrapped_disk_value_3_B, visible_disk_value_3_B)))
        board_copy = Board.get_board_copy(board)
        best_column, highest_score = Drop7.best_drop_for_disk(board, visible_disk_value_5_B)
        assert (best_column,highest_score) == (4, 16)
        actual_score = Drop7.play(board_copy,[visible_disk_value_5_B],[best_column])
        assert actual_score == highest_score
        assert are_equal_boards(board,board_copy)
        score.value += 8
    except:
        pass

def test_Best_Column_For_Disk_SeveralColumns(score, max_score):
    """Function best_columns_for_disk: several columns"""
    max_score.value += 10
    try:
        set_up()
        board = Board.init_board \
            (dimension=6, given_disks= \
                ((cracked_disk_value_4,),
                 (cracked_disk_value_4_B, visible_disk_value_5, cracked_disk_value_1, wrapped_disk_value_4),
                 (wrapped_disk_value_4_B, cracked_disk_value_4_C),
                 (visible_disk_value_5_B, wrapped_disk_value_5, visible_disk_value_5_C, visible_disk_value_5_D),
                 (),
                 (cracked_disk_value_1_B, visible_disk_value_5_E, visible_disk_value_5_F, visible_disk_value_5_G) ))
        board_copy = Board.get_board_copy(board)
        best_column, highest_score = Drop7.best_drop_for_disk(board, visible_disk_value_2)
        assert (best_column,highest_score) == (6,14)
        actual_score = Drop7.play(board_copy,[visible_disk_value_2],[best_column])
        assert actual_score == highest_score
        assert are_equal_boards(board,board_copy)
        score.value += 10
    except:
        pass



def test_Highest_Greedy_Score__NoDisks(score, max_score):
    """Function highest_greedy_score: No disks."""
    max_score.value += 3
    try:
        set_up()
        test_board_4_copy = Board.get_board_copy(test_board_4)
        highest_score, columns = Drop7.highest_greedy_score(test_board_4, [])
        assert highest_score == 0
        assert len(columns) == 0
        assert are_identical_boards(test_board_4, test_board_4_alias)
        assert are_equal_boards(test_board_4, test_board_4_copy)
        score.value += 3
    except:
        pass

def test_Highest_Greedy_Score__Single_Placable_Disk(score, max_score):
    """Function highest_greedy_score: Single disk."""
    max_score.value += 6
    try:
        set_up()
        test_board_6_copy = Board.get_board_copy(test_board_6)
        disks_to_drop = [visible_disk_value_2_B]
        disks_to_drop_copy = list.copy(disks_to_drop)
        highest_score, columns = \
            Drop7.highest_greedy_score(test_board_6, disks_to_drop)
        assert highest_score == 6
        assert columns == (6,)
        assert len(disks_to_drop) == 0
        actual_score = Drop7.play(test_board_6_copy, disks_to_drop_copy, columns)
        assert actual_score == highest_score
        assert are_equal_boards(test_board_6,test_board_6_copy)
        score.value += 6
    except:
        pass

def test_Highest_Greedy_Score__Several_Placable_Disks(score, max_score):
    """Function highest_greedy_score: Several disks that can all be dropped."""
    max_score.value += 14
    try:
        set_up()
        test_board_6_copy = Board.get_board_copy(test_board_6)
        disks_to_drop = [visible_disk_value_4_C,visible_disk_value_5_B,visible_disk_value_3_C]
        disks_to_drop_copy = list.copy(disks_to_drop)
        highest_score, columns = \
            Drop7.highest_greedy_score(test_board_6, disks_to_drop)
        assert highest_score == 40
        assert columns == (1,4,6)
        assert len(disks_to_drop) == 0
        actual_score = Drop7.play(test_board_6_copy, disks_to_drop_copy, columns)
        assert actual_score == highest_score
        assert are_equal_boards(test_board_6,test_board_6_copy)
        score.value += 14
    except:
        pass

def test_Highest_Greedy_Score__Several_Disks_Not_All_Placable(score, max_score):
    """Function highest_greedy_score: Several disks that can not all be dropped."""
    max_score.value += 14
    try:
        set_up()
        test_board = Board.init_board(2,
                ( (cracked_disk_value_2, wrapped_disk_value_1),
                  (wrapped_disk_value_2_B,) ) )
        test_board_copy = Board.get_board_copy(test_board)
        disks_to_drop = [visible_disk_value_2,visible_disk_value_2_B,
                         wrapped_disk_value_2_C, wrapped_disk_value_2_D,
                         wrapped_disk_value_2_E, wrapped_disk_value_1_B,
                         wrapped_disk_value_1_C, wrapped_disk_value_1_D]
        disks_to_drop_copy = list.copy(disks_to_drop)
        for i in range(0,len(disks_to_drop_copy)):
            disks_to_drop_copy[i] = Disk.get_disk_copy(disks_to_drop_copy[i])
        highest_score, columns = \
            Drop7.highest_greedy_score(test_board, disks_to_drop)
        assert highest_score == 14
        assert columns == (2,2,2,2,1,1)
        assert disks_to_drop == disks_to_drop_copy[6:]
        actual_score = Drop7.play(test_board_copy, disks_to_drop_copy[:6], columns)
        assert actual_score == highest_score
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 14
    except:
        pass
# Greedy algorithm: one disk, several disks, not all disks can be placed.



def test_Highest_Score__NoDisks(score, max_score):
    """Function highest_score: No disks."""
    max_score.value += 3
    try:
        set_up()
        test_board_4_copy = Board.get_board_copy(test_board_4)
        highest_score, columns = Drop7.highest_score(test_board_4, [])
        assert highest_score == 0
        assert len(columns) == 0
        assert are_identical_boards(test_board_4, test_board_4_alias)
        assert are_equal_boards(test_board_4, test_board_4_copy)
        score.value += 3
    except:
        pass

def test_Highest_Score__Single_Disk_No_Explosions(score, max_score):
    """Function highest_score: Single disk, no explosions."""
    max_score.value += 4
    try:
        set_up()
        test_board_4_copy = Board.get_board_copy(test_board_4)
        highest_score, columns = Drop7.highest_score(test_board_4, [visible_disk_value_4])
        assert highest_score == 0
        assert columns == [1]
        assert are_identical_boards(test_board_4, test_board_4_alias)
        assert are_equal_boards(test_board_4, test_board_4_copy)
        score.value += 4
    except:
        pass

def test_Highest_Score__Single_Exploding_Disk_Several_Columns(score, max_score):
    """Function highest_score: Single exploding disk, with same high score in several columns."""
    max_score.value += 5
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=4, given_disks= \
                ([wrapped_disk_value_3, ],
                 [],
                 [wrapped_disk_value_2, ],
                 [visible_disk_value_4, wrapped_disk_value_3_B]))
        test_board_alias = Board.init_board \
            (dimension=4, given_disks= \
                ((wrapped_disk_value_3,),
                 [],
                 (wrapped_disk_value_2,),
                 [visible_disk_value_4, wrapped_disk_value_3_B]))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = Drop7.highest_score(test_board, [visible_disk_value_2])
        assert highest_score == 2
        assert columns == [1]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 5
    except:
        pass

def test_Highest_Score__Single_Disk_Several_Explosions(score, max_score):
    """Function highest_score: Single exploding disk, with same high score in several columns."""
    max_score.value += 10
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=4, given_disks= \
                ([cracked_disk_value_2, ],
                 [wrapped_disk_value_1, wrapped_disk_value_4],
                 [wrapped_disk_value_3, cracked_disk_value_4, wrapped_disk_value_2, visible_disk_value_2],
                 [cracked_disk_value_1]))
        test_board_alias = Board.init_board \
            (dimension=4, given_disks= \
                ([cracked_disk_value_2, ],
                 [wrapped_disk_value_1, wrapped_disk_value_4],
                 [wrapped_disk_value_3, cracked_disk_value_4, wrapped_disk_value_2, visible_disk_value_2],
                 [cracked_disk_value_1]))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = Drop7.highest_score(test_board, [visible_disk_value_2_B])
        assert highest_score == 10
        assert columns == [4]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 10
    except:
        pass

def test_Highest_Score__Two_Disks_Exploding_At_Each_Drop(score, max_score):
    """Function highest_score: Two disks, highest score when exploding at each drop."""
    max_score.value += 12
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=4, given_disks= \
                ([cracked_disk_value_1, ],
                 [],
                 [cracked_disk_value_2, wrapped_disk_value_4],
                 []))
        test_board_alias = Board.init_board \
            (dimension=4, given_disks= \
                ([cracked_disk_value_1, ],
                 [],
                 [cracked_disk_value_2, wrapped_disk_value_4],
                 []))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = Drop7.highest_score(test_board, [visible_disk_value_3, visible_disk_value_3_B])
        assert highest_score == 12
        assert columns == [3, 2]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 12
    except:
        pass

def test_Highest_Score__Two_Disks_Exploding_At_Last_Drop(score, max_score):
    """Function highest_score: Two disks, highest score when exploding at last drop."""
    max_score.value += 12
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=4, given_disks= \
                ([wrapped_disk_value_1, ],
                 [wrapped_disk_value_4, cracked_disk_value_2, cracked_disk_value_3],
                 [cracked_disk_value_3_B],
                 [wrapped_disk_value_4_B]))
        test_board_alias = Board.init_board \
            (dimension=4, given_disks= \
                ([wrapped_disk_value_1, ],
                 [wrapped_disk_value_4, cracked_disk_value_2, cracked_disk_value_3],
                 [cracked_disk_value_3_B],
                 [wrapped_disk_value_4_B]))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = Drop7.highest_score(test_board, [wrapped_disk_value_3_B, visible_disk_value_3])
        assert highest_score == 14
        assert columns == [1, 1]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 12
    except:
        pass

def test_Highest_Score__Too_Many_Disks(score, max_score):
    """Function highest_score: Too many disks."""
    max_score.value += 6
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=2, given_disks= \
                ([cracked_disk_value_1, ],
                 [cracked_disk_value_1_B, ]))
        test_board_alias = Board.init_board \
            (dimension=2, given_disks= \
                ([cracked_disk_value_1, ],
                 [cracked_disk_value_1_B, ]))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = \
            Drop7.highest_score(test_board, [wrapped_disk_value_1, wrapped_disk_value_2, visible_disk_value_1])
        assert highest_score is None
        assert columns is None
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 6
    except:
        pass

def test_Highest_Score__Several_Disks_Case_1(score, max_score):
    """Function highest_score: Several disks, case 1."""
    # This test takes quite some time.
    max_score.value += 25
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=6, given_disks= \
                ([cracked_disk_value_1, wrapped_disk_value_2],
                 [visible_disk_value_3, wrapped_disk_value_4, cracked_disk_value_2, visible_disk_value_2],
                 [],
                 [wrapped_disk_value_2_B, visible_disk_value_3_B],
                 [wrapped_disk_value_5, wrapped_disk_value_4_B, wrapped_disk_value_3_C, wrapped_disk_value_3_D,
                  wrapped_disk_value_3_B, cracked_disk_value_5],
                 [visible_disk_value_4]))
        test_board_alias = Board.init_board \
            (dimension=6, given_disks= \
                ([cracked_disk_value_1, wrapped_disk_value_2],
                 [visible_disk_value_3, wrapped_disk_value_4, cracked_disk_value_2, visible_disk_value_2],
                 [],
                 [wrapped_disk_value_2_B, visible_disk_value_3_B],
                 [wrapped_disk_value_5, wrapped_disk_value_4_B, wrapped_disk_value_3_C, wrapped_disk_value_3_D,
                  wrapped_disk_value_3_B, cracked_disk_value_5],
                 [visible_disk_value_4]))
        test_board_copy = Board.get_board_copy(test_board)

        highest_score, columns = Drop7.highest_score(test_board,
                                                     [visible_disk_value_1, visible_disk_value_3_C,
                                                      wrapped_disk_value_3_E,
                                               visible_disk_value_4_B])
        assert highest_score == 264
        assert columns == [1, 2, 1, 4]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 25
    except:
        pass

def test_Highest_Score__Several_Disks_Case_2(score, max_score):
    """Function highest_score: Several disks, case 2."""
    # This test takes quite some time.
    max_score.value += 40
    try:
        set_up()
        test_board = Board.init_board \
            (dimension=6, given_disks= \
                ([cracked_disk_value_1, cracked_disk_value_2, cracked_disk_value_3,
                  cracked_disk_value_4, cracked_disk_value_5],
                 [visible_disk_value_3, wrapped_disk_value_4, cracked_disk_value_2_B,
                  visible_disk_value_5],
                 [],
                 [wrapped_disk_value_2_B, visible_disk_value_1],
                 [visible_disk_value_6, visible_disk_value_4, visible_disk_value_3_C,
                  visible_disk_value_2, visible_disk_value_2_B],
                 [visible_disk_value_4_B, cracked_disk_value_4_C, wrapped_disk_value_3]))
        test_board_alias = Board.init_board \
            (dimension=6, given_disks= \
                ([cracked_disk_value_1, cracked_disk_value_2, cracked_disk_value_3,
                  cracked_disk_value_4, cracked_disk_value_5],
                 [visible_disk_value_3, wrapped_disk_value_4, cracked_disk_value_2_B,
                  visible_disk_value_5],
                 [],
                 [wrapped_disk_value_2_B, visible_disk_value_1],
                 [visible_disk_value_6, visible_disk_value_4, visible_disk_value_3_C,
                  visible_disk_value_2, visible_disk_value_2_B],
                 [visible_disk_value_4_B, cracked_disk_value_4_C, wrapped_disk_value_3]))
        test_board_copy = Board.get_board_copy(test_board)
        highest_score, columns = Drop7.highest_score(test_board,
                    [wrapped_disk_value_3_B, visible_disk_value_6_B,
                     visible_disk_value_5_B, wrapped_disk_value_4_B])
        assert highest_score == 1164
        assert columns == [6,5,3,2]
        assert are_identical_boards(test_board, test_board_alias)
        assert are_equal_boards(test_board,test_board_copy)
        score.value += 40
    except:
        pass






Drop7_test_functions = \
    {
        test_Drop_Disk_At__NoExplosions,
        test_Drop_Disk_At__ExplodingDisk_NoCrackingDisksBecomingVisible,
        test_Drop_Disk_At__OtherDiskExploding_NoCrackedDisksBecomingVisible,
        test_Drop_Disk_At__OtherDiskExploding_SomeDisksBecomingVisible_NotCausingExplosions,
        test_Drop_Disk_At__OtherDiskExploding_SomeDisksBecomingVisible_CausingAnotherExplosion,
        test_Drop_Disk_At__SeveralExplodingDisks_SameColumn,
        test_Drop_Disk_At__SeveralExplodingDisks_DifferentColumns_NotCausingOtherExplosions,
        test_Drop_Disk_At__SeveralExplodingDisks_WrappedDiskAdjacentSeveralExplodingDisks,
        test_Drop_Disk_At__SuccessiveExposions,
        test_Drop_Disk_At_NoDisk,

        test_Best_Column_For_Disk_EmptyBoard,
        test_Best_Columns_For_Disk_SingleColumn,
        test_Best_Column_For_Disk_SeveralColumns,

        test_Highest_Greedy_Score__NoDisks,
        test_Highest_Greedy_Score__Single_Placable_Disk,
        test_Highest_Greedy_Score__Several_Placable_Disks,
        test_Highest_Greedy_Score__Several_Disks_Not_All_Placable,

        test_Highest_Score__NoDisks,
        test_Highest_Score__Single_Disk_No_Explosions,
        test_Highest_Score__Single_Exploding_Disk_Several_Columns,
        test_Highest_Score__Single_Disk_Several_Explosions,
        test_Highest_Score__Two_Disks_Exploding_At_Each_Drop,
        test_Highest_Score__Two_Disks_Exploding_At_Last_Drop,
        test_Highest_Score__Too_Many_Disks,
        test_Highest_Score__Several_Disks_Case_1,
        test_Highest_Score__Several_Disks_Case_2
    }
