import random
import json
import os

from pico2d import *
import game_framework
import game_world
import title_state

from boy import Boy
from back import Back
from stage_one_back import Stage_one_back

name = "MainState"

boy = None
back = None
stage_one_back = None





def enter():
    global boy, back, stage_one_back
    boy = Boy()
    back = Back()
    stage_one_back = Stage_one_back()

    game_world.add_object(back, 0)
    game_world.add_object(stage_one_back, 0)
    game_world.add_object(boy, 1)

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







