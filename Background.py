
from Hamtori_Image import Backgorund_image
from pico2d import load_image,load_music


class Background:
    def __init__(self,stage):
        self.stage=stage
        self.x, self.y = 400, 300  # 화면 중앙에 배경 위치
        if self.stage==1:
            self.background_image = load_image(Backgorund_image.stage_1)
            self.bgm= load_music('ham_bgm_1.mp3')
            self.bgm.set_volume(32)
            self.bgm.repeat_play()
        elif self.stage==2:
            self.background_image= load_image(Backgorund_image.stage_2)
            self.bgm= load_music('ham_bgm_2.mp3')
            self.bgm.set_volume(32)
            self.bgm.repeat_play()     
        
    def draw(self):
        self.background_image.draw(self.x, self.y, 800, 600)  # 배경을 화면에 그림

    def update(self):
        pass