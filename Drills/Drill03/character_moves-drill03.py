from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 402
y = 90
square = True
circle = False
dir = 'right'

while (True):
    while(square == True):
        clear_canvas_now()
        grass.draw_now(400,30)
        if(dir == 'right'):
            x += 2
            y = 90
            if(x > 800):
                dir = 'up'
            elif (x == 400):
                circle = True
                square = False
        elif (dir == 'up'):
            y += 2
            x = 800
            if(y > 600):
                dir = 'left'
        elif(dir == 'left'):
            x -= 2
            y = 600
            if(x < 0):
                dir = 'down'
        elif(dir == 'down'):
            y -= 2
            x = 0 
            if(y<90):
                dir='right'

        character.draw_now(x, y)        
        delay(0.01)

    while(circle == True):
        for deg in range(90, 360 + 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            r = (360 - deg) * math.pi / 180
            x = 400 + 205 * math.cos(r)
            y = 300 + 205 * math.sin(r)
            character.draw_now(x, y)
            delay(0.01)
        square = True
        circle = False
        x = 402
        dir = 'right'

close_canvas()
