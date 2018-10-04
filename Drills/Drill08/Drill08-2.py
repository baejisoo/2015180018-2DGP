from pico2d import*
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_stamp(p, dir, frame):
    character.clip_draw(2 * 100, 100 * dir, 100, 100, p[0], p[1])

def draw_curve_3_points(p1, p2, p3):
    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
    return x, y

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

def move_character(p1, p2, p3):
    frame = 0
    prevX = 0
    for i in range(0, 100 + 1, 2):
        dir = 0


        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

        if (prevX > x):
            dir = 0
        elif (prevX < x):
            dir = 1
        elif (prevX == x):
            pass

        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)

        prevX = x


        if(x, y == p1[0], p1[1]):
            draw_stamp(p1, dir, frame)
        if (x, y == p2[0], p2[1]):
            draw_stamp(p2, dir, frame)
        if (x, y == p3[0], p3[1]):
            draw_stamp(p3, dir, frame)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


size = 10
n = 0
points = [(random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(size)]

while running:
    #move_character(points[2 * n], points[2 * n -1], points[2 * (n - 1)])
    #n = (n + 1) % size
    move_character(points[0], points[1], points[2])
    move_character(points[2], points[3], points[4])
    move_character(points[4], points[5], points[6])
    move_character(points[6], points[7], points[8])
    move_character(points[8], points[9], points[0])



close_canvas()