import random
import json
import os

from pico2d import *
import game_framework
import game_world

from back import Back
#from stage_one_back import Stage_one_back
from stage_one_back import FixedTileBackground as Stage_one_Back

from boy import Boy
from mook import Mook
from ladder import Ladder
from ui import Ui

name = "ScrollState"

mook_position = [(2010, 390), (500, 390), (2200, 390), (2010, 390), (500, 390), (2200, 390)]
ladder_position = [(300, 200), (300, 400)]
boy = None
mooks = []
bullets = []
ladders=[]

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

    global back
    back = Back()
    game_world.add_object(back, 0)

    global stage_one_back
    stage_one_back = Stage_one_Back()
    game_world.add_object(stage_one_back, 0)

    # global ladders
    # ladders = [Ladder(ladder_position[i]) for i in range(2)]
    # for ladder in ladders:
    #     ladder.set_background(stage_one_back)
    # game_world.add_objects(ladders, 1)

    global boy
    boy = Boy()
    game_world.add_object(boy, 2)

    global mooks
    mooks = [Mook(mook_position[i]) for i in range(6)]

    for mook in mooks:
        mook.set_background(stage_one_back)
    game_world.add_objects(mooks, 4)

    stage_one_back.set_center_object(boy)
    boy.set_background(stage_one_back)

    global ui
    ui= Ui()
    game_world.add_object(ui, 6)

    # global boy, mook, back, stage_one_back, ui
    # boy = Boy()
    # mook = Mook()
    # back = Back()
    # stage_one_back = Stage_one_Back()
    # ui = Ui()
    # game_world.add_object(back, 0)
    # game_world.add_object(stage_one_back, 0)
    # game_world.add_object(ui, 0)
    # game_world.add_object(boy, 1)
    # game_world.add_object(mook, 1)
#
    # stage_one_back.set_center_object(boy)
    # stage_one_back.set_center_object(mook)
    # boy.set_background(stage_one_back)
    # mook.set_background(stage_one_back)


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

    for bullet in game_world.objects[3]:
        for mook in mooks:
            if collide(bullet, mook) and mook.hp >= 0:
                mook.hp -= 1
                game_world.remove_object(bullet)
                print(mook.hp)

    for mook in mooks:
        if (mook.hp < 0):
            game_world.remove_object(mook)

    # for ladder in game_world.objects[1]:
    #     if collide(ladder, boy):
    #         boy.bIsLadder = True
    #     else:
    #         boy.bIsLadder = False

        #print(boy.bIsLadder)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







