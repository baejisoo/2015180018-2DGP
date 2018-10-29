import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image, startimage, exitimage, selectimage
    global select_frame, select_x, select_y
    select_frame, select_x, select_y = 0, 1280 // 2, 720 // 10 * 3
    image = load_image('logo2.png')
    startimage = load_image('Start.png')
    exitimage = load_image('Exit.png')
    selectimage = load_image('Select.png')

def exit():
    global image
    del(image)


def handle_events():
    global select_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and select_y == 720 // 10 * 1:
                select_y = 720//10 * 3
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and select_y == 720 // 10 * 3:
                select_y = 720//10 * 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if(select_y == 720// 10 * 3):
                    game_framework.change_state(main_state)
                elif(select_y == 720// 10 * 1):
                    game_framework.quit()

def draw():
    clear_canvas()
    image.draw(1280 // 2, 720 // 2)
    selectimage.clip_draw(select_frame * 512, 0, 512, 64, select_x, select_y)
    startimage.draw(1280//2, 720//10 * 3)
    exitimage.draw(1280//2, 720//10 * 1)
    update_canvas()





def update():
    global select_frame
    select_frame = (select_frame + 1) % 8


def pause():
    pass


def resume():
    pass






