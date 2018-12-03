from pico2d import *
import math
import random

import game_world
import game_framework
import scroll_state
from bullet import Bullet
from gun import Gun

global w, h, size, bullet_w, bullet_h
w, h = 20, 22
size = 3
bullet_w, bullet_h = 14, 8

# Mook Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0           # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
BULLET_SPEED_MPS = 240.0
BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

# Mook Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Mook States
IDLE_LEFT, IDLE_RIGHT, WALK_LEFT, WALK_RIGHT, SHOT_LEFT, SHOT_RIGHT = range(6)

class Mook:
    image = None
    font = None

    def __init__(self, x=100, y=90):
        self.x, self.y = 2400, 390
        if Mook.font is None:
            Mook.font = load_font('ttf/Typo_SsangmunDongB.TTF', 16)
        if Mook.image == None:
            Mook.image = load_image('image/mook_animation.png')
        self.dir = random.random()*2*math.pi
        self.speed = 0
        self.frame = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.state = IDLE_RIGHT
        self.hp = 3
        #self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), random.randint(0, 1600 - 1), 0

    def get_bb(self):
        return self.cx - 20, self.cy - 30, self.cx + 20, self.cy + 30

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random()*2*math.pi

    def find_player(self):
        # boy = scroll_state.get_boy()
        # distance = (boy.x - self.x)**2 + (boy.y - self.y)**2

        pass

    def equip_gun(self):
        global gun
        gun = Gun(self.x, self.y, self.gun_state)
        game_world.add_object(gun, 1)

    def update_gun(self):
        global gun
        gun.set_info(self.x, self.y, self.gun_state)
        gun.draw()
        gun.update()

    def unequip_gun(self):
        global gun
        game_world.remove_object(gun)

    def fire_bullet(self):
        bullet = Bullet(self.x, self.y - 7.0, self.dir * 10)
        game_world.add_object(bullet, 1)


    def update(self):
        self.x = clamp(2100,self.x, 3600)
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir)* game_framework.frame_time
        self.wander()
        if math.cos(self.dir) < 0:
            self.state = WALK_LEFT
        else:
            self.state = WALK_RIGHT

        pass

    def draw(self):
        if self.state == IDLE_LEFT:
            self.image.clip_draw(int(self.frame) * w, h * 5, w, h, self.cx, self.cy, w * size, h * size)
        elif self.state == IDLE_RIGHT:
            self.image.clip_draw(int(self.frame) * w, h * 4, w, h, self.cx, self.cy, w * size, h * size)
        elif self.state == WALK_LEFT:
            self.image.clip_draw(int(self.frame) * w, h * 0, w, h, self.cx, self.cy, w * size, h * size)
        elif self.state == WALK_RIGHT:
            self.image.clip_draw(int(self.frame) * w, h * 1, w, h, self.cx, self.cy, w * size, h * size)


        #draw_rectangle(*self.get_bb())
        #self.font.draw(self.cx - 60, self.cy + 50, '(X,Y: %d, %d)' % (self.cx, self.cy), (255, 255, 0))

    def set_background(self, bg):
        self.bg = bg

    def get_mook(self):
        return self.x, self.y
