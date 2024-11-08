from pico2d import *
from Background import Background
from Walls import Walls
from hamtori import Hamtori
from game_framework import*

running = True
dirx = 0
diry = 0



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
def update():
    game_world.update()
def init():
    global hamtori, background, walls
    hamtori = Hamtori()  # 햄토리 객체 생성
    background = Background()  # 배경 객체 생성
    walls = Walls()

################################### 게임 실행 ###################################
init()

while running:
    handle_events()  # 입력 이벤트 처리
    update_world()  # 캐릭터 이동 및 상태 업데이트
    render_world()  # 화면에 그리기
    delay(0.05)
close_canvas()
