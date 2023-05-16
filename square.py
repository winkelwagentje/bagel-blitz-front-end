from enum import Enum
import pyglet


class Colour(Enum):
    BLACK = (155, 148, 120)
    WHITE = (245, 245, 245)


class State(Enum):
    IDLE = 0
    SELECTED = 1
    MOVABLE = 2


def determine_colour(i, j):
    if (i + j) % 2 == 0:
        return Colour.BLACK
    return Colour.WHITE


class Square:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.colour = determine_colour(x, y)
        self.state = State.IDLE
        self.content = None
        self.shape_object = pyglet.shapes.Rectangle(x * board.size / 8 + board.padding, y * board.size / 8 + board.padding,
                                                board.size / 8, board.size / 8, self.colour.value,
                                                batch=board.batch)

    def set_piece(self, piece):
        self.content = piece

    def empty(self):
        self.content = None
