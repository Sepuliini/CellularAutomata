import numpy as np
import mathlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import argparse
import sys

class MakeGrid():

    def __init__ (self, cols, rows, gridtype):
        self.cols = cols
        self.rows = rows
        self.world = np.zeros((self.cols, self.rows))

    def randomGrid(self):
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self.world[i,j] = random.randint(0,1)    
        return self.world  

    def beacon(self):
        beacon = [[1, 1, 0, 0],[1, 1, 0, 0],[0, 0, 1, 1],[0, 0, 1, 1]]    

        self.world[1:5, 1:5] = beacon  
        return self.world   

    def glider(self):
        glider = [[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0]]
        self.world[1:5, 1:5] = glider
        return self.world

    def gliderGun(self):
        gliderGun =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                      [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                      [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.world[1:10,1:37] = gliderGun
        return(self.world)

def neighbours(i, j, world):
    neighbours = 0
    neighbours = np.sum(world[i - 1:i + 2, j - 1:j + 2])
    neighbours -= world[i,j]

    if world[i, j] == 1:
        if neighbours < 2 or neighbours > 3:
            return 0

    elif world[i, j] == 0:
        if neighbours == 3:
            return 1
    return world[i,j]

def gen(world):
    new_world = np.copy(world)
    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            new_world[i, j] = neighbours(i, j, world)
    return new_world

def animate(world,nt,rep):
    fig = plt.figure()
    plt.axis('on')
    ims = []
    i = 0
    boolrep = ""

    #needs fix
    if rep=="true" or rep=="yes":
        boolrep = bool(True)

    elif rep =="false" or rep=="no":
        boolrep = bool(False)

    for n in range(nt):
        ims.append((plt.imshow(world, cmap='binary'),plt.title('Game_Of_Life')))
        world = gen(world)
        i+=1

    print("Starting simulation")    
    #interval = speed
    #takes a long time to load if the grid is large (more than 100x100)
    gol_animation = animation.ArtistAnimation(fig, ims, interval=25,
    repeat=boolrep, blit=True)
    plt.show()

def start():
    cols = int(input("How many columns? "))
    rows = int(input("How many rows? "))
    gridtype = int(input("Select gridtype: 0:, 1:, 2:, 3: "))
    toistot = int(input("How many times? "))
    uudelleen = input("Repeat simulation? ")

    print('{} , {} , {} , {} , {}'.format(cols, rows, gridtype, toistot, uudelleen))

    world = np.zeros((cols,rows)) 
    gridi = MakeGrid(cols, rows, gridtype)

    if gridtype == 0:
        world = gridi.randomGrid()
    elif gridtype == 1:
        world = gridi.beacon()
    elif gridtype== 2:
        world = gridi.glider()
    elif gridtype == 3:
        world = gridi.gliderGun()
    animate(world,toistot,uudelleen)

if __name__ == '__main__':
    start()

   # no parser for now
   # parser = argparse.ArgumentParser(description="Conway's Game of Life")
   # parser.add_argument('--grid-size cols', dest='cols', required=True)
   # parser.add_argument('--grid-size rows', dest='rows', required=True)
   # parser.add_argument('--gridtype', dest='gridtype', required=True)
   # parser.add_argument('--nt', dest='rows', required=True)

    # cols = int(sys.argv[1])
    # rows = int(sys.argv[2])
    # gridtype = int(sys.argv[3])
    # nt = int(sys.argv[4])
