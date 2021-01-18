import numpy as np
import mathlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import argparse
import sys

def makeGrid():
     world = np.zeros((60,60))
     world[30,30] = 1
     return (world)

def gen(world):
    new_world = np.copy(world)
    step = random.randint(1,4)

    for i in range(world.shape[0]):
        for j in range(world.shape[1]):

            if world[i,j] == 1:

                if step == 1:
                    new_world[i,j] = 2
                    new_world[i,j-1] = 2
                    new_world[i,j-2] = 1

                if step == 2:
                    new_world[i,j] = 2
                    new_world[i,j+1] = 2
                    new_world[i,j+2] = 1

                if step == 3:
                    new_world[i,j] = 2
                    new_world[i+1,j] = 2
                    new_world[i+2,j] = 1

                if step == 4:
                    new_world[i,j] = 2
                    new_world[i+1,j] = 2
                    new_world[i-2,j] = 1
                     

    return new_world        
    

def animate(world,nt):
    fig = plt.figure()
    plt.axis('off')
    ims = []
    i = 0
    
    for n in range(nt):
        ims.append(
        (plt.imshow(world, cmap='binary'),plt.title('RandomWalk')))
        world = gen(world)

        i+=1
        print(i/1000)

    print("Starting simulation")    
    walk_animation = animation.ArtistAnimation(fig, ims, interval=100,
    repeat=False, blit=True)
    plt.show()

def start():
    grid = makeGrid()   
    animate(grid, 80)

if __name__ == '__main__':
    start()
