from pico2d import *

class Back:
    def __init__(self):
        self.image = load_image('Back.png')
        self.bgm = load_wav('Stage1_BGM.wav')
        self.bgm.set_volume(10)
        self  .bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280//2, 720//2)
