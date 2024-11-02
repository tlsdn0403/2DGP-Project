from pico2d import *

open_canvas()
running = True
y = 600 // 2
x = 800 // 2
frame = 0
dirx = 0
diry = 0
ham_image_judge = 1  # 초기 이미지 방향 설정

################################### 클래스들 ##############################
class Hamtori_Image:
    ham_up = load_image('Hams_Walking_Up.png')
    ham_down = load_image('Hams_Walking_Down.png')
    ham_left_right = load_image('Hams_walking_left_right.png')
    ham_idle = load_image('Hams_idle1.png')

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

##########################배경 클래스#######################
class Backgorund_image:
    stage_1 = 'ham_background.jpg'

class Background:
    def __init__(self):
        self.x, self.y = 400, 300  # 화면 중앙에 배경 위치
        self.background_image = load_image(Backgorund_image.stage_1)

    def draw(self):
        self.background_image.draw(self.x, self.y, 800, 600)  # 배경을 화면에 그림

class walls_image:
    stage_1_walls = 'greenwall.jpg'

class Walls:
    def __init__(self):
        self.walls_image = load_image(walls_image.stage_1_walls)
        # 벽의 위치들을 리스트로 저장
        self.positions = [
            (400, 300),
            (20, 20),
            (60, 20),
            (100, 20),  # 추가하고 싶은 좌표를 계속 추가
        ]

    def draw(self):
        # 위치 리스트에 있는 각 좌표에 벽을 그림
        for (x, y) in self.positions:
            self.walls_image.draw(x, y, 40, 40)

    def check_collision(self, x, y):
        # 각 벽 위치와 햄토리의 좌표를 비교하여 충돌 확인
        for (wall_x, wall_y) in self.positions:
            # 벽의 크기와 햄토리의 크기를 고려하여 충돌 여부를 판단
            if abs(x - wall_x) < 40 and abs(y - wall_y) < 40:
                return True  # 충돌이 발생하면 True 반환
        return False  # 충돌이 없으면 False 반환

#################################### 함수들 ##############################
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
    global dirx, diry
    if dirx == -1:
        hamtori.move_left(walls)
    elif dirx == 1:
        hamtori.move_right(walls)
    if diry == 1:
        hamtori.move_up(walls)
    elif diry == -1:
        hamtori.move_down(walls)
    elif dirx == 0 and diry == 0:
        hamtori.idle()
    hamtori.update()  # 애니메이션 프레임 업데이트

def render_world():
    clear_canvas()  # 화면을 지움
    background.draw()  # 배경 그리기
    walls.draw()  # 장애물 그리기
    hamtori.draw()  # 햄토리 그리기
    update_canvas()  # 화면 업데이트

def reset_world():
    global hamtori, background, walls
    hamtori = Hamtori()  # 햄토리 객체 생성
    background = Background()  # 배경 객체 생성
    walls = Walls()

################################### 게임 실행 ###################################
reset_world()

while running:
    handle_events()  # 입력 이벤트 처리
    update_world()  # 캐릭터 이동 및 상태 업데이트
    render_world()  # 화면에 그리기
    delay(0.05)
close_canvas()
