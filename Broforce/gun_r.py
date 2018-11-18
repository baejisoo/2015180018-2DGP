from pico2d import *
import game_world
import game_framework
global w, h, size
w, h, size = 26, 22, 3

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy States
JUMP_LEFT, JUMP_RIGHT, WALK_LEFT, WALK_RIGHT, IDLE_LEFT, IDLE_RIGHT, SHOT_LEFT, SHOT_RIGHT = range(8)


class Gun:
    image = None
    image_fire = None

    def __init__(self, x=1280 // 2, y=720 // 2, state=IDLE_RIGHT):
        if Gun.image == None:
            Gun.image = load_image('rambro_gun_animation.png')
        if Gun.image_fire == None:
            Gun.image_fire = load_image('rambro_gun_shot_animation.png')
        self.x, self.y, self.state = x, y, state
        self.frame = 0
        global gun_state
        gun_state = state

    def draw(self):
        if self.state == IDLE_RIGHT or self.state == JUMP_RIGHT:
            self.image.clip_draw(int(self.frame) * w, h * 3, w, h, self.x, self.y, w * size, h * size)
        elif self.state == IDLE_LEFT or self.state == JUMP_LEFT:
            self.image.clip_draw(int(self.frame) * w, h * 2, w, h, self.x, self.y, w * size, h * size)
        elif self.state == WALK_RIGHT:
            self.image.clip_draw(int(self.frame) * w, h * 1, w, h, self.x, self.y, w * size, h * size)
        elif self.state == WALK_LEFT:
            self.image.clip_draw(int(self.frame) * w, h * 0, w, h, self.x, self.y, w * size, h * size)
        elif self.state == SHOT_RIGHT:
            self.image_fire.clip_draw(int(self.frame) * 40, 22 * 1, 40, 22, self.x, self.y, w * size, h * size)
        elif self.state == SHOT_LEFT:
            self.image_fire.clip_draw(int(self.frame) * 40, 22 * 0, 40, 22, self.x, self.y, w * size, h * size)

    def update(self):
        global gun_state
        self.state = gun_state
        if self.state == IDLE_RIGHT or self.state == IDLE_LEFT:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        elif self.state == WALK_RIGHT or self.state == WALK_LEFT:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        elif self.state == JUMP_RIGHT or self.state == JUMP_LEFT or self.state == SHOT_RIGHT or self.state == SHOT_LEFT:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def set_info(self, x, y, state):
        self.x, self.y = x, y
        self.state = state

