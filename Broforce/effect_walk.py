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

    def __init__(self, x = 640, y = 360, velocity = 1):
        if Effect_walk.image == None:
            Effect_walk.image = load_image('image/effect_walk.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.timer = 0
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * w, 0, w, h, self.x, self.y, w * 5, h * 5)

    def update(self):
        self.timer += self.velocity
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if self.timer > + 10:
            game_world.remove_object(self)

        if self.x < 25 or self.x > 1600 - 25:
            #game_world.remove_object(self)
            pass