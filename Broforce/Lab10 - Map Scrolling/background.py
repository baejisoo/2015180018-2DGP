import random

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('StageOne_Back.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        # fill here
        self.set_center_object = boy

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(
            self.left, 0, self.canvas_width,
            self.canvas_height, 0, 0
        )


    def update(self, frame_time):
        # fill here
        self.left = clamp(0, int(self.set_center_object.x) -
                          self.canvas_width // 2, self.w - self.canvas_width)

    def handle_event(self, event):
        pass


class InfiniteBackground:


    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy


    def draw(self):
        # fill here
        pass


    def update(self, frame_time):
        # fill here
        pass

    def handle_event(self, event):
        pass




