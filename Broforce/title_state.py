import game_framework
import main_state
import scroll_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image, startimage, exitimage, selectimage
    global select_frame, select_x, select_y
    global bgm, select_sound
    select_frame, select_x, select_y = 0, 1280 // 2, 720 // 10 * 3
    image = load_image('image/logo2.png')
    startimage = load_image('image/Start.png')
    exitimage = load_image('image/Exit.png')
    selectimage = load_image('image/Select.png')

    bgm = load_wav('sound/MenuBGM.wav')
    bgm.set_volume(10)
    bgm.repeat_play()

    select_sound = load_wav('sound/Rambro_Shot1.wav')
    select_sound.set_volume(10)

def exit():
    global image, bgm, select_sound
    del(image)
    del(bgm)
    del(select_sound)

def handle_events():
    global select_y, select_sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and select_y == 720 // 10 * 1:
                select_y = 720//10 * 3
                select_sound.play()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and select_y == 720 // 10 * 3:
                select_y = 720//10 * 1
                select_sound.play()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if select_y == 720 / 10 * 3:
                    select_sound.play()
                    game_framework.change_state(scroll_state)
                elif select_y == 720 / 10 * 1:
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






