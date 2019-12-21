import Drop7.Position as Position


def test_Is_Proper_Position__Legal_Case(score, max_score):
    """Function is_proper_position: given position is proper position."""
    max_score.value += 1
    try:
        assert Position.is_proper_position(4, (1, 1))
        assert Position.is_proper_position(4, (4, 4))
        assert Position.is_proper_position(4, (2, 3))
        assert Position.is_proper_position(4, (4, 5)) # Overflow position
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Not_Tuple(score, max_score):
    """Function is_proper_position: given position is not a tuple."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position(4, [1, 2])
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_Length(score, max_score):
    """Function is_proper_position: given position is a tuple of length different from 2."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position(4, (1,))
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_Column(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with improper column."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position(4, (0, 3))
        assert not Position.is_proper_position(4, (5, 3))
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_Row(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with improper row."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position(4, (3, 0))
        assert not Position.is_proper_position(4, (3, 6))
        score.value += 1
    except:
        pass



def test_Is_Overflow_Position__Single_Case(score, max_score):
    """Function is_overflow_position: single case."""
    max_score.value += 1
    try:
        assert not Position.is_overflow_position(4, (1, 1))
        assert not Position.is_overflow_position(4, (4, 4))
        assert Position.is_overflow_position(4, (4, 5))
        score.value += 1
    except:
        pass



def test_Left__Not_Leftmost_Position(score, max_score):
    """Function left: non-leftmost position"""
    max_score.value += 1
    try:
        assert Position.left(8, (2, 4)) == (1, 4)
        score.value += 1
    except:
        pass

def test_Left__Leftmost_Position(score, max_score):
    """Function up: leftmost position"""
    max_score.value += 1
    try:
        assert Position.left(8, (1, 6)) == None
        score.value += 1
    except:
        pass



def test_Right__Not_Rightmost_Position(score, max_score):
    """Function right: non-rightmost position"""
    max_score.value += 1
    try:
        assert Position.right(8, (2, 4)) == (3, 4)
        score.value += 1
    except:
        pass

def test_Right__Rightmost_Position(score, max_score):
    """Function right: rightmost position"""
    max_score.value += 1
    try:
        assert Position.right(8, (8, 6)) == None
        score.value += 1
    except:
        pass



def test_Up__Not_Upmost_Position(score, max_score):
    """Function up: non-upmost position"""
    max_score.value += 1
    try:
        assert Position.up(8, (2, 3)) == (2, 4)
        score.value += 1
    except:
        pass

def test_Up__Upmost_Position(score, max_score):
    """Function up: upmost position"""
    max_score.value += 1
    try:
        assert Position.up(8, (2, 8)) == (2,9)
        score.value += 1
    except:
        pass

def test_Up__Overflow_Position(score, max_score):
    """Function up: overflow position"""
    max_score.value += 1
    try:
        assert Position.up(8, (2, 9)) == None
        score.value += 1
    except:
        pass



def test_Down__Not_Bottom_Position(score, max_score):
    """Function down: not bottom position"""
    max_score.value += 1
    try:
        assert Position.down(8, (2, 5)) == (2, 4)
        score.value += 1
    except:
        pass

def test_Down__Bottom_Position(score, max_score):
    """Function down: bottom position"""
    max_score.value += 1
    try:
        assert Position.down(8, (2, 1)) == None
        score.value += 1
    except:
        pass



def test_Next_Not_End_Row(score, max_score):
    """Function next: position not at end of row"""
    max_score.value += 1
    try:
        assert Position.next(4, (3, 1)) == (4, 1)
        assert Position.next(4, (2, 4)) == (3, 4)
        score.value += 1
    except:
        pass

def test_Next_End_Non_Top_Row(score, max_score):
    """Function next: position at end of row that is not top row"""
    max_score.value += 1
    try:
        assert Position.next(4, (4, 2)) == (1, 3)
        score.value += 1
    except:
        pass

def test_Next_End_Top_Row(score, max_score):
    """Function next: position at end of top row"""
    max_score.value += 1
    try:
        assert Position.next(4, (4, 5)) == None
        score.value += 1
    except:
        pass



def test_Get_All_Adjacent_Positions__Empty_Collection(score, max_score):
    """Function get_all_adjacent_positions: empty collection."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, []) == set()
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Bottom_Left_Position(score, max_score):
    """Function get_all_adjacent_positions: bottom left position."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, [(1, 1)]) == set([(1, 2), (2, 1)])
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Bottom_Right_Position(score, max_score):
    """Function get_all_adjacent_positions: bottom right position."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, [(6, 1)]) == set([(6, 2), (5, 1)])
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Top_Left_Position(score, max_score):
    """Function get_all_adjacent_positions: top left position."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, [(1, 7)]) == set([(1, 6), (2, 7)])
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Top_Right_Position(score, max_score):
    """Function get_all_adjacent_positions: top right position."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, [(6, 7)]) == set([(6, 6), (5, 7)])
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Arbitrary_Position(score, max_score):
    """Function get_all_adjacent_positions: arbitrary position."""
    max_score.value += 1
    try:
        assert Position.get_all_adjacent_positions(6, [(2, 4)]) == set([(2, 3), (2, 5), (1, 4), (3, 4)])
        score.value += 1
    except:
        pass

def test_Get_All_Adjacent_Positions__Collection_of_Positions(score, max_score):
    """Function get_all_adjacent_positions: collection of positions."""
    max_score.value += 3
    try:
        assert Position.get_all_adjacent_positions(6, [(2, 4), (3, 4), (3, 5)]) == \
               set([(2, 3), (2, 5), (1, 4), (3, 4), (3, 3), (3, 5), (2, 4), (4, 4), (3, 4), (3, 6), (2, 5), (4, 5)])
        score.value += 3
    except:
        pass



position_test_functions = \
    {
        test_Is_Proper_Position__Not_Tuple,
        test_Is_Proper_Position__Improper_Length,
        test_Is_Proper_Position__Improper_Column,
        test_Is_Proper_Position__Improper_Row,
        test_Is_Proper_Position__Legal_Case,
        test_Is_Overflow_Position__Single_Case,
        test_Left__Not_Leftmost_Position,
        test_Left__Leftmost_Position,
        test_Right__Not_Rightmost_Position,
        test_Right__Rightmost_Position,
        test_Up__Not_Upmost_Position,
        test_Up__Upmost_Position,
        test_Up__Overflow_Position,
        test_Down__Not_Bottom_Position,
        test_Down__Bottom_Position,
        test_Next_Not_End_Row,
        test_Next_End_Non_Top_Row,
        test_Next_End_Top_Row,
        test_Get_All_Adjacent_Positions__Empty_Collection,
        test_Get_All_Adjacent_Positions__Bottom_Left_Position,
        test_Get_All_Adjacent_Positions__Bottom_Right_Position,
        test_Get_All_Adjacent_Positions__Top_Left_Position,
        test_Get_All_Adjacent_Positions__Top_Right_Position,
        test_Get_All_Adjacent_Positions__Arbitrary_Position,
        test_Get_All_Adjacent_Positions__Collection_of_Positions
    }



