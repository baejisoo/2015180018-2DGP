import game_framework
import main_state
from pico2d import *

import main_state

name = "PauseState"
image = None

pause_time = 0.0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def draw():
    clear_canvas()
    if(pause_time > 0.5):
        image.draw(400, 300)

    main_state.grass.draw()

    update_canvas()





def update():
    global pause_time

    if(pause_time > 1.0):
        pause_time = 0
    delay(0.01)
    pause_time += 0.01


def pause():
    pass


def resume():
    pass






