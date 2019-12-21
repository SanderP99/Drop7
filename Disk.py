import random

# Disks can be stored on the game board. They have a state
# and a number.
#  - Disks are mutable things. More in particular, it must be
#    possible to change the state of a disk.

# Enumeration of the possible states of a disk.
VISIBLE = 10
CRACKED = 20
WRAPPED = 30


# Disks are lists with the state on position 0 and the value on position 1.

def is_proper_disk(dimension, disk):
    """
       Check whether the given disk is a proper disk for any board with
       the given dimension.
       - The state of the given disk must be one of the values VISIBLE,
         WRAPPED, CRACKED or some additional self-defined state.
       - The value of the given disk must be a positive integer number
         that does not exceed the dimension of the given board.
       ASSUMPTIONS
       - None
    """
    if not disk[0] in (VISIBLE, CRACKED, WRAPPED):  # Check if the state is allowed
        return False

    if not isinstance(disk[1], int):  # Check if the value is an integer
        return False

    if disk[1] <= 0 or disk[1] > dimension:  # Check if the value is within the dimensions
        return False

    return True


def init_disk(state, value):
    """
       Return a new disk with given state and given value.
       ASSUMPTIONS
       - None
    """
    disk = [state, value]
    return disk


def get_random_disk(dimension, possible_states):
    """
       Return a random disk for a board with the given dimension with
       a state that belongs to the collection of possible states.
       ASSUMPTIONS
       - The given dimension is positive.
       - The given collection of possible states is not empty and contains
         only elements VISIBLE, WRAPPED and/or CRACKED
    """
    list_of_possible_states = list(possible_states)
    list_of_chances = [0.66, 0.33]  # Weights for the different states
    value = random.randint(1, dimension)  # Get a random value
    state = random.choices(range(len(list_of_possible_states)), weights=list_of_chances, k=1)
    # Get a random state from collection with weights to prevent an overuse of wrapped disks in the game

    return init_disk(list_of_possible_states[state[0]], value)


def set_state(disk, state):
    """
        Set the state of the given disk to the given state.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    disk[0] = state
    return disk


def get_state(disk):
    """
        Return the state of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    return disk[0]


def set_value(disk, value):
    """
        Set the value of the given disk to the given value.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    disk[1] = value
    return disk


def get_value(disk):
    """
        Return the value of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    return disk[1]


def get_disk_copy(disk):
    """
        Return a new disk whose state and value are identical to the
        state and value of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    copy_disk = [0, 0]

    set_state(copy_disk, get_state(disk))
    set_value(copy_disk, get_value(disk))

    return copy_disk
