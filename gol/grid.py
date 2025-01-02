import numpy as np
import random
#import mathlib  

class MakeGrid():
    """
    A class that generates different initial configurations (grids) for
    Conway's Game of Life cellular automata.

    Attributes
    ----------
    cols : int
        Number of columns in the grid.
    rows : int
        Number of rows in the grid.
    world : numpy.ndarray
        2D NumPy array representing the grid. 
        Each cell is initially 0 (dead).
    """

    def __init__(self, cols, rows, gridtype):
        """
        Initialize the MakeGrid object with given dimensions and type of pattern.

        Parameters
        ----------
        cols : int
            The number of columns in the grid.
        rows : int
            The number of rows in the grid.
        gridtype : int
            An integer indicating which pattern to create 
            (handled in the public methods like randomGrid, beacon, etc.).
        """
        self.cols = cols
        self.rows = rows
        # Create a 2D NumPy array (cols x rows) initially filled with zeros (all dead cells).
        self.world = np.zeros((self.cols, self.rows))

    def randomGrid(self):
        """
        Create a grid where each cell is randomly assigned to be dead (0) or alive (1).

        Returns
        -------
        numpy.ndarray
            The 2D array 'world' filled with random 0/1 states.
        """
        for i in range(self.cols):
            for j in range(self.rows):
                self.world[i, j] = random.randint(0, 1)
        return self.world

    def beacon(self):
        """
        Place a 'beacon' pattern near the center of the grid.

        The beacon is a 4x4 oscillating pattern in Conway's Game of Life, i.e.:
            1 1 0 0
            1 1 0 0
            0 0 1 1
            0 0 1 1

        Returns
        -------
        numpy.ndarray
            The updated 'world' array containing a beacon at the center.
        """
        beacon = [[1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1]]

        # Place the 4x4 beacon at (cols/2, rows/2).
        self.world[int(self.cols/2):int(self.cols/2)+4,
                   int(self.rows/2):int(self.rows/2)+4] = beacon
        return self.world

    def glider(self):
        """
        Place a 'glider' pattern near the center of the grid.

        The glider is a small pattern that moves across the board:
            0 1 0 0
            0 0 1 0
            1 1 1 0
            0 0 0 0

        Returns
        -------
        numpy.ndarray
            The updated 'world' array containing a glider at the center.
        """
        glider = [[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0]]

        # Place the 4x4 glider at (cols/2, rows/2).
        self.world[int(self.cols/2):int(self.cols/2)+4,
                   int(self.rows/2):int(self.rows/2)+4] = glider
        return self.world

    def gliderGun(self):
        """
        Place a 'Gosper glider gun' pattern near the top-left corner of the grid.

        This pattern repeatedly generates gliders. It's larger (9 rows x 36 columns).
        Placed starting at row 1, column 1.

        Returns
        -------
        numpy.ndarray
            The updated 'world' array containing a glider gun at the top-left area.
        """
        gliderGun = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        # Place the glider gun in the top-left area of the grid (rows [1..9], columns [1..37]).
        self.world[1:10, 1:37] = gliderGun
        return self.world

    def Sierpinksi(self):
        """
        (Currently incomplete) Attempt at placing a Sierpinski-triangle-based pattern.

        Returns
        -------
        numpy.ndarray
            The world with a small 2x4 pattern, presumably to be extended
            or used with rule 90 or similar. Not fully implemented.
        """
        triangle = [[0,1,1,0],
                    [0,1,1,0]]
        self.world[int(self.cols/2): int(self.cols/2)+2,
                   int(self.rows/2): int(self.rows/2)+4] = triangle
        return self.world
