from pico2d import *
from Background import Background
from Walls import Walls
from hamtori import Hamtori
from obstacle import Obstacle
import game_framework
import game_world
import Stage_2

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif hamtori.x>=600 and hamtori.y>=600:
            game_framework.change_mode(Stage_2) 
        else:
            hamtori.handle_event(event)
        

def init():
    global hamtori, background, walls
    hamtori = Hamtori(66,66,1)  # 햄토리 객체 생성
    game_world.add_object(hamtori,1)
    background = Background(1)  # 배경 객체 생성
    game_world.add_object(background,0)
    

    wall_positions = []
    for x in range(20, 800, 40):  # Bottom
        wall_positions.append((x, 20))
    for y in range(60, 600, 40):  # Right
        wall_positions.append((780, y))

    for x in range(60, 360, 40):  # Middle_left
        wall_positions.append((x, 300))
    for x in range(60, 360, 40):  # Middle_left
        wall_positions.append((x, 340))

    for x in range(460, 780, 40):  # Middle_Right
        wall_positions.append((x, 300))
    for x in range(460, 780, 40):  # Middle_Right
        wall_positions.append((x, 340))

    for y in range(60, 600, 40):  # Left
        wall_positions.append((20, y))
    for x in range(20, 660, 40):  # Top
        wall_positions.append((x, 580))
    
    # WallSegment 객체 리스트로 관리
    walls = [Walls(x, y,stage=1) for (x, y) in wall_positions]


    game_world.add_collision_pair('hamtori:wall',hamtori, None)  #햄토리를 한 번만 넣도록 만듦
    # 벽 객체를 game_world에 추가
    for wall in walls:
        game_world.add_object(wall, 1)
        # Hamtori와 각 WallSegment의 충돌 페어 추가
        game_world.add_collision_pair('hamtori:wall', None, wall)

    obstacle_positions = []
    obstacle_positions.append((70,240))
    obstacle_positions.append((720,160))

    obstacle_positions.append((70,400))
    obstacle_positions.append((720,520))

    obstacles = [Obstacle(x, y,1) for (x, y) in obstacle_positions]
    game_world.add_collision_pair('hamtori:obstacle',hamtori, None)  #햄토리를 한 번만 넣도록 만듦
    for obstacle in obstacles:
        game_world.add_object(obstacle, 1)
        game_world.add_collision_pair('hamtori:obstacle',None, obstacle)  #햄토리를 한 번만 넣도록 만듦

    
    


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


