import random
import json
import os

from pico2d import *
import game_framework
import game_world
import title_state

from boy import Boy
from mook import Mook
from back import Back
#from stage_one_back import Stage_one_back
from stage_one_back import FixedTileBackground as Stage_one_Back
from ui import Ui

name = "ScrollState"

rambro = None
back = None
stage_one_back = None


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global boy, mook, back, stage_one_back, ui
    boy = Boy()
    back = Back()
    stage_one_back = Stage_one_Back()
    ui = Ui()
    game_world.add_object(back, 0)
    game_world.add_object(stage_one_back, 0)
    game_world.add_object(ui, 0)
    game_world.add_object(boy, 1)

    stage_one_back.set_center_object(boy)
    boy.set_background(stage_one_back)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







