from Hamtori_Image import walls_image


from pico2d import*


class Walls:
    def __init__(self):
        self.walls_image = load_image(walls_image.stage_1_walls)
        #벽 위치
        self.positions = []
        for x in range(20, 800, 40):  # Bottom
            self.positions.append((x, 20))
        for y in range(60, 600, 40):  # Right
            self.positions.append((780, y))
        for y in range(60, 600, 40):  # Left
            self.positions.append((20, y))
        for x in range(20, 660, 40):  # Top
            self.positions.append((x, 580))

    def draw(self):
        
        for (x, y) in self.positions:
            self.walls_image.draw(x, y, 40, 40)
            #충돌처리 구역
            draw_rectangle(*self.get_bb(x, y))

    def get_bb(self, x, y):
        return x - 20, y - 20, x + 20, y + 20

    def check_collision(self, x, y):
        for (wall_x, wall_y) in self.positions:
            if abs(x - wall_x) < 40 and abs(y - wall_y) < 40:
                return True 
        return False  

    def update(self):
        pass
