# import Drop7.Board as Board
import Drop7.Disk as Disk

def test_Is_Proper_Disk__Legal_Case(score, max_score):
    """Function is_proper_disk: given disk is proper disk."""
    max_score.value += 1
    try:
        assert Disk.is_proper_disk(4, Disk.init_disk(Disk.VISIBLE, 4))
        assert Disk.is_proper_disk(4, Disk.init_disk(Disk.CRACKED, 1))
        score.value += 1
    except:
        pass

def test_Is_Proper_Disk__Illegal_State(score, max_score):
    """Function is_proper_disk: illegal state."""
    max_score.value += 1
    try:
        assert not Disk.is_proper_disk(4, Disk.init_disk(("ABC",), 4))
        score.value += 1
    except:
        pass

def test_Is_Proper_Disk__Illegal_Value(score, max_score):
    """Function is_proper_disk: illegal value."""
    max_score.value += 1
    try:
        assert not Disk.is_proper_disk(4, Disk.init_disk(Disk.VISIBLE, 5))
        score.value += 1
    except:
        pass



def test_Init_Disk__Single_Case(score,max_score):
    """Function init_disk: single case."""
    max_score.value += 1
    try:
        disk = Disk.init_disk(Disk.VISIBLE,4)
        assert Disk.get_state(disk) == Disk.VISIBLE
        assert Disk.get_value(disk) == 4
        score.value += 1
    except:
        pass



def test_Get_Random_Disk__Single_Case(score,max_score):
    """Function get_random_disk: single case."""
    max_score.value += 1
    try:
        for i in range(1,1000):
            disk = Disk.get_random_disk(7,{Disk.VISIBLE,Disk.WRAPPED})
            assert Disk.get_state(disk) in {Disk.VISIBLE,Disk.WRAPPED}
            assert 1 <= Disk.get_value(disk) <= 7
        score.value += 1
    except:
        pass



def test_Set_State(score, max_score):
    """Function set_state: single case."""
    max_score.value += 1
    try:
        disk = Disk.init_disk(Disk.CRACKED,5)
        Disk.set_state(disk, Disk.VISIBLE)
        assert Disk.get_state(disk) == Disk.VISIBLE
        score.value += 1
    except:
        pass



def test_Set_Value(score, max_score):
    """Function set_value: single case."""
    max_score.value += 1
    try:
        disk = Disk.init_disk(Disk.CRACKED,5)
        Disk.set_value(disk, 8)
        assert Disk.get_value(disk) == 8
        score.value += 1
    except:
        pass



def test_Get_Disk_Copy(score, max_score):
    """Function get_disk_copy: single case."""
    max_score.value += 3
    try:
        disk = Disk.init_disk(Disk.CRACKED,5)
        copy = Disk.get_disk_copy(disk)
        assert Disk.get_state(copy) == Disk.get_state(disk)
        assert Disk.get_value(copy) == Disk.get_value(disk)
        # Checking that a new disk has been returned.
        Disk.set_value(disk,Disk.get_value(disk)+100)
        assert Disk.get_value(copy) == Disk.get_value(disk)-100
        score.value += 3
    except:
        pass



disk_test_functions = \
    {
        test_Is_Proper_Disk__Legal_Case,
        test_Is_Proper_Disk__Illegal_State,
        test_Is_Proper_Disk__Illegal_Value,
        test_Init_Disk__Single_Case,
        test_Get_Random_Disk__Single_Case,
        test_Set_State,
        test_Set_Value,
        test_Get_Disk_Copy
    }


