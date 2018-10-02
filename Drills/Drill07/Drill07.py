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

def move_character(p1, p2):
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        return x, y

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

size = 10
n = 1
points = [(random.randint(- (KPU_WIDTH // 2), KPU_WIDTH // 2), random.randint(-(KPU_HEIGHT // 2), KPU_HEIGHT // 2)) for i in range(size)]


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    x, y = move_character(points[n-1], points[n])
    n = (n + 1) % size
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x , y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.1)
    handle_events()

close_canvas()