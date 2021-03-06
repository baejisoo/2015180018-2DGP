from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 여기를 채우세요.

route =[(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]
now = 0
next = now + 1
xPos, yPos = route[0][0], route[0][1]

def make_dir(now, next):
    dirX = route[next][0] - route[now][0]
    dirY = route[next][1] - route[now][1]
    return dirX, dirY

def move_by_dir(dirX, dirY):
    return dirX * 0.1, dirY * 0.1

def make_animation(xPos, yPos, dirX, frame):
    if(dirX < 0):
        character.clip_draw(100 * frame, 0, 100, 100, xPos, yPos)
    else:
        character.clip_draw(100 * frame, 100, 100, 100, xPos, yPos)

def make_routine(now, next):
    xPos, yPos = route[now][0], route[now][1]
    #print(xPos, yPos)
    dirX, dirY = make_dir(now, next)
    moveX, moveY = move_by_dir(dirX, dirY)
    #print(moveX, moveY)
    cnt = 0
    frame = 0
    while cnt < 10:
        clear_canvas()
        grass.draw(400,30)
        xPos += moveX
        yPos += moveY
        print(xPos, yPos)
        cnt += 1
        #character.clip_draw(100, 100, 100, 100, 400, 300)
        #character.draw_now(xPos, yPos)
        make_animation(xPos, yPos, dirX, frame)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.1)

idx = 0
final = len(route)
while True:

    if(idx < len(route) - 1):
        make_routine(idx, idx + 1)
        idx += 1
    elif(idx == len(route) - 1):
        make_routine(idx, 0)
        idx = 0


close_canvas()

