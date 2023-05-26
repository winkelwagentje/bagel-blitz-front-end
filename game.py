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
        for piecelogic in self.pieces:
            if piecelogic.x == selected_square.x and piecelogic.y == selected_square.y:
                return False
        return True

    def is_valid_move(self, from_square, to_square):  # returns true iff the move requested is allowed
        piececode = ""
        for piecelogic in self.pieces:
            if piecelogic.x == from_square.x and piecelogic.y == from_square.y:
                piececode = piecelogic.code
                break
        match piececode:
            case "BB":
                #still need to check if a move doesnt put its own king in check.
                if abs(to_square.x - from_square.x) == abs(to_square.y - from_square.y) and 0 <= to_square.x <= 7 and 0 <= to_square.y <= 7:
                    return True
                return False
            case "BK":
                raise Exception("not implemented yet")
            case "BN":
                raise Exception("not implemented yet")
            case "BP":
                raise Exception("not implemented yet, also watch en passent")
            case "BQ":
                raise Exception("not implemented yet")
            case "BR":
                raise Exception("not implemented yet")
            case "WB":
                raise Exception("not implemented yet")
            case "WK":
                raise Exception("not implemented yet")
            case "WN":
                raise Exception("not implemented yet")
            case "WP":
                raise Exception("not implemented yet")
            case "WQ":
                raise Exception("not implemented yet")
            case "WR":
                raise Exception("not implemented yet")
        raise Exception("is_valid_move is not implemented yet")

    def move(self, from_square, to_square):  # moves a piece from from_square to to_square
        if not self.is_valid_move(from_square, to_square):
            raise Exception("you requested an invalid move")

        raise Exception("move is not implemented yet")

