from pico2d import *
import random
from Hamtori_Image import boss_image
import math
from Hamtori_Image import Hamtori_Image
from pico2d import *
from state_machine import *
import game_world
import game_framework
import Stage_2
from Walls import*
import behavior_tree
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector


# Boss Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 12.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boss Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

animation_names = ['Walk', 'Idle']


class Boss:
    images = None


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = load_image(boss_image.stage_2)
        self.dir = 0.0  # radian 값으로 방향을 표시
        self.dirx=0
        self.diry=0
        self.speed = 0.0
        self.frame=0
        self.patrol_locations = [(43, 274), (300, 274)]
        self.loc_no = 0
        self.tx, self.ty = 0, 0
        self.build_behavior_tree()
        self.state='Idle'

        if x>400 and y>300:
            self.num=4
        elif x<400 and y>300:
            self.num=3
        elif x<400 and y<300:
            self.num=2
        elif x>400 and y<300:
            self.num=1
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.bt.run()
        # fill here

    def draw(self):
        if math.cos(self.dir) < 0:
            self.image.clip_draw(int(self.frame) * 28, 30, 26, 30, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 28, 0, 26, 30, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

 

    def set_target_location(self, x=None, y=None):
        if not x or not y:
            raise ValueError('위치 지정을 해야합니다.')
        self.tx, self.ty = x, y
        return BehaviorTree.SUCCESS
        pass

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

    def move_to(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.ty, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        
    def set_random_location(self):
        if self.num==4:
            self.tx, self.ty = random.randint(440, 800 - 50), random.randint(350, 550)
        elif self.num==3:
            self.tx, self.ty = random.randint(50, 400 - 50), random.randint(350, 550)
        elif self.num==2:
            self.tx, self.ty = random.randint(50, 400 - 50), random.randint(50, 250)
        elif self.num==1:
            self.tx, self.ty = random.randint(440, 800 - 50), random.randint(50, 250)
        pass

    def is_ham_nearby(self, r):
        if self.distance_less_than(Stage_2.hamtori.x, Stage_2.hamtori.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def handle_collision(self, group, other):
        if group == 'hamtori:boss':
            if self.num==4:
                self.x,self.y = 500, 500
            elif self.num==3:
                self.x,self.y = 200, 500
            elif self.num==2<300:
                self.x,self.y = 200, 200
            elif self.num==1<300:
                self.x,self.y = 420, 240
        if group == 'boss:walls':
            left, bottom, right, top = other.get_bb()  # Get the bounding box of the wall
            if self.x < left:
                self.x = left-20
            elif self.x > right:
                self.x = right+20
            if self.y < bottom:
                self.y = bottom-20
            elif self.y > top:
                self.y = top+20


    def move_to_ham(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(Stage_2.hamtori.x, Stage_2.hamtori.y)
        if self.distance_less_than(Stage_2.hamtori.x, Stage_2.hamtori.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def get_patrol_location(self):
        self.tx, self.ty = self.patrol_locations[self.loc_no]
        self.loc_no = (self.loc_no+1) % len(self.patrol_locations)
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        a1 = Action('Move to', self.move_to)
        a2 = Action('랜덤 위치', self.set_random_location)
        SEQ_wander = Sequence('Wander', a2, a1)

        c1 = Condition('햄토리가 근처에 있는가?', self.is_ham_nearby, 4)
        a3= Action('햄토리로 이동', self.move_to_ham)
        SEQ_chace= Sequence('chace', c1, a3)
        root = SEQ_chase_or_wander= Selector('추적 혹은 배회',SEQ_chace, SEQ_wander)
        self.bt = BehaviorTree(root)
        pass


