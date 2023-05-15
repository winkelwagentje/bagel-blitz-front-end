
class Board:
    def __init__ (self, size, padding):
        self.size = size
        self.padding = padding

    def get_square_size (self):
        return self.size/8

    def get_abs_x(self, rel_x):
        return self.padding+self.size/8*rel_x

    def get_abs_y(self, rel_y):
        return self.padding+self.size/8*rel_y