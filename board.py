import pyglet
import math


def determine_colour(i, j):
    BLACK = (150, 75, 0)
    WHITE = (245, 245, 245)

    if (i + j) % 2 == 0:
        return BLACK
    return WHITE


def squares(size, padding, batch):
    list = []
    for i in range(8):
        for j in range(8):
            list.append(pyglet.shapes.Rectangle(i * size / 8 + padding, j * size / 8 + padding,
                                                size / 8, size / 8, determine_colour(i, j),
                                                batch=batch))

    return list


class Board:
    def __init__(self, size, padding, batch):
        self.size = size
        self.padding = padding
        self.board_squares = squares(size, padding, batch)

    def get_square_size(self):
        return self.size / 8

    def get_abs_x(self, rel_x):
        return self.padding + self.size / 8 * rel_x

    def get_abs_y(self, rel_y):
        return self.padding + self.size / 8 * rel_y

    def get_square(self, x, y):
        rel_x = math.floor((x - self.padding) / self.get_square_size())
        rel_y = math.floor((y - self.padding) / self.get_square_size())

        if 0 <= rel_x <= 7 and 0 <= rel_y <= 7:
            return rel_x, rel_y
        return -1, -1  # an invalid position
