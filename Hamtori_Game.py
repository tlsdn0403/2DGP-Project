from pico2d import *
from Background import Background
from Walls import Walls
from hamtori import Hamtori
import game_framework
import game_world

dirx = 0
diry = 0



#################################### 함수들 ##############################
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            hamtori.handle_event(event)
        


def update():
    game_world.update()
def init():
    global hamtori, background, walls
    hamtori = Hamtori()  # 햄토리 객체 생성
    game_world.add_object(hamtori,1)
    background = Background()  # 배경 객체 생성
    game_world.add_object(background,0)

    walls = Walls()
    game_world.add_object(walls)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass

def resume():
    pass

