
from Hamtori_Image import Backgorund_image
from pico2d import load_image


class Background:
    def __init__(self):
        self.x, self.y = 400, 300  # 화면 중앙에 배경 위치
        self.background_image = load_image(Backgorund_image.stage_1)

    def draw(self):
        self.background_image.draw(self.x, self.y, 800, 600)  # 배경을 화면에 그림

    def update(self):
        pass