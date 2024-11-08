from Hamtori_Image import Hamtori_Image
from pico2d import *


class Hamtori:
    def __init__(self):
        self.x, self.y = 200, 200  # 화면 왼아래에서 시작
        self.frame = 0
        self.ham_image_judge = 0  # 초기 이미지 설정
        self.ham_image = Hamtori_Image.ham_idle  # 기본 이미지

    def update(self):
        self.frame = (self.frame + 1) % 4  # 애니메이션 프레임 업데이트

    def draw(self):
        # 방향에 따라 이미지를 선택
        if self.ham_image_judge == 1:  # 위로 이동
            self.ham_image = Hamtori_Image.ham_up
            self.ham_image.clip_draw(self.frame * 37, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 2:  # 아래로 이동
            self.ham_image = Hamtori_Image.ham_down
            self.ham_image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y)
        elif self.ham_image_judge == 3:  # 좌 이동
            self.ham_image = Hamtori_Image.ham_left_right
            self.ham_image.clip_draw(self.frame * 37 - 3, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 4:  # 우 이동
            self.ham_image = Hamtori_Image.ham_left_right
            self.ham_image.clip_draw(144 + self.frame * 37, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 0:
            self.ham_image = Hamtori_Image.ham_idle
            self.ham_image.clip_draw(self.frame * 38, 0, 38, 40, self.x, self.y)

    def move_left(self, walls):
        if not walls.check_collision(self.x - 5, self.y):  # 왼쪽으로 이동 전 충돌 검사
            self.ham_image_judge = 3  # 왼쪽으로 이동하는 이미지로 설정
            self.x -= 5  # 왼쪽으로 이동

    def move_right(self, walls):
        if not walls.check_collision(self.x + 5, self.y):  # 오른쪽으로 이동 전 충돌 검사
            self.ham_image_judge = 4  # 오른쪽으로 이동하는 이미지로 설정
            self.x += 5  # 오른쪽으로 이동

    def move_up(self, walls):
        if not walls.check_collision(self.x, self.y + 5):  # 위로 이동 전 충돌 검사
            self.ham_image_judge = 1  # 위로 이동하는 이미지로 설정
            self.y += 5  # 위로 이동

    def move_down(self, walls):
        if not walls.check_collision(self.x, self.y - 5):  # 아래로 이동 전 충돌 검사
            self.ham_image_judge = 2  # 아래로 이동하는 이미지로 설정
            self.y -= 5  # 아래로 이동

    def idle(self):
        self.ham_image_judge = 0