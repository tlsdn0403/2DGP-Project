################################### 클래스들 ##############################
from pico2d import load_image
from pico2d import *
open_canvas()

class Hamtori_Image:
    ham_up = load_image('Hams_Walking_Up.png')
    ham_down = load_image('Hams_Walking_Down.png')
    ham_left_right = load_image('Hams_walking_left_right.png')
    ham_idle = load_image('Hams_idle1.png')

class walls_image:
    stage_1_walls = 'greenwall.jpg'
    stage_2_walls = 'blackwall.jpg'
    stage_3_walls= 'redwall.jpg'

class Backgorund_image:
    stage_1 = 'ham_background.jpg'
    stage_2 = 'ham_background_2.jpg'
    stage_5= 'Ending.png'

class obstacle_image:
    stage_1= 'stone_2.png'

class boss_image:
    stage_2 ='boss.png'
class bijou_image:
    stage_4='bijou.png'