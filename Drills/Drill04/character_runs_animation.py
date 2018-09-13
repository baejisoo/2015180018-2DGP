from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
dir = 'right'

while(True):
    if(dir == 'right'):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 10

        if(x > 800):
            dir = 'left'

        delay(0.05)
        get_events()

    if(dir == 'left'):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 5) % 8
        x -= 10

        if(x < 0):
            dir = 'right'

        delay(0.05)
        get_events()

close_canvas()

