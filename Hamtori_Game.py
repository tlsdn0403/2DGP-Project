from pico2d import *
open_canvas()

running=True


y=600//2
x=800//2
frame=0
dirx=0
diry=0


###################################클래스들##############################
class Hamtori_Image:
    ham_up=('Hams_Walking_Up.png')
    ham_down=('Hams_Walking_Down.png')
    ham_left_rigth=('Hams_walking_left_right.png')



class Hamtori:
    def __init__(self, ham_image_judge=1):
        self.x, self.y = 20, 20
        self.frame = 0
        if ham_image_judge == 1:
            self.ham_image = load_image(Hamtori_Image.ham_up)
        elif ham_image_judge == 2:
            self.ham_image = load_image(Hamtori_Image.ham_down)
        elif ham_image_judge == 3:
            self.ham_image = load_image(Hamtori_Image.ham_left_right)    
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.ham_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def moving_left(ham_image_judge):
        ham_image_judge=3
        
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
    wall_image=None
    if wall_image==None:
        wall_image=('wall.png')
    pass
class obstacle:
    pass
class Events:
    global running
    def escape_event():
        running=False
####################################함수들##############################



def handle_events():
    global dirx, diry, running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dirx = -1
            elif event.key == SDLK_RIGHT:
                dirx = 1
            elif event.key == SDLK_UP:
                diry = 1
            elif event.key == SDLK_DOWN:
                diry = -1
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_LEFT, SDLK_RIGHT):
                dirx = 0
            elif event.key in (SDLK_UP, SDLK_DOWN):
                diry = 0


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