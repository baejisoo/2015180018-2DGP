import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import main_state
import world_build_state

boy = None
name = "WorldBuildState"
rank = []
for i in range(0,10):
    rank.append(0)

def enter():
    hide_cursor()
    hide_lattice()


def exit():
    pass

def pause():
    pass


def resume():
    pass


def get_boy():
    return boy


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    font = load_font('ENCR10B.TTF', 20)
    for i in range(0, 10):
        font.draw(400, 800 - i*50, str(i) + " - " + str(rank[i]), (255, 0, 0))

    update_canvas()