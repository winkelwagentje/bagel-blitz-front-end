import pyglet
from math import floor
from square import Colour


class Clock:
    def __init__(self, color, batch, x, time=60_000):
        self.color = color
        self.time = time  # milliseconds
        if color == Colour.WHITE:
            y = 80
        else:
            y = 40

        self.label = pyglet.text.Label(text=str(floor(time/1000)), font_name='Arial', font_size=36, x=x, y=y, batch=batch)

    def get_time(self):
        return self.time

    def subtract(self, amount):
        self.time -= amount
        self.label.text = str(floor(self.time/1000))
