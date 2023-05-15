import pyglet
from piece import Piece
from board import Board


def determine_colour(i, j):
    BLACK = (150, 75, 0)
    WHITE = (245, 245, 245)

    if (i + j) % 2 == 0:
        return BLACK
    return WHITE


def main():
    WINDOW_X, WINDOW_Y = 600, 400

    window = pyglet.window.Window(WINDOW_X, WINDOW_Y)
    background = pyglet.graphics.Batch()
    board_batch = pyglet.graphics.Batch()
    pieces = pyglet.graphics.Batch()

    BG = pyglet.shapes.Rectangle(0, 0, WINDOW_X, WINDOW_Y, (10, 100, 100), batch=background)

    board = Board(size=300, padding=50)

    board_squares = []

    for i in range (8):
        for j in range (8):
            board_squares.append(pyglet.shapes.Rectangle(i * board.size/8 + board.padding, j * board.size/8 + board.padding,
                                                         board.size/8, board.size/8, determine_colour(i, j), batch=board_batch))

    pion = Piece(1, 1, "C:/Users/dieks/PycharmProjects/BagelBlitz/venv/images/BlackPawn.png", "gendrik", "Black", pieces, board)

    pion.move(2, 3, board)

    @window.event
    def on_draw():
        window.clear()
        background.draw()
        board_batch.draw()
        pieces.draw()

    pyglet.app.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
