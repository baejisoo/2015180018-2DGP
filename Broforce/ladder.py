import random
from pico2d import *
import game_world
import game_framework

class Ladder:
    image = None

    def __init__(self, x=100, y=90):
        self.x, self.y = 1145, 370

    def get_bb(self):
        return self.cx - 10, self.cy, self.cx + 10, self.cy + 320

    def draw(self):
        draw_rectangle(*self.get_bb())

    def update(self):
        # self.x = clamp(0, self.x, self.bg.w)
        # self.y = clamp(50, self.y, 1150)
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom

    def set_background(self, bg):
        self.bg = bg