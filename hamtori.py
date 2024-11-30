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


class RunUp:
    @staticmethod
    def enter(self, e):
        self.ham_image_judge, self.diry, self.dirx = 1, +1, 0

    @staticmethod
    def exit(self, e):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.y += self.diry * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.ham_image = Hamtori_Image.ham_up
        self.ham_image.clip_draw(int(self.frame) * 37, 0, 37, 40, self.x, self.y)


class RunDown:
    @staticmethod
    def enter(self, e):
        self.ham_image_judge, self.diry, self.dirx = 2, -1, 0

    @staticmethod
    def exit(self, e):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.y += self.diry * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.ham_image = Hamtori_Image.ham_down
        self.ham_image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y)


class RunLeft:
    @staticmethod
    def enter(self, e):
        self.ham_image_judge, self.dirx, self.diry = 3, -1, 0

    @staticmethod
    def exit(self, e):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dirx * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(int(self.frame) * 37 - 3, 0, 37, 40, self.x, self.y)


class RunRight:
    @staticmethod
    def enter(self, e):
        self.ham_image_judge, self.dirx, self.diry = 4, +1, 0

    @staticmethod
    def exit(self, e):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dirx * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(144 + int(self.frame) * 37, 0, 37, 40, self.x, self.y)

class RunRightUp:
    @staticmethod
    def enter(self, e):
        self.action = 1
        self.speed = RUN_SPEED_PPS
        self.dir = math.pi / 4.0

    @staticmethod
    def exit(self, e):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(144 + int(self.frame) * 37, 0, 37, 40, self.x, self.y)

class RunRightDown:
    @staticmethod
    def enter(self, e):
        self.action = 1
        self.speed = RUN_SPEED_PPS
        self.dir = -math.pi / 4.0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(144 + int(self.frame) * 37, 0, 37, 40, self.x, self.y)

class RunLeftUp:
    @staticmethod
    def enter(self, e):
        self.action = 0
        self.speed = RUN_SPEED_PPS
        self.dir = math.pi * 3.0 / 4.0

    @staticmethod
    def exit(self, e):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(int(self.frame) * 37 - 3, 0, 37, 40, self.x, self.y)


class RunLeftDown:
    @staticmethod
    def enter(boy, e):
        boy.action = 0
        boy.speed = RUN_SPEED_PPS
        boy.dir = - math.pi * 3.0 / 4.0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.ham_image = Hamtori_Image.ham_left_right
        self.ham_image.clip_draw(int(self.frame) * 37 - 3, 0, 37, 40, self.x, self.y)

class Hamtori:
    def __init__(self,x,y):
        self.hp=3
        self.x, self.y = x, y  # 화면 왼아래에서 시작
        self.frame = 0
        self.dirx=0
        self.diry=0
        self.ham_image_judge = 0  # 초기 이미지 설정
        self.ham_image = Hamtori_Image.ham_idle  # 기본 이미지
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
    {
        Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, upkey_down: RunUp,
                   downkey_down: RunDown, downkey_up: RunUp},
            RunRight: {right_up: Idle, left_down: Idle, upkey_down: RunRightUp, upkey_up: RunRightDown,
                       downkey_down: RunRightDown, downkey_up: RunRightUp},
            RunRightUp: {upkey_up: RunRight, right_up: RunUp, left_down: RunUp, downkey_down: RunRight},
            RunUp: {upkey_up: Idle, left_down: RunLeftUp, downkey_down: Idle, right_down: RunRightUp,
                    left_up: RunRightUp, right_up: RunLeftUp},
            RunLeftUp: {right_down: RunUp, downkey_down: RunLeft, left_up: RunUp, upkey_up: RunLeft},
            RunLeft: {left_up: Idle, upkey_down: RunLeftUp, right_down: Idle, downkey_down: RunLeftDown,
                      upkey_up: RunLeftDown, downkey_up: RunLeftUp},
            RunLeftDown: {left_up: RunDown, downkey_up: RunLeft, upkey_down: RunLeft, right_down: RunDown},
            RunDown: {downkey_up: Idle, left_down: RunLeftDown, upkey_down: Idle, right_down: RunRightDown,
                      left_up: RunRightDown, right_up: RunLeftDown},
            RunRightDown: {right_up: RunDown, downkey_up: RunRight, left_down: RunDown, upkey_down: RunRight}
    }
)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()# 방향에 따라 이미지를 선택
        #draw_rectangle(*self.get_bb())
        
         

    def get_bb(self):
        return self.x -18, self.y-20, self.x +18, self.y+18
        pass


    def handle_collision(self, group, other):
        if group == 'hamtori:wall':
            if self.dirx > 0 and self.x <= other.x: 
                self.x -= self.dirx * RUN_SPEED_PPS * game_framework.frame_time
                self.dirx = 0
                
            elif self.dirx < 0 and self.x >= other.x: 
                self.x -= self.dirx * RUN_SPEED_PPS * game_framework.frame_time
                self.dirx = 0

            elif self.diry > 0 and self.y <= other.y:
                self.y -= self.diry * RUN_SPEED_PPS * game_framework.frame_time 
                self.diry = 0

            elif self.diry < 0 and self.y >= other.y:  
                self.y -= self.diry * RUN_SPEED_PPS * game_framework.frame_time 
                self.diry = 0
            else:
                self.x -= math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
                self.y -= math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time
                print("collid")


            print("Hamtori collided with a wall.")
        if group == 'hamtori:obstacle':
            self.x=65
            self.y=65
            print("Hamtori collided with a obs.")

        if group == 'hamtori:boss':
            self.x=720
            self.y=65
            print("Hamtori collided with a boss.")
        