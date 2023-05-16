from piece import Piece
from board import Board


def move_test(x, y, button, modifiers, board, pion):
    print(board.get_board_coordinates(x, y))
    v, w = board.get_board_coordinates(x, y)
    if (v, w) != (-1, -1):
        pion.move(v, w, board)
