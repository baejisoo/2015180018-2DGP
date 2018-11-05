from pico2d import *

from gun import Gun
from bullet import Bullet
from effect_walk import Effect_walk
from effect_jump import Effect_jump

import game_world
import game_framework

global w, h, bullet_w, bullet_h
w, h = 20, 22
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

# Mook Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, JUMP, LAND_TIMER, FIRE = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): JUMP,
    (SDL_KEYDOWN, SDLK_LCTRL): FIRE
}

# Boy States
JUMP_LEFT, JUMP_RIGHT, WALK_LEFT, WALK_RIGHT, IDLE_LEFT, IDLE_RIGHT, SHOT_LEFT, SHOT_RIGHT = range(8)


class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        if boy.dir == 1:
            boy.gun_state = IDLE_RIGHT
        else:
            boy.gun_state = IDLE_LEFT
        boy.equip_gun()

    @staticmethod
    def exit(boy, event):
        if event == FIRE:
            if boy.dir == 1:
                boy.gun_state = SHOT_RIGHT
            else:
                boy.gun_state = SHOT_LEFT
            boy.fire_bullet()
        boy.unequip_gun()

    @staticmethod
    def do(boy):
        boy.update_gun()
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.x += boy.velocity * game_framework.frame_time
        #if boy.timer == 0:
        #    boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * IDLE_RIGHT, w, h, boy.x, boy.y, w * 5, h * 5)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * IDLE_LEFT, w, h, boy.x, boy.y, w * 5, h * 5)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        boy.dir = clamp(-1, boy.velocity, 1)
        if boy.dir == 1:
            boy.gun_state = WALK_RIGHT
        else:
            boy.gun_state = WALK_LEFT
        boy.equip_gun()
        #boy.walk_sound.repeat_play()

    @staticmethod
    def exit(boy, event):
        if event == FIRE:
            if boy.dir == 1:
                boy.gun_state = SHOT_RIGHT
            else:
                boy.gun_state = SHOT_LEFT
            boy.fire_bullet()
        boy.unequip_gun()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.walk_effect_timer += game_framework.frame_time
        if boy.walk_effect_timer > 0.5:
            boy.create_effect_walk()
            boy.walk_effect_timer = 0
        boy.update_gun()
        boy.walk_sound.play()

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * WALK_RIGHT, w, h, boy.x, boy.y, w * 5, h * 5)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * WALK_LEFT, w, h, boy.x, boy.y, w * 5, h * 5)


class JumpState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        if boy.dir == 1:
            boy.gun_state = JUMP_RIGHT
        else:
            boy.gun_state = JUMP_LEFT
        boy.equip_gun()
        boy.jump_sound.play()

    @staticmethod
    def exit(boy, event):
        if event == FIRE:
            if boy.dir == 1:
                boy.gun_state = SHOT_RIGHT
            else:
                boy.gun_state = SHOT_LEFT
            boy.fire_bullet()
        boy.unequip_gun()

    @staticmethod
    def do(boy):
        boy.update_gun()
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.jump_timer += game_framework.frame_time
        if boy.jump_timer < 1:
            boy.y += h * 7 * game_framework.frame_time
        elif boy.jump_timer >= 1 and boy.jump_timer <= 2:
            boy.y -= h * 7 * game_framework.frame_time
        elif boy.jump_timer > 2:
            boy.jump_timer = 0
            boy.add_event(LAND_TIMER)


    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * JUMP_RIGHT, w, h, boy.x, boy.y, w * 5, h * 5)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * JUMP_LEFT, w, h, boy.x, boy.y, w * 5, h * 5)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                FIRE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               FIRE: RunState},
}


class Mook:

    def __init__(self):
        self.x, self.y = 640, 90
        self.image = load_image('rambro_animation.png')
        self.font = load_font('Typo_SsangmunDongB.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump_timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.gun_state = IDLE_RIGHT
        self.walk_effect_timer = 0
        self.walk_sound = load_wav('Foot.wav')
        self.walk_sound.set_volume(8)
        self.jump_effect_timer = 0
        self.jump_sound = load_wav('Jump.wav')
        self.jump_sound.set_volume(8)

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

    def create_effect_walk(self):
        global effect_walk
        effect_walk = Effect_walk(self.x, self.y - 25, 1)
        game_world.add_object(effect_walk, 1)

    def create_effect_jump(self):
        global effect_jump
        effect_jump = Effect_jump(self.x, self.y - 25, 1)
        game_world.add_object(effect_jump, 1)

    def delete_effect_jump(self):
        global effect_jump
        game_world.remove_object(effect_jump)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
