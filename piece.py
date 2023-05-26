import pyglet


"""
PieceGUI class stores and handles all the GUI of a piece
"""


class PieceGUI:
    def __init__(self, x, y, code, batch, size, board):
        self.x = x  # related to board
        self.y = y  # related to board
        self.code = code
        self.size = size
        self.image_obj = self.load(batch, board)

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}, img:images/{self.code}.png'

    def load(self, batch, board):  # loads the sprite into the window
        image = pyglet.image.load(f"images/{self.code}.png")
        sprite = pyglet.sprite.Sprite(image, batch=batch)
        sprite.scale_x = self.size / sprite.width
        sprite.scale_y = self.size / sprite.height
        sprite.x = board.get_abs_x(self.x)
        sprite.y = board.get_abs_y(self.y)
        return sprite

    def move_to(self, new_x, new_y, board):  # moves the sprite to a new location
        board.get_square(self.x, self.y).empty()

        self.x = new_x
        self.y = new_y

        self.image_obj.x = board.get_abs_x(new_x)
        self.image_obj.y = board.get_abs_y(new_y)

        board.get_square(self.x, self.y).set_piece(self)


"""
PieceLogic class stores and handles all the logic of a piece
"""


class PieceLogic:
    def __init__(self, code, x, y):
        self.code = code
        self.x = x
        self.y = y
