from pico2d import *

class Back:
    def __init__(self):
        self.image = load_image('image/Back.png')
        self.bgm = load_wav('sound/Stage1_BGM.wav')
        self.bgm.set_volume(100000)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280//2, 720//2)
