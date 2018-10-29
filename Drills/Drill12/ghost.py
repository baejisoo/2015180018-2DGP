from pico2d import *
import game_world
import random

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
RUN_SPEED_DPS = (360 * 2 / 3600.0)

class Ghost:
    image = None

    def __init__(self, x = 1600//2, y = 90, velocity = 1):
        global boy_x, boy_y
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
            Ghost.image.opacify(0.5)
        self.x, self.y, self.velocity = x, y, velocity
        self.opacity = random.randrange(0, 10) * 0.1
        boy_x = x
        boy_y = y + 90

        self.move_timer = get_time()
        self.deg = 90
    def draw(self):
        self.image.clip_draw(0 * 100, 300, 100, 100, self.x, self.y)
        self.image.opacify(self.opacity)
    def update(self):
        global boy_x, boy_y
        #self.x += self.velocity
        self.opacity = (random.randrange(0, 10) * 0.1)
        radian = math.radians(360 - self.deg)
        self.x = boy_x + PIXEL_PER_METER * 3 * math.cos(radian) + random.randrange(-1, 1) * 3
        self.y = boy_y + PIXEL_PER_METER * 3 * math.sin(radian)
        self.deg += RUN_SPEED_DPS
        #delay(0.01)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

