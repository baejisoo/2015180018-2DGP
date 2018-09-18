from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.

route =[(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]
now = 0
next = now + 1
def make_dir(now, next):
    dirX = route[next][0] - route[now][0]
    dirY = route[next][0] - route[now][0]
    return dirX, dirY
def move_by_dir():
    pass
def make_animation():
    pass

def make_routine():
    dirX, dirY = make_dir(now, next)
    move_by_dir()
    make_animation()
    pass

while True:
    make_routine()

close_canvas()

