import pyglet
from board import Board
from mouse_handler import *
from clock import Clock
from game import Game
from enumerators import Color


def main():
    # window parameters
    WINDOW_X, WINDOW_Y = 600, 400
    REFRESH_RATE = 1 / 100.0

    # window initialization
    window = pyglet.window.Window(WINDOW_X, WINDOW_Y)
    window.set_caption("")

    # batch initialization
    background = pyglet.graphics.Batch()
    board_batch = pyglet.graphics.Batch()
    clock_batch = pyglet.graphics.Batch()

    # board initialization
    game_state = Game([])
    game_state.add_pieces()
    board = Board(size=300, padding=50, batch=board_batch, pieces=game_state.pieces)

    # shape creation
    BG = pyglet.shapes.Rectangle(0, 0, WINDOW_X, WINDOW_Y, (10, 100, 100), batch=background)

    # clock creation
    clock_white = Clock(Color.WHITE, clock_batch, WINDOW_X - 150)
    clock_black = Clock(Color.BLACK, clock_batch, WINDOW_X - 150)

    def update(dt):  # every frame update
        if game_state.color_to_move == Color.WHITE:
            clock_white.subtract(REFRESH_RATE * 1000)
        else:
            clock_black.subtract(REFRESH_RATE * 1000)

    @window.event
    def on_mouse_press(x, y, button, modifiers):  # mouse handler
        if on_board(x, y, board):  # clicked on the board
            if board.is_selected():
                handle_second_click(x, y, button, modifiers, board, game_state)
            else:
                handle_first_click(x, y, button, modifiers, board)
        elif on_button(x, y):  # clicked on a button
            handle_button(x, y, button, modifiers)
        else:  # clicked on nothing
            handle_empty_click(x, y, button, modifiers, board)

    @window.event
    def on_key_press(symbol, modifiers):  # keyboard handler
        pass

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        handle_cursor_type(x, y, board, window)
        handle_button_hover(x, y)

    @window.event
    def on_draw():  # drawer
        window.clear()
        background.draw()
        board_batch.draw()
        clock_batch.draw()

    pyglet.clock.schedule_interval(update, REFRESH_RATE)
    pyglet.app.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
