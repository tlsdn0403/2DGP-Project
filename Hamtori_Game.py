from pico2d import *
open_canvas()
running=False
###################################클래스들##############################
class Hamtori:
    pass
class Background:
    pass
class wall:
    pass
class obstacle:
    pass

####################################함수들##############################
def handle_events():
    pass
def update_world():
    pass
def render_world():
    pass
def reset_world(): #초기화 함수
    pass

def stage_1():  #1스테이지
    pass
def stage_2():  #2스테이지
    pass
def stage_3():  #3스테이지
    pass
def stage_4():  #4스테이지
    pass

open_canvas()

# initialization code 객체를 초기에 창조함
reset_world()
while running:
    handle_events() #입력 이벤트 처리
    update_world()
    render_world()
    delay(0.05) 

close_canvas()