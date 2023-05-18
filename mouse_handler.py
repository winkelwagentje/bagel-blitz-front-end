from piece import Piece
from board import Board
from enum import Enum

class Field(Enum):
    BOARD = 0
    OTHER = 1


def move_test(x, y, button, modifiers, board, pion):
    print(board.get_board_coordinates(x, y))
    v, w = board.get_board_coordinates(x, y)
    if (v, w) != (-1, -1):
        pion.move(v, w, board)



def select_square(x, y, button, modifiers, board):
    rel_x, rel_y = board.get_board_coordinates(x, y)
    board.deselect()
    if (rel_x, rel_y) != (-1, -1):
        board.get_square(rel_x, rel_y).select()

def area(board, x, y):
    if board.padding <= x <= board.padding + board.size and board.padding <= y <= board.padding + board.size:
        return Field.BOARD
    return Field.OTHER
