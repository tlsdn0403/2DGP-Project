from pico2d import *
from Background import Background
from Walls import Walls
from hamtori import Hamtori
from obstacle import Obstacle
import game_framework
import game_world
import Stage_1

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif hamtori.x<=0 and hamtori.y>=500:
            game_framework.change_mode(Stage_1) 
        else:
            hamtori.handle_event(event)
        

def init():
    from boss import Boss
    global hamtori, background, walls
    hamtori = Hamtori(720,65,3)  # 햄토리 객체 생성
    game_world.add_object(hamtori,1)
    background = Background(2)  # 배경 객체 생성
    game_world.add_object(background,0)
    

    wall_positions = []
    for x in range(20, 800, 40):  # Bottom
        wall_positions.append((x, 20))
    for y in range(60, 600, 40):  # Right
        wall_positions.append((780, y))


    for y in range(60, 500, 40):  # Left
        wall_positions.append((20, y))
    for x in range(20, 800, 40):  # Top
        wall_positions.append((x, 580))

    for x in range(140, 800, 40):  #1차 벽
        wall_positions.append((x, 200))
    for x in range(140,740,120):
         wall_positions.append((x, 60))


    for x in range(60, 700, 40):  #2차 벽
        wall_positions.append((x, 380))
    for x in range(140,740,120):
        wall_positions.append((x, 340))

    # WallSegment 객체 리스트로 관리
    walls = [Walls(x, y,stage=3) for (x, y) in wall_positions]


    game_world.add_collision_pair('hamtori:wall',hamtori, None)  #햄토리를 한 번만 넣도록 만듦
    # 벽 객체를 game_world에 추가
    for wall in walls:
        game_world.add_object(wall, 1)
        # Hamtori와 각 WallSegment의 충돌 페어 추가
        game_world.add_collision_pair('hamtori:wall', None, wall)

    obstacle_positions = []

    obstacle_positions.append((670,260))
    obstacle_positions.append((70,140))
    obstacle_positions.append((70,440))


    obstacles = [Obstacle(x, y,3) for (x, y) in obstacle_positions]
    game_world.add_collision_pair('hamtori:obstacle',hamtori, None)  #햄토리를 한 번만 넣도록 만듦
    for obstacle in obstacles:
        game_world.add_object(obstacle, 1)
        game_world.add_collision_pair('hamtori:obstacle',None, obstacle)  #햄토리를 한 번만 넣도록 만듦

    boss_positions = []
    boss_positions.append((66,220))
    boss_positions.append((720,420))
    boss_positions.append((400,560))

 
    Enemys=[Boss(x,y,3) for (x,y) in boss_positions ]
    game_world.add_collision_pair('hamtori:boss',hamtori,None)
    for Enemy in Enemys:
        game_world.add_object(Enemy ,1)
        game_world.add_collision_pair ('hamtori:boss',None,Enemy)

    for Enemy in Enemys:
        game_world.add_collision_pair ('boss:walls',Enemy,None)
    for wall in walls:
        game_world.add_collision_pair ('boss:walls',None,wall)
    
    for Enemy in Enemys:
        game_world.add_collision_pair ('boss:obstacle',Enemy,None)
    for obstacle in obstacles:
        game_world.add_collision_pair ('boss:obstacle',None,obstacle)
    


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


