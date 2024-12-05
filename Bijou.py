from Hamtori_Image import bijou_image
import game_framework

from pico2d import*


PIXEL_PER_METER = (10.0 / 0.3) 
RUN_SPEED_KMPH = 30.0 
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Bijou:
    def __init__(self, x, y,stage):
        self.x = x
        self.y = y
        self.image = load_image(bijou_image.stage_4)
        self.frame=0
        self.stage= stage
        

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    

    def update(self):
        self.do()
       