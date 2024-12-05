from Background import Background
import game_framework
import game_world
from pico2d import *
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global hamtori, background, walls
    background = Background(5)  # 배경 객체 생성
    game_world.add_object(background,0)

    
    


def finish():
    game_world.clear()
    game_world.clear_collision_pairs()
    pass

def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass

def resume():
    pass