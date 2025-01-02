import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import argparse
import sys

from grid import MakeGrid  # Custom class used to generate initial grid patterns

def neighbours(i, j, world):
    """
    Calculate the next state (0 or 1) of a cell at (i, j) in the 'world' array
    based on the Conway's Game of Life rules.

    Parameters:
    -----------
    i : int
        Row index of the cell.
    j : int
        Column index of the cell.
    world : numpy.ndarray
        2D array representing the current state of the grid.

    Returns:
    --------
    int
        The next state (0 or 1) for cell (i, j) based on number of neighbors.
    """
    # Count the total number of neighbors by summing the 3x3 block centered on (i, j).
    # Subtract the cell's own value to get only its neighbors.
    neighbours_count = np.sum(world[i - 1:i + 2, j - 1:j + 2])
    neighbours_count -= world[i, j]

    # If the cell is alive (1):
    if world[i, j] == 1:
        # Dies by underpopulation (<2) or overpopulation (>3).
        if neighbours_count < 2 or neighbours_count > 3:
            return 0

    # If the cell is dead (0):
    elif world[i, j] == 0:
        # Becomes alive if exactly 3 neighbors.
        if neighbours_count == 3:
            return 1

    # Otherwise, cell state remains unchanged.
    return world[i, j]

def gen(world):
    """
    Generate the next state (one iteration) of the entire world grid.

    Parameters:
    -----------
    world : numpy.ndarray
        The current state of the grid (2D array).

    Returns:
    --------
    numpy.ndarray
        A new 2D array (copy of the old one) after applying the Game of Life rules.
    """
    new_world = np.copy(world)
    # Iterate through every cell in the grid
    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            new_world[i, j] = neighbours(i, j, world)
    return new_world

def animate(world, nt, rep):
    """
    Create and display an animation of Conway's Game of Life for 'nt' iterations.

    Parameters:
    -----------
    world : numpy.ndarray
        Initial grid (2D array).
    nt : int
        Number of iterations (or 'frames') to animate.
    rep : str
        Whether the animation should repeat ('true'/'yes' or 'false'/'no').

    Notes:
    ------
    - Uses matplotlib.animation.ArtistAnimation to create the animation.
    - The 'interval=10' sets the delay between frames in milliseconds.
    - 'blit=True' can improve performance, but can cause issues with
      some backends.
    """
    fig = plt.figure()
    plt.axis('on')
    ims = []  # Will store the frames (each a tuple of (imshow, title))

    # Convert string input for repeat into boolean
    if rep == "true" or rep == "yes":
        boolrep = True
    elif rep == "false" or rep == "no":
        boolrep = False
    else:
        # Default if user typed something unexpected
        boolrep = False

    print("Starting simulation")
    # Generate and record 'nt' frames
    for n in range(nt):
        ims.append((plt.imshow(world, cmap='binary'),
                    plt.title('Game_Of_Life')))
        # Update 'world' for the next frame
        world = gen(world)

    # Create the animation
    gol_animation = animation.ArtistAnimation(
        fig,
        ims,
        interval=10,  # Time (ms) between each frame
        repeat=boolrep,
        blit=True
    )

    plt.show()

def start():
    """
    Prompt the user for parameters (grid size, type of grid, number of iterations),
    generate an initial world, and then run an animation of Conway's Game of Life.
    """
    # Query user for basic parameters
    cols = int(input("How many columns? "))
    rows = int(input("How many rows? "))
    gridtype = int(input("Select gridtype: 0:, 1:, 2:, 3:, "))
    toistot = int(input("How many times? "))
    uudelleen = input("Repeat simulation? (yes/no) ")

    print('{} , {} , {} , {} , {}'.format(cols, rows, gridtype, toistot, uudelleen))

    # Initialize the empty grid
    world = np.zeros((cols, rows))
    # Create a MakeGrid object (custom class) to build specific patterns
    gridi = MakeGrid(cols, rows, gridtype)

    # Select the pattern for the initial grid
    if gridtype == 0:
        world = gridi.randomGrid()
    elif gridtype == 1:
        world = gridi.beacon()
    elif gridtype == 2:
        world = gridi.glider()
    elif gridtype == 3:
        world = gridi.gliderGun()
    # elif gridtype == 4:
    #     world = gridi.Sierpinski()  # Example placeholder if implemented

    # Start the animation
    animate(world, toistot, uudelleen)

if __name__ == '__main__':
    # When script is run directly, call start() to begin an interactive session
    start()

# Below is commented-out code that could be used with argparse / sys.argv in the future:
#
# parser = argparse.ArgumentParser(description="Conway's Game of Life")
# parser.add_argument('--grid-size cols', dest='cols', required=True)
# parser.add_argument('--grid-size rows', dest='rows', required=True)
# parser.add_argument('--gridtype', dest='gridtype', required=True)
# parser.add_argument('--nt', dest='rows', required=True)
#
# cols = int(sys.argv[1])
# rows = int(sys.argv[2])
# gridtype = int(sys.argv[3])
# nt = int(sys.argv[4])
