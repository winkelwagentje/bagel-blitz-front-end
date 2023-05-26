from math import floor
from enumerators import SquareState
from square import Square
from piece import PieceGUI


"""
Board class stores and handles all the GUI of the board
"""


class Board:
    def __init__(self, size, padding, batch, pieces):
        self.size = size
        self.padding = padding
        self.batch = batch
        self.board_squares = self.create_squares(size, padding)
        self.pieces = self.create_pieces(pieces)

    def create_squares(self, size, padding):  # initializes all the UI squares of the board
        list_of_squares = []
        for i in range(8):
            for j in range(8):
                list_of_squares.append(Square(i, j, self.square_width(), self.padding, self.batch))

        return list_of_squares

    def create_pieces(self, pieces):  # initializes all the UI pieces of the game_state
        list_of_pieces = []
        for piece in pieces:
            list_of_pieces.append(PieceGUI(piece.x, piece.y, piece.code, self.batch, self.square_width(), self))

        return list_of_pieces

    def square_width(self):  # returns the width of a square inside the board
        return self.size / 8

    def get_abs_x(self, rel_x):  # converts x relative to the board to absolute coordinates
        return self.padding + self.size / 8 * rel_x

    def get_abs_y(self, rel_y):  # converts y relative to the board to absolute coordinates
        return self.padding + self.size / 8 * rel_y

    def get_rel_xy(self, x, y):  # converts absolute x and y to x and y relative to the board
        rel_x = floor((x - self.padding) / self.square_width())
        rel_y = floor((y - self.padding) / self.square_width())

        if 0 <= rel_x <= 7 and 0 <= rel_y <= 7:
            return rel_x, rel_y
        return -1, -1  # an invalid position

    def get_square(self, rel_x, rel_y):  # returns the square object at rel_x and rel_y
        return self.board_squares[rel_x * 8 + rel_y]

    def get_selected_square(self):  # returns the square object of the selected square
        for square in self.board_squares:
            if square.state == SquareState.SELECTED:
                return square
        return None

    def is_selected(self):  # returns true if the board is selected
        for square in self.board_squares:
            if square.state == SquareState.SELECTED:
                return True
        return False

    def deselect(self):  # deselects the entire board
        for square in self.board_squares:
            square.deselect()

    def get_piece(self, square):  # returns the pieceGUI object of square
        pass
