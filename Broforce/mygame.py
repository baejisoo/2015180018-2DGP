import game_framework
import pico2d

import start_state
import main_state

pico2d.open_canvas(1280, 720, sync=True)
game_framework.run(main_state)
pico2d.clear_canvas()