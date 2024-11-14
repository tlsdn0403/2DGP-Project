from Hamtori_Image import obstacle_image
import game_framework

from pico2d import*

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = load_image(obstacle_image.stage_1)

    def draw(self):
        self.image.draw(self.x, self.y,40,40)
        

    def update(self):
        pass

