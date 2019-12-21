# Positions identify individual cells on game boards.


def is_proper_position(dimension, position):
    """
        Check whether the given position is a proper position for any board
        with the given dimension.
        - The given position must be a tuple of length 2 whose elements are both
          natural numbers.
        - The first element identifies the column. It may not exceed the given
          dimension.
        - The second element identifies the row. It may not exceed the given
          dimension incremented with 1 (taking into account the overflow position)
        ASSUMPTIONS
        - None
    """
    if not isinstance(position, tuple) or len(position) != 2:
        return False

    if position[0] <= 0 or position[1] <= 0:  # Negative integer
        return False

    if position[0] > dimension or position[1] > dimension + 1:  # Greater than dimension
        return False
    return True


def is_overflow_position(dimension, position):
    """
        Check whether the given position is an overflow position for any board
        with the given dimension.
        - True if and only if the position is in the overflow row of the given board.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """
    if position[1] == dimension + 1:
        return True
    return False


def left(dimension, position):
    """
        Return the position on any board with the given dimension immediately to
        the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """
    left_pos = (position[0] - 1, position[1])
    if position[0] == 1:
        return None
    else:
        return left_pos


def right(dimension, position):
    """
       Return the position on any board with the given dimension immediately to
       the right of the given position.
       - None is returned if the generated position is outside the boundaries of
         a board with the given dimension.
       ASSUMPTIONS
       - The given position is a proper position for any board with the
         given dimension.
     """

    right_pos = (position[0] + 1, position[1])
    if position[0] == dimension:
        return None
    else:
        return right_pos


def up(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        above the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    up_pos = (position[0], position[1] + 1)
    if position[1] > dimension:
        return None
    else:
        return up_pos


def down(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        below the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    down_pos = (position[0], position[1] - 1)
    if position[1] == 1:
        return None
    else:
        return down_pos


def next(dimension, position):
    """
        Return the position on any board with the given dimension next to the
        given position.
        - If the given position is not at the end of a row, the resulting position
          is immediately to the right of the given position.
        - If the given position is at the end of a row, the resulting position is
          the leftmost position of the row above. If that next row does not exist,
          None is returned.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    row, column = position

    if column <= dimension + 1 and row < dimension:
        return right(dimension, position)
    elif column == dimension + 1 and row == dimension:
        return None
    else:
        return 1, column + 1


def get_all_adjacent_positions(dimension, positions):
    """
        Return a mutable set of all positions adjacent to at least one of the positions
        in the given collection of positions and within the boundaries of any board
        with the given dimension.
        ASSUMPTIONS
        - Each position in the given collection of positions is a proper position
          for any board with the given dimension.
    """
    adjacent_positions = set()

    for position in positions:
        set.add(adjacent_positions, left(dimension, position))
        set.add(adjacent_positions, right(dimension, position))
        set.add(adjacent_positions, up(dimension, position))
        set.add(adjacent_positions, down(dimension, position))

    set.discard(adjacent_positions, None)
    return adjacent_positions
