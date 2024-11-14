from Hamtori_Image import obstacle_image
import game_framework

from pico2d import*



TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = load_image(obstacle_image.stage_1)
        self.frame=0

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image.draw(self.x, self.y,40,40)
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 178, self.x, self.y)
        

    def update(self):
        self.do()

