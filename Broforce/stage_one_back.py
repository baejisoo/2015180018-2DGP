from pico2d import *
from TileMap import load_tile_map

class Stage_one_back:
    def __init__(self):
        self.image = load_image('image/StageOne_Back1.png')
       #self.bgm = load_wav('Stage1_BGM.wav')
       #self.bgm.set_volume(10)
       #self.bgm.repeat_play()
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.left = clamp(0, int(self.set_center_object.x) -
                          self.canvas_width // 2, self.w - self.canvas_width)
        self.bottom = clamp(0, int(self.set_center_object.y) -
                            self.canvas_height // 2, self.h - self.canvas_height)

    def draw(self):
        self.image.clip_draw_to_origin(self.left, self.bottom, self.canvas_width,
                                       self.canvas_height, 0, 0)

    def set_center_object(self, boy):
        self.set_center_object = boy

class FixedTileBackground:

    def __init__(self):
        self.image = load_image('image/StageOne_Back1.png')
        #self.image_test = load_image('broforce_tiles_e100ff.png')
        # fill here
        self.tile_map = load_tile_map('broforce_tilemap_e100ff.json')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.tile_map.width * self.tile_map.tilewidth
        self.h = self.tile_map.height * self.tile_map.tileheight


    def set_center_object(self, boy):
        self.center_object = boy
        self.max_window_left = self.w - self.canvas_width
        self.max_window_bottom = self.h - self.canvas_height

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)
        self.tile_map.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)
        #self.image_test.draw(200, 200)

        pass

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.max_window_left)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.max_window_bottom)


