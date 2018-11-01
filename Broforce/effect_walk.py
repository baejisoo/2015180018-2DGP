from pico2d import *
import game_world
import game_framework

global w, h
w, h = 8, 8

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Effect_walk:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Effect_walk.image == None:
            Effect_walk.image = load_image('effect_walk.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * w, 0, w, h, self.x, self.y, w * 5, h * 5)

    def update(self):
        self.y += self.velocity
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if self.y > 150:
            game_world.remove_object(self)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
