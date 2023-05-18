import pyglet
from piece import Piece
from board import Board
from mouse_handler import *
from json_handler import *


def main():
    WINDOW_X, WINDOW_Y = 600, 400

    window = pyglet.window.Window(WINDOW_X, WINDOW_Y)
    background = pyglet.graphics.Batch()
    board_batch = pyglet.graphics.Batch()
    pieces = pyglet.graphics.Batch()

    window.set_caption("")

    BG = pyglet.shapes.Rectangle(0, 0, WINDOW_X, WINDOW_Y, (10, 100, 100), batch=background)

    board = Board(size=300, padding=50, batch=board_batch)
    # pion = Piece(1, 1, "images/BlackPawn.png", "gendrik", "Black", pieces, board)

    # request({"move": [-1, -1]})

    initial_board = listen()

    board.update(initial_board["board-layout"])

    def update(dt):
        new_board = listen()

        if new_board["updated"] == 1:
            print("Board is updated")
            board.update(new_board["board-layout"])
            clear_local_JSON()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if area(x, y, board) == Field.BOARD:
            if board.is_selected() and board.get_selected_square().content is not None:
                move_request(board, board.get_selected_square().content, board.get_board_coordinates(x, y))
            else:
                board.get_board_coordinates(x, y).select()
        else:
            board.deselect()

    @window.event
    def on_draw():
        window.clear()
        background.draw()
        board_batch.draw()
        pieces.draw()

    pyglet.clock.schedule_interval(update, 1 / 1.0)
    pyglet.app.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
