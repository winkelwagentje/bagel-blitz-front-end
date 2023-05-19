import pyglet
from piece import Piece
from board import Board
from mouse_handler import *
from json_handler import *
from clock import Clock
from square import Colour
from enum import Enum


class Screen(Enum):
    START = 0,
    GAME = 1,


SCREEN_STATE = Screen.START
def main():
    WINDOW_X, WINDOW_Y = 600, 400
    REFRESH_RATE = 1/10.0

    window = pyglet.window.Window(WINDOW_X, WINDOW_Y)
    background = pyglet.graphics.Batch()
    board_batch = pyglet.graphics.Batch()
    pieces = pyglet.graphics.Batch()
    clock_batch = pyglet.graphics.Batch()
    start_screen_batch = pyglet.graphics.Batch()

    window.set_caption("")

    BG = pyglet.shapes.Rectangle(0, 0, WINDOW_X, WINDOW_Y, (10, 100, 100), batch=background)

    STRT_BG = pyglet.shapes.Rectangle(0, 0, WINDOW_X, WINDOW_Y, (40, 130, 130), batch=start_screen_batch)
    STRT_LBL = pyglet.text.Label(text="PRESS any KEY to START", font_name='Arial', font_size=24, x=WINDOW_X / 2 - 100, y=50, batch=start_screen_batch)

    board = Board(size=300, padding=50, batch=board_batch)
    clock_white = Clock(Colour.WHITE, clock_batch, WINDOW_X-150)
    clock_black = Clock(Colour.BLACK, clock_batch, WINDOW_X-150)

    initial_board = listen()

    board.update(initial_board["board-layout"], pieces)

    def update(dt):
        new_board = listen()

        if board.colour_to_move == Colour.WHITE:
            clock_white.subtract(REFRESH_RATE * 1000)
        else:
            clock_black.subtract(REFRESH_RATE * 1000)

        if new_board["updated"] == 1:
            print("Board is updated")
            board.update(new_board["board-layout"])
            clear_local_JSON()

        if SCREEN_STATE != Screen.START and STRT_BG.visible:
            if STRT_BG.y < WINDOW_Y:
                STRT_BG.y += 10
                STRT_LBL.y += 10
            else:
                STRT_BG.visible = False
                STRT_LBL.visible = False

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global SCREEN_STATE
        if SCREEN_STATE == Screen.GAME:
            if area(x, y, board) == Field.BOARD:
                if board.is_selected() and board.get_selected_square().content is not None:
                    move_request(board, board.get_selected_square().content, board.get_board_coordinates(x, y))
                else:
                    board.deselect()
                    a, b = board.get_board_coordinates(x, y)
                    board.get_square(a, b).select()
            else:
                board.deselect()

    @window.event
    def on_key_press(symbol, modifiers):
        global SCREEN_STATE
        if SCREEN_STATE == Screen.START:
            SCREEN_STATE = Screen.GAME


    @window.event
    def on_draw():
        window.clear()
        background.draw()
        board_batch.draw()
        pieces.draw()
        clock_batch.draw()
        start_screen_batch.draw()

    pyglet.clock.schedule_interval(update, REFRESH_RATE)
    pyglet.app.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
