import numpy as np
import mathlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

def makeGrid(cols,rows):
    world = np.zeros((cols,rows))
    for i in range(0,cols):
        for j in range(0,rows):
            world[i][j] = random.randint(0,1)
    return(world)

def neighbours(x, y, world):
    neighbours = 0
    neighbours = np.sum(world[x - 1:x + 2, y - 1:y + 2])
    neighbours -= world[x,y]

    if world[x, y] == 1:
        if neighbours < 2 or neighbours > 3:
            return 0
    elif world[x, y] == 0:
        if neighbours == 3:
            return 1
    return world[x,y]

def gen(world):
    new_world = np.copy(world)
    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            new_world[i, j] = neighbours(i, j, world)
    return new_world

def animate(world):
    fig = plt.figure()
    plt.axis('on')
    ims = []
    i = 1
    rotation = 200

    for i in range(rotation):
        ims.append((plt.imshow(world, cmap='binary'),))
        world = gen(world)
        i+1
        print(i,'/',rotation)
    im_ani = animation.ArtistAnimation(fig, ims, interval=10,
    repeat_delay=10000, blit=True)

    plt.show()


if __name__ == '__main__':
    cols = 60
    rows = 60
    world = makeGrid(cols,rows)
    animate(world)
