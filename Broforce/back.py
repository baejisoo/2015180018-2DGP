from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Back.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280//2, 720//2)
