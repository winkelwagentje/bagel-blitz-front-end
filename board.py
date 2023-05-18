import pyglet
import math
from square import Square, State


def determine_colour(i, j):
    BLACK = (150, 75, 0)
    WHITE = (245, 245, 245)

    if (i + j) % 2 == 0:
        return BLACK
    return WHITE


def squares(size, padding, board):
    list = []
    for i in range(8):
        for j in range(8):
            list.append(Square(i, j, board))

    return list


class Board:
    def __init__(self, size, padding, batch, history=""):
        self.size = size
        self.padding = padding
        self.batch = batch
        self.board_squares = squares(size, padding, self)
        self.history = history

    def get_square_size(self):
        return self.size / 8

    def get_abs_x(self, rel_x):
        return self.padding + self.size / 8 * rel_x

    def get_abs_y(self, rel_y):
        return self.padding + self.size / 8 * rel_y

    def get_board_coordinates(self, x, y):
        rel_x = math.floor((x - self.padding) / self.get_square_size())
        rel_y = math.floor((y - self.padding) / self.get_square_size())

        if 0 <= rel_x <= 7 and 0 <= rel_y <= 7:
            return rel_x, rel_y
        return -1, -1  # an invalid position

    def get_square(self, rel_x, rel_y):
        return self.board_squares[rel_x * 8 + rel_y]

    def get_selected_square(self):
        for square in self.board_squares:
            if square.state == State.SELECTED:
                return square
        return None

    def is_selected(self):
        for square in self.board_squares:
            if square.state == State.SELECTED:
                return True
        return False

    def deselect(self):
        for square in self.board_squares:
            square.deselect()

    def update(self, layout):
        pass

    def layout(self):
        pass