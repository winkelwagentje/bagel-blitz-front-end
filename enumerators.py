from enum import Enum


class Color(Enum):
    BLACK = (150, 75, 0)
    WHITE = (245, 245, 245)
    BLACK_SELECTED = (34, 139, 34)
    WHITE_SELECTED = (144, 238, 144)


class SquareState(Enum):
    IDLE = 0
    SELECTED = 1
    MOVABLE = 2
