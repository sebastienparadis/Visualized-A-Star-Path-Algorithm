# Settings
from BlockState import *


# Declarations
# set_grid
# h (AKA heuristic/taxi cab)

# Definitions
def set_grid(grid_width, num_rows):
    # using the BlockState class, we can add each block to a 2D array (grid) using embedded for loops
    grid = []
    # space taken by each block is the floor of div between grid width and total num of rows
    space = grid_width//num_rows
    # will append block state to this grid until grid is full
    for i in range(num_rows):  # row
        grid.append([])  # append nothing at the start of each row
        for j in range(num_rows):  # col
            # define specific block and add to list
            grid[i].append( Block(space, i, j, num_rows) )

    return grid


# For now, not going to add any lines between grid until I test

# in function for A*, h
# "Taxi Cab" Distance / Heuristic function
def h(fst_coord, snd_coord):
    # The distance is the sum of the absolute value of the difference of the x values and
    # the absolute value of the difference of the y values
    #   distance = |x2 - x1| + |y2 - y1|
    #   e.g. From X to X
    #   O O O O O O O O O O O O             O O O O O O O O O O O O
    #   O O X O O O O O O O O O             O O X O O O O O O O O O
    #   O O O O O O O O O O O O             O O T O O O O O O O O O
    #   O O O O O O O O O O O O   ------>   O O T O O O O O O O O O
    #   O O O O O O O O O O O O             O O T O O O O O O O O O
    #   O O O O O O O O X O O O             O O T T T T T T X O O O
    #   O O O O O O O O O O O O             O O O O O O O O O O O O

    # coord format: (x, y)
    x1 = fst_coord[0]
    y1 = fst_coord[1]
    x2 = snd_coord[0]
    y2 = snd_coord[1]

    taxi_cab_dist = ( abs(x2 - x1) + abs(y2 - y1) )
    return taxi_cab_dist
