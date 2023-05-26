from enumerators import Color
from piece import PieceLogic


"""
Game class stores and handles all the game state data.
"""


class Game:
    def __init__(self, history):
        self.color_to_move = Color.WHITE
        self.pieces = []
        self.history = history

    def add_pieces(self):
        self.pieces.append(PieceLogic("WK", 2, 7))

    def square_is_empty(self, selected_square):  # returns true iff there is no piece occupying the square
        raise Exception("square_is_empty is not implemented yet")

    def is_valid_move(self, from_square, to_square):  # returns true iff the move requested is allowed
        raise Exception("is_valid_move is not implemented yet")

    def move(self, from_square, to_square):  # moves a piece from from_square to to_square
        if not self.is_valid_move(from_square, to_square):
            raise Exception("you requested an invalid move")

        raise Exception("move is not implemented yet")

