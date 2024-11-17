from Hamtori_Image import walls_image
import game_framework

from pico2d import*

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Walls:
    def __init__(self, x, y,stage):
        self.stage= stage
        self.x = x
        self.y = y
        if stage==1:
            self.walls_image = load_image(walls_image.stage_1_walls)
        elif stage==2:
            self.walls_image = load_image(walls_image.stage_2_walls)

    def draw(self):
        self.walls_image.draw(self.x, self.y,40,40)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x -20, self.y -20,self.x +20, self.y +20


    def update(self):
        pass

    def handle_collision(self, group, other):
        # fill here
        if group == 'hamtori:wall':
            print("collid")
        pass
