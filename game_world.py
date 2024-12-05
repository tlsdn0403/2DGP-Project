world = [[] for _ in range(4)]


collision_pairs={}#빈 딕셔너리 

def add_collision_pair(group,a,b):
    if group not in collision_pairs:
        #print(f'NEW group {group} added......')
        collision_pairs[group]=[ [] , [] ]
    if a:
        #print(f'group {group} : {a} added......')
        collision_pairs[group][0].append(a)
    if b:
        #print(f'group {group} : {b} added......')
        collision_pairs[group][1].append(b)


def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def collide(a, b):

    al,ab,ar,at=a.get_bb()
    bl,bb,br,bt= b.get_bb()


    if ar<bl: return False
    if al>br: return False
    if at<bb: return False
    if ab>bt : return False

    return True
    pass


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) #collision pairs 에서 o를 삭제
            del o  #글로벌 변수 같은거는 메모리에서 객체 자체를 삭제해줘야
            return

    raise ValueError('Cannot delete non existing object')
def clear():
    for layer in world:
        layer.clear()


def handle_collisions():
    # 게임 월드에 등록된 충돌 정보를 바탕으로 실제 충돌 검사를 수행
    for group,pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    #print(f'{group} collide')
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)
    return None 


def clear_collision_pairs():
    """충돌 페어를 모두 제거"""
    global collision_pairs
    collision_pairs.clear()