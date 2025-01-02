# Conway’s Game of Life & Random Walk Simulations

This repository contains Python scripts demonstrating two main concepts:

1. **Conway’s Game of Life** – a classic cellular automaton where cells evolve based on neighbor counts.  
2. **Random Walk** – a simple demonstration of cells moving at random on a grid.

All scripts target **Python 3** and use **NumPy** and **matplotlib** for array operations and animations.

---

## 1. Conway’s Game of Life

### Overview

The Game of Life scripts allow you to **configure** and **visualize** various initial patterns (random, beacon, glider, glider gun, etc.) and watch them evolve for a specified number of iterations.

**Key files:**

- **`gol.py`**:
  - **`neighbours(i, j, world)`**: Determines the next state of a cell based on how many neighbors it has.
  - **`gen(world)`**: Creates the next iteration of the entire grid.
  - **`animate(world, nt, rep)`**: Uses `matplotlib.animation` to produce an animation over `nt` iterations, optionally repeating.
  - **`start()`**: Interactively prompts for grid size, pattern type, and iteration count, then runs the animation.

- **`grid.py`**:
  - **`MakeGrid`** class with methods (`randomGrid`, `beacon`, `glider`, `gliderGun`, etc.) to create different **initial states** of the grid.

### Dependencies

- **Python 3.x**
- **NumPy**
- **matplotlib**

### How to Run

1. **Install** dependencies (if needed):
   ```bash
   pip install numpy matplotlib
   ```

2. Run the script:
  ```bash
   python gol.py
  ```

3. Respond to prompts:
Number of columns, number of rows
Grid type (0 for random, 1 for beacon, 2 for glider, 3 for glider gun, etc.)
Number of iterations
Whether to repeat the animation (yes/no)

A window opens showing the grid evolving.
Note: Large grids or large iteration counts can slow down the animation.

---

## 2. Random Walk

### Overview

The **Random Walk** script shows a cell with value `1` moving around on a 2D grid, leaving a trail of `2`s. Each time step, the script randomly picks a direction (up, down, left, or right) and moves that cell accordingly.

**Key points:**

- **`makeGrid()`**: Creates a 60×60 grid with one cell set to `1` in the center.
- **`gen(world)`**: Picks a random direction for any `1` cell, moves it, and marks previous positions with `2`.
- **`animate(world, nt)`**: Animates `nt` frames using `matplotlib.animation`.

### Dependencies

- **Python 3.x**
- **NumPy**
- **matplotlib**

### How to Run

1. **Install** dependencies (if not already done):
   ```bash
   pip install numpy matplotlib
   ```

2. Run the script:
  ```bash
   python randwalk.py
```

3. The script will:
- Create a 60×60 grid (one cell set to 1)
- Animate 80 steps (or however many you configure), updating the grid each frame
- Display the result as a simple random movement pattern
- A window will open showing the random walk in progress.


## References

- [Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Random walk](https://en.wikipedia.org/wiki/Random_walk)




