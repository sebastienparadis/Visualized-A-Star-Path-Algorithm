# Settings
from Functions import *


# Set Grid - Initializes the 2D array grid
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
            grid[i].append(Block(grid_width, j, i, num_rows))

    return grid


# Draw Grid Lines - Adds grid lines between blocks
def draw_grid_lines(screen, grid_width, num_rows):

    #   O O O           O|O|O
    #                   -----
    #   O O O  ------>  O|O|O
    #                   -----
    #   O O O           O|O|O

    space = grid_width//num_rows
    index_i = 0
    for i in range(num_rows):
        # run.draw.line(surface type, colour, start, end)
        index_j = 0
        run.draw.line(screen, silver, (0, index_i*space), (grid_width, index_i*space))
        index_i += 1
        index_j = 0
        for j in range(num_rows):
            run.draw.line(screen, silver, (index_j * space, 0), (grid_width, index_i * space))
            index_j += 1


# Draw Visual Grid - Adds all individual blocks to default grid
def draw_visual_grid(screen, grid_width, num_rows, grid):
    default_default_screen(screen, grid_width, num_rows, grid)
    for i in grid:      # row
        for j in i:     # block
            # using the methods in Block class, draw every block into grid
            j.draw(screen)
    run.display.update()


# Draw Default Screen - Creates blank grid with separating lines
def default_default_screen(screen, grid_width, num_rows, grid):
    screen.fill(black)
    draw_grid_lines(screen, grid_width, num_rows)


# Find Mouse - Returns location of mouse when click input
def find_mouse(position, grid_width, num_rows):
    space = grid_width//num_rows
    # position will be input as (y, x), since row ~= y and col ~= x
    return  position[0] // space,  position[1] // space
