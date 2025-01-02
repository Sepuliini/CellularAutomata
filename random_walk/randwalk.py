import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import argparse
import sys

def makeGrid():
    """
    Create and return a 60x60 NumPy array (world) of zeros.
    Initialize one cell to 1 at position (30, 30).

    Returns
    -------
    numpy.ndarray
        A 2D array (60x60) with one cell set to 1 in the center.
    """
    world = np.zeros((60, 60))
    world[30, 30] = 1
    return world

def gen(world):
    """
    Generate the next state of 'world' based on a random step for any cell with value 1.

    For each cell that has value 1:
      - Choose a random step direction (1 through 4).
      - Convert the current cell (i, j) to 2,
      - Place 2's in an adjacent cell based on the direction,
      - Place a 1 in a further cell in the same direction.

    Directions are interpreted as follows:
      1. Move left:   current cell -> 2, left 1 cell -> 2, left 2 cells -> 1
      2. Move right:  current cell -> 2, right 1 cell -> 2, right 2 cells -> 1
      3. Move down:   current cell -> 2, down 1 cell -> 2, down 2 cells -> 1
      4. Move up:     current cell -> 2, up 1 cell -> 2, up 2 cells -> 1 
         (though note in the code, 'i+1' and 'i-2' might be reversed in meaning 
          depending on row-index orientation)

    Parameters
    ----------
    world : numpy.ndarray
        A 2D NumPy array representing the grid.

    Returns
    -------
    numpy.ndarray
        A new 2D array that reflects the random step taken by any cell with value 1.
    """
    new_world = np.copy(world)
    step = random.randint(1, 4)  # Pick a random step direction

    for i in range(world.shape[0]):
        for j in range(world.shape[1]):

            if world[i, j] == 1:
                # If we find a cell with 1, move it and mark trails with 2
                if step == 1:
                    # Move to the left
                    new_world[i, j]   = 2
                    new_world[i, j-1] = 2
                    new_world[i, j-2] = 1

                if step == 2:
                    # Move to the right
                    new_world[i, j]   = 2
                    new_world[i, j+1] = 2
                    new_world[i, j+2] = 1

                if step == 3:
                    # Move down
                    new_world[i, j]   = 2
                    new_world[i+1, j] = 2
                    new_world[i+2, j] = 1

                if step == 4:
                    # Move up (though note here it's coded i+1 and i-2,
                    # so you may want to check the logic for i-2).
                    new_world[i, j]   = 2
                    new_world[i+1, j] = 2
                    new_world[i-2, j] = 1

    return new_world

def animate(world, nt):
    """
    Create an animation of 'nt' frames, each applying 'gen' to the world.

    Parameters
    ----------
    world : numpy.ndarray
        The initial grid (2D array).
    nt : int
        Number of steps/frames to animate.

    Notes
    -----
    - Each frame is created by calling 'gen(world)', which modifies cells
      in a somewhat random 'walk' manner.
    - The final animation is displayed via matplotlib's ArtistAnimation with
      interval=100ms between frames, no repeat, and blitting for performance.
    """
    fig = plt.figure()
    plt.axis('off')   # Turn off axis lines and labels
    ims = []
    i = 0

    # Generate and store each frame
    for n in range(nt):
        ims.append(
            (plt.imshow(world, cmap='binary'), plt.title('RandomWalk'))
        )
        world = gen(world)  # Update world for the next frame

        i += 1
        # Print progress for debugging (here as fraction of 1000, presumably arbitrary)
        print(i / 1000)

    print("Starting simulation")

    # Create the animation
    walk_animation = animation.ArtistAnimation(
        fig, ims, interval=100, repeat=False, blit=True
    )
    plt.show()

def start():
    """
    Entry point to initialize the grid, then animate 80 steps.

    No user input in this script; it just creates a 60x60 grid with a cell 
    set to 1 at [30,30] (via makeGrid), then calls animate() with 80 iterations.
    """
    grid = makeGrid()
    animate(grid, 80)

if __name__ == '__main__':
    # If run directly, call 'start' to begin execution
    start()
