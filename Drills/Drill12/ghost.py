from pico2d import *
from PIL import Image, ImageFilter
import game_world
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 360

PIXEL_PER_DEG = math.pi / 180.0
CIR_SPEED_KMPH = 720
class Ghost:
    image = None

    def __init__(self, x = 1600//2, y = 90, velocity = 1):
        global boy_x, boy_y
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
            im = Image.open('animation_sheet.png')
            blurImage = im.filter(ImageFilter.BLUR)
            blurImage.save('animation_sheet-blur.png')
            Ghost.image = load_image('animation_sheet-blur.png')
            Ghost.image.opacify(0.5)
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.opacity = random.randrange(0, 10) * 0.1
        boy_x = x
        boy_y = y + 90

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)
        self.image.opacify(self.opacity)

    def update(self):
        global boy_x, boy_y
        self.opacity = (random.randrange(0, 10) * 0.1)

        self.velocity = (self.velocity + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 360
        #radian = math.radians(360 - self.deg)
        radian = self.velocity * math.pi / 180
        self.x = boy_x + PIXEL_PER_METER * 3 * math.cos(radian) + random.randrange(0, 1) * 10
        self.y = boy_y + PIXEL_PER_METER * 3 * math.sin(radian)

        self.frame = (self.frame + 8 * ACTION_PER_TIME * game_framework.frame_time) % 8


