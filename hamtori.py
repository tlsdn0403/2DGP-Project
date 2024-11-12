from Hamtori_Image import Hamtori_Image
from pico2d import *
from state_machine import *
import game_world
import game_framework
from Walls import*
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Idle:
    def enter(self, e):
        if start_event(e):
            self.ham_image_judge = 3


    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.ham_image = Hamtori_Image.ham_idle
        self.ham_image.clip_draw(int(self.frame) * 38, 0, 38, 40, self.x, self.y)
    def exit(self,e):
        pass


class Run:
    @staticmethod
    def enter(self, e):
        if right_down(e): # 오른쪽으로 RUN
            self.ham_image_judge, self.dirx,self.diry = 4, +1,0
        elif left_down(e): # 왼쪽으로 RUN           
            self.ham_image_judge,self.dirx,self.diry=3,-1,0
        elif down_down(e):
            self.ham_image_judge, self.diry,self.dirx = 2, -1,0
        elif up_down(e):  
            self.ham_image_judge, self.diry,self.dirx = 1, +1,0
    def exit(hamtori,e):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        self.x += self.dirx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.diry * RUN_SPEED_PPS * game_framework.frame_time
        
    def draw(self):
        if self.ham_image_judge == 1:  # 위로 이동
            self.ham_image = Hamtori_Image.ham_up
            self.ham_image.clip_draw(int(self.frame) * 37, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 2:  # 아래로 이동
            self.ham_image = Hamtori_Image.ham_down
            self.ham_image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y)
        elif self.ham_image_judge == 3:  # 좌 이동
            self.ham_image = Hamtori_Image.ham_left_right
            self.ham_image.clip_draw(int(self.frame) * 37 - 3, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 4:  # 우 이동
            self.ham_image = Hamtori_Image.ham_left_right
            self.ham_image.clip_draw(144 + int(self.frame) * 37, 0, 37, 40, self.x, self.y)
        elif self.ham_image_judge == 0:
            self.ham_image = Hamtori_Image.ham_idle
            self.ham_image.clip_draw(int(self.frame) * 38, 0, 38, 40, self.x, self.y)


class Hamtori:
    def __init__(self):
        self.x, self.y = 200, 200  # 화면 왼아래에서 시작
        self.frame = 0
        self.dirx=0
        self.diry=0
        self.ham_image_judge = 0  # 초기 이미지 설정
        self.ham_image = Hamtori_Image.ham_idle  # 기본 이미지
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run,down_up:Run, down_down:Run, up_down:Run , up_up:Run , space_down: Idle},
                Run: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle,down_up:Idle, down_down:Run, up_down:Run , up_up:Idle , space_down: Idle}
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        # 방향에 따라 이미지를 선택
         

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