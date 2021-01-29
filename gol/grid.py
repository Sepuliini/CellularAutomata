import numpy as np
import random
import mathlib


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
        beacon = [[1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1]]    

        #self.world[1:5, 1:5] = beacon 
        self.world[int(self.cols/2):int(self.cols/2)+4, int(self.cols/2):int(self.cols/2)+4] = beacon
        return self.world   

    def glider(self):
        glider = [[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0]]
        #self.world[1:5, 1:5] = glider
        self.world[int(self.cols/2):int(self.cols/2)+4, int(self.cols/2):int(self.cols/2)+4] = glider
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
        return self.world

    #needs rule 90
    #to-do
    def Sierpinksi(self):
        triangle = [[0,1,1,0],
                    [0,1,1,0]]   
        self.world[ int(self.cols/2): int((self.cols/2))+2, int(self.rows/2): int((self.rows/2))+4] = triangle            
        #self.world[1:5,1:2]
        return(self.world)