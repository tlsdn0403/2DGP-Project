from Hamtori_Image import walls_image
import game_framework

from pico2d import*


class Walls:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls_image = load_image(walls_image.stage_1_walls)

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
        if group == 'boy:zombie':
            game_framework.quit()
        pass
