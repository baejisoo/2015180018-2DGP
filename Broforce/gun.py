from pico2d import *
import game_world

global w, h
w, h = 50, 55

# Boy States
IDLE_RIGHT, IDLE_LEFT, WALK_RIGHT, WALK_LEFT = range(4)

class Gun:
    image = None

    def __init__(self, x = 1280 // 2, y = 720 // 2, gun_state = IDLE_RIGHT):
        if Gun.image == None:
            Gun.image = load_image('rambro_gun_stand_walk4.png')
        self.x, self.y, self.state = x, y, gun_state
        self.frame = 0
        global gun_x, gun_y
        gun_x, gun_y = x, y

    def draw(self):
        if(self.state == IDLE_RIGHT):
            self.image.clip_draw(self.frame * w, h * 3, w, h, self.x, self.y)
        elif(self.state == IDLE_LEFT):
            self.image.clip_draw(self.frame * w, h * 2, w, h, self.x, self.y)
        elif(self.state == WALK_RIGHT):
            self.image.clip_draw(self.frame * w, h * 1, w, h, self.x, self.y)
        elif(self.state == WALK_LEFT):
            self.image.clip_draw(self.frame * w, h * 0, w, h, self.x, self.y)


    def update(self):
        global gun_x
        self.x = gun_x
        self.frame = (self.frame + 1) % 8
