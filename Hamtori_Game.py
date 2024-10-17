from pico2d import *
open_canvas()

running=False


y=600//2
x=800//2
frame=0
dirx=0
diry=0


###################################클래스들##############################
class Hamtori:
    def moving_left():
        pass
    def moving_right():
        pass
    def moving_up():
        pass
    def moving_down():
        pass
    def idle():
        pass
    def running_left():
        pass
    def running_right():
        pass
    def running_up():
        pass
    def running_down():
        pass

class enemy_1:
    pass
class enemy_2:
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