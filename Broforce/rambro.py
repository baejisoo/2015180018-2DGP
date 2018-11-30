from pico2d import *
from gun import Gun
from bullet import Bullet
from effect_walk import Effect_walk
from effect_jump import Effect_jump

import game_world
import game_framework

global size, w, h, bullet_w, bullet_h
w, h = 20, 22
size = 3
bullet_w, bullet_h = 14, 8

# rambro Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0           # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
BULLET_SPEED_MPS = 240.0
BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

# rambro Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# rambro Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, JUMP, LAND_TIMER, FIRE, UP_DOWN, DOWN_DOWN = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): JUMP,
    (SDL_KEYDOWN, SDLK_LCTRL): FIRE,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN
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
        elif event == UP_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocity -= RUN_SPEED_PPS

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
        #el#if event == UP_DOWN:
        #    boy.y += 20
        #elif event == DOWN_DOWN:
        #    boy.y -= 20
        boy.unequip_gun()

    @staticmethod
    def do(boy):
        boy.update_gun()
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        #boy.x += boy.velocity * game_framework.frame_time
        boy.y += boy.velocity * game_framework.frame_time
        #if boy.timer == 0:
        #    boy.add_event(SLEEP_TIMER)


    @staticmethod
    def draw(boy):
        x_left_offset = min(0, boy.x - boy.canvas_width // 2)
        x_right_offset = max(0, boy.x - boy.bg.w + boy.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, boy.y - boy.canvas_height // 2)
        y_top_offset = max(0, boy.y - boy.bg.h + boy.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * IDLE_RIGHT, w, h,
                                boy.canvas_width//2+x_offset, boy.canvas_height//2 + y_offset, w * size, h * size)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * IDLE_LEFT, w, h,
                                boy.canvas_width//2+x_offset, boy.canvas_height//2 + y_offset, w * size, h * size)


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
        #boy.x = clamp(25, boy.x, 1280 - 25)
        boy.walk_effect_timer += game_framework.frame_time
        if boy.walk_effect_timer > 0.5:
            boy.create_effect_walk()
            boy.walk_effect_timer = 0
        boy.update_gun()
        boy.walk_sound.play()

    @staticmethod
    def draw(boy):
        x_left_offset = min(0, boy.x - boy.canvas_width // 2)
        x_right_offset = max(0, boy.x - boy.bg.w + boy.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, boy.y - boy.canvas_height // 2)
        y_top_offset = max(0, boy.y - boy.bg.h + boy.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * WALK_RIGHT, w, h,
                                boy.canvas_width//2+x_offset, boy.canvas_height//2 + y_offset,
                                w * size, h * size)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * WALK_LEFT, w, h,
                                boy.canvas_width//2+x_offset, boy.canvas_height//2 + y_offset,
                                w * size, h * size)

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
        #boy.x = clamp(25, boy.x, 1280 - 25)
        boy.jump_timer += game_framework.frame_time
        if boy.jump_timer < 1:
            boy.jump_y += h * 7 * game_framework.frame_time
        elif boy.jump_timer >= 1 and boy.jump_timer <= 2:
            boy.jump_y -= h * 7 * game_framework.frame_time
        elif boy.jump_timer > 2:
            boy.jump_timer = 0
            boy.jump_y = 0
            boy.add_event(LAND_TIMER)

    @staticmethod
    def draw(boy):
        x_left_offset = min(0, boy.x - boy.canvas_width // 2)
        x_right_offset = max(0, boy.x - boy.bg.w + boy.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, boy.y - boy.canvas_height // 2)
        y_top_offset = max(0, boy.y - boy.bg.h + boy.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * w, h * JUMP_RIGHT, w, h,
                                boy.canvas_width//2+x_offset, boy.jump_y + boy.canvas_height//2 + y_offset,
                                w * size, h * size)
        else:
            boy.image.clip_draw(int(boy.frame) * w, h * JUMP_LEFT, w, h,
                                boy.canvas_width//2+x_offset, boy.jump_y + boy.canvas_height//2 + y_offset,
                                w * size, h * size)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                JUMP: JumpState, FIRE: IdleState,
                UP_DOWN: IdleState, DOWN_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               JUMP: JumpState, FIRE: RunState},
    JumpState: {LAND_TIMER: IdleState, JUMP: JumpState,
                RIGHT_UP: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState,
                FIRE: JumpState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 1280 // 2, 90
        self.image = load_image('image/rambro_animation.png')
        self.font = load_font('ttf/Typo_SsangmunDongB.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump_timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.gun_state = IDLE_RIGHT
        self.walk_effect_timer = 0
        self.walk_sound = load_wav('sound/Foot.wav')
        self.walk_sound.set_volume(10000000)
        self.jump_effect_timer = 0
        self.jump_sound = load_wav('sound/Jump.wav')
        self.jump_sound.set_volume(10000000)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.jump_y = 0

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 10
        self.y = self.bg.h / 4

    def equip_gun(self):
        global gun
        gun = Gun(self.x, self.y, self.gun_state)
        game_world.add_object(gun, 1)

    def update_gun(self):
        global gun
        x_left_offset = min(0, self.x - self.canvas_width // 2)
        x_right_offset = max(0, self.x - self.bg.w + self.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, self.y - self.canvas_height // 2)
        y_top_offset = max(0, self.y - self.bg.h + self.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset
        gun.set_info(self.canvas_width // 2 + x_offset, self.jump_y + self.canvas_height // 2 + y_offset, self.gun_state)
        gun.draw()
        gun.update()

    def unequip_gun(self):
        global gun
        game_world.remove_object(gun)

    def fire_bullet(self):
        x_left_offset = min(0, self.x - self.canvas_width // 2)
        x_right_offset = max(0, self.x - self.bg.w + self.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, self.y - self.canvas_height // 2)
        y_top_offset = max(0, self.y - self.bg.h + self.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset
        bullet = Bullet(self.canvas_width // 2 + x_offset, self.jump_y + self.canvas_height // 2 - 7.0 + y_offset, self.dir * 10)
        game_world.add_object(bullet, 1)

    def create_effect_walk(self):
        global effect_walk
        x_left_offset = min(0, self.x - self.canvas_width // 2)
        x_right_offset = max(0, self.x - self.bg.w + self.canvas_width // 2)
        x_offset = x_left_offset + x_right_offset
        y_bottom_offset = min(0, self.y - self.canvas_height // 2)
        y_top_offset = max(0, self.y - self.bg.h + self.canvas_height // 2)
        y_offset = y_bottom_offset + y_top_offset

        effect_walk = Effect_walk(self.canvas_width // 2 + x_offset, self.canvas_height // 2 - 10, 1)


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
        self.font.draw(60, 640, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

