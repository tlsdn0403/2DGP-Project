from Hamtori_Image import obstacle_image
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

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = load_image(obstacle_image.stage_1)
        self.frame=0
        if(self.x>400):
            self.dir=-1
        else:
            self.dir=1

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image.clip_draw(int(self.frame) * 96, 0, 96, 96, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x -40, self.y -40,self.x +40, self.y +40
        

    def update(self):
        self.do()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 750:
            self.dir = -1
        elif self.x < 60:
            self.dir = 1
        self.x = clamp(40, self.x, 760)

    def handle_collision(self, group, other):
        # fill here
        if group == 'hamtori:obstacle':
            print("collid")
        pass


