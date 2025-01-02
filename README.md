Cellular Automata & Random Walk Simulations in Python
This repository contains Python scripts demonstrating two main concepts:

Conway’s Game of Life – a classic cellular automaton where cells evolve based on neighbor counts.
Random Walk – a simple random-based movement demonstration on a grid.
All scripts target Python 3.x and use NumPy and matplotlib for array operations and animations.

1. Conway’s Game of Life
Overview
The Game of Life scripts allow you to configure and visualize different initial patterns (e.g., random grids, gliders, beacons, a glider gun) and watch them evolve over a specified number of iterations.
The primary components include:

game_of_life.py (example name):

neighbours(i, j, world): Counts and applies the rules to determine if a cell lives or dies.
gen(world): Generates the next iteration of the entire grid.
animate(world, nt, rep): Uses matplotlib.animation to create a visual animation of nt iterations.
start(): Interactively prompts you for number of columns, rows, a grid pattern type, etc., then calls animate.
grid.py:

MakeGrid class that provides methods (randomGrid, beacon, glider, gliderGun, etc.) to initialize the grid with various known patterns in Conway’s Game of Life.
Dependencies
Python 3.x
NumPy
matplotlib
(Optionally argparse if you plan to extend the script with command-line arguments, though it’s currently just interactive prompts.)

Usage
Install required libraries (if not already installed):
bash
Copy code
pip install numpy matplotlib
Run the Game of Life script (example):
bash
Copy code
python game_of_life.py
Interactive prompts:
How many columns? – e.g., 50
How many rows? – e.g., 50
Select gridtype: – e.g., 0 for random, 1 for beacon, 2 for glider, 3 for glider gun
How many times? – number of iterations to animate
Repeat simulation? – yes/no (to determine if the animation loops)
After entering your choices, a window opens showing the grid evolving frame by frame.
Note: Large grids or high iteration counts may slow down the animation.

2. Random Walk
Overview
The Random Walk script demonstrates a simple 2D movement pattern. Each time-step, a cell with value 1 can move up, down, left, or right on a grid, leaving “trails” marked as 2.

Key functions:

makeGrid(): Initializes a 60×60 array with a single cell set to 1 at the center.
gen(world): Randomly selects a move (1–4) for any cell with value 1, shifts it, and replaces its former positions with 2.
animate(world, nt): Creates an 80-frame animation (by default) visualizing these random steps using matplotlib.animation.
Usage
Install required libraries:
bash
Copy code
pip install numpy matplotlib
Run the random walk script (example):
bash
Copy code
python random_walk.py
The script will:
Create a 60×60 grid (makeGrid()) with one cell set to 1.
Animate nt=80 time-steps (animate(grid, 80)), updating the grid randomly each frame.
Display the resulting movement in a matplotlib window, with each frame shown for ~0.1 seconds (interval=100ms).
The result is a simple random path moving across the grid.

Common Notes
Both simulations use matplotlib’s ArtistAnimation, which stores frames in memory before displaying the animation. On very large grids or with a high number of frames, this can consume a lot of memory and take time to render.
You can experiment with different parameters to see more complex behaviors or different speeds.
Optional: If you want to run these scripts on a remote cluster (like CSC’s Puhti) and you do not have a graphical environment, you may want to direct the output to a file, or run them locally with X-forwarding enabled (or produce an .mp4 output using matplotlib.animation.Animation.save).
Extending / Modifying
Argparse: The scripts contain commented-out examples of how to handle command-line arguments. You could re-enable that code and remove the input() calls to run it in a fully non-interactive mode:
bash
Copy code
python game_of_life.py --grid-size 50 50 --gridtype 2 --nt 100
Additional Patterns: In grid.py, you can define more patterns (e.g., Sierpinski or custom ones) by adding methods and referencing them with a new gridtype index.
Performance Tweaks: For large grids, consider using blit=True (already set in the code) and decreasing the iteration count or the update frequency to speed up the animation.
Contact / Acknowledgments
Conway’s Game of Life concept: Wikipedia
Random walk concept: Wikipedia
These scripts are provided as teaching tools or fun examples of Python-based visualization. Contributions, suggestions, or bug reports are welcome via GitHub issues or pull requests.

