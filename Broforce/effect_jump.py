from pico2d import *
import game_world
import game_framework

global w, h
w, h = 16, 16

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Effect_jump:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Effect_jump.image == None:
            Effect_jump.image = load_image('image/effect_jump.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.timer = 0
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * w, 0, w, h, self.x, self.y, w * 5, h * 5)

    def update(self):
        self.timer += self.velocity
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

        if self.timer > 30:
            game_world.remove_object(self)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
