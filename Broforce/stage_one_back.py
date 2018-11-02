from pico2d import *

class Stage_one_back:
    def __init__(self):
        self.image = load_image('StageOne_Back1.png')
       #self.bgm = load_wav('Stage1_BGM.wav')
       #self.bgm.set_volume(10)
       #self.bgm.repeat_play()
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.left = clamp(0, int(self.set_center_object.x) -
                          self.canvas_width // 2, self.w - self.canvas_width)
        self.bottom = clamp(0, int(self.set_center_object.y) -
                            self.canvas_height // 2, self.h - self.canvas_height)

    def draw(self):
        self.image.clip_draw_to_origin(self.left, self.bottom, self.canvas_width,
                                       self.canvas_height, 0, 0)

    def set_center_object(self, boy):
        self.set_center_object = boy
