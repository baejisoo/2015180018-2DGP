import pickle

# 게임 월드에 담겨있는 모든 객체들을 담고 있는 리스트.
# Drawing Layer 에 따라서 분류.
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: player
# layer 3: bullet
# layer 4: mook
# layer 5: gun, effect
# layer 6: ui
objects = [[],[],[],[],[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def save():
    # fill here
    with open('game.sav', 'wb') as f:
        pickle.dump(objects, f)

    pass

def load():
    # fill here
    global objects
    with open('game.sav', 'rb') as f:
        objects = pickle.load(f)
    pass
