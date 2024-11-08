from Hamtori_Image import walls_image


from pico2d import load_image


class Walls:
    def __init__(self):
        self.walls_image = load_image(walls_image.stage_1_walls)
        # 벽의 위치들을 리스트로 저장
        self.positions =[]
        for x in range(20, 800, 40): ##아래
            self.positions.append((x, 20))


        for y in range(60, 600, 40): ##오른쪽
            self.positions.append((780, y))

        for y in range(60, 600, 40): ##왼쪽
            self.positions.append((20, y))

        for x in range(20, 660, 40): ##위
            self.positions.append((x, 580))

    def draw(self):
        # 위치 리스트에 있는 각 좌표에 벽을 그림
        for (x, y) in self.positions:
            self.walls_image.draw(x, y, 40, 40)

    def check_collision(self, x, y):
        # 각 벽 위치와 햄토리의 좌표를 비교하여 충돌 확인
        for (wall_x, wall_y) in self.positions:
            # 벽의 크기와 햄토리의 크기를 고려하여 충돌 여부를 판단
            if abs(x - wall_x) < 40 and abs(y - wall_y) < 40:
                return True  # 충돌이 발생하면 True 반환
        return False  # 충돌이 없으면 False 반환