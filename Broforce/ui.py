from pico2d import *

class Ui:
    def __init__(self):
        self.image_ui_back = load_image('Rambro_Face3.png')
        self.image_face = load_image('Rambro_Face0.png')
        self.image_hp = load_image('Rambro_Face4.png')
       #self.bgm = load_wav('Stage1_BGM.wav')
       #self.bgm.set_volume(10)
       #self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image_ui_back.draw(100, 50, 64 * 3, 32 * 3)
        self.image_face.draw(40, 40, 124 / 2, 148 / 2)
        self.image_hp.draw(80, 40, 10 * 3, 10 * 3)
        self.image_hp.draw(110, 40, 10 * 3, 10 * 3)
        self.image_hp.draw(140, 40, 10 * 3, 10 * 3)