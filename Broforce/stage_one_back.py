from pico2d import *

class Stage_one_back:
    def __init__(self):
        self.image = load_image('StageOne_Back.png')
       #self.bgm = load_wav('Stage1_BGM.wav')
       #self.bgm.set_volume(10)
       #self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.image.w / 2, self.image.h / 2)