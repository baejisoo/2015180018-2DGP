from pico2d import *
import game_world

global size
size = 3
class Bullet:
    image = None
    sound = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('image/rambro_bullet14x8.png')
        if Bullet.sound == None:
            Bullet.sound = load_wav('sound/Rambro_Shot1.wav')
            Bullet.sound.set_volume(50)

        self.x, self.y, self.velocity = x, y, velocity
        self.sound.play()

    def draw(self):
        self.image.draw(self.x, self.y, 14 * size, 7 * size)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1280 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10