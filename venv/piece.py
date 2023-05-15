import pyglet


class Piece:
    def __init__ (self, x, y, img_path, name, color, pieces, board):
        self.x = x #related to board
        self.y = y #related to board
        self.img_path = img_path
        self.name = name
        self.color = color
        self.image_obj = self.load(pieces, board)

    def __repr__ (self):
        return f'x: {self.x}, y: {self.y}, img:{self.img_path}'

    def load (self, batch, board):
        image = pyglet.image.load(self.img_path)
        sprite = pyglet.sprite.Sprite(image, batch=batch)
        sprite.scale_x = board.get_square_size()/sprite.width
        sprite.scale_y = board.get_square_size()/sprite.height
        sprite.x = board.get_abs_x(self.x)
        sprite.y = board.get_abs_y(self.y)
        print("hi")
        return sprite

    def move (self, new_x, new_y, board):
        self.image_obj.x = board.get_abs_x(new_x)
        self.image_obj.y = board.get_abs_y(new_y)