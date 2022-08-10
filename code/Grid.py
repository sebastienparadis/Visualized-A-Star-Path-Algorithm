# Settings
from Functions import *
from config import *


# Set Grid - Initializes the 2D array grid
def set_grid(grid_width, num_rows):
    # using the BlockState class, we can add each block to a 2D array (grid) using embedded for loops
    grid = []
    # space taken by each block is the floor of div between grid width and total num of rows
    space = grid_width // num_rows
    # will append block state to this grid until grid is full
    for i in range(num_rows):  # row
        grid.append([])  # append nothing at the start of each row
        for j in range(num_rows):  # col
            # define specific block and add to list
            grid[i].append(Block(space, i, j, num_rows))

    return grid


# Draw Grid Lines - Adds grid lines between blocks
def draw_grid_lines(screen, grid_width, num_rows):
	#   O O O           O|O|O
	#                   -----
	#   O O O  ------>  O|O|O
	#                   -----
	#   O O O           O|O|O

	space = grid_width // num_rows
	i_index = 0
	for i in range(num_rows):
		# print("i: ", i)
		# RUN.draw.line(surface type, colour, start, end)
		j_index = 0
		RUN.draw.line(screen, grid_line_colour, (0, i_index * space), (grid_width, i_index * space))
		for j in range(num_rows):
			RUN.draw.line(screen, grid_line_colour, (j_index * space, 0), (j_index * space, grid_width))
			j_index += 1
		i_index += 1


# Draw Visual - Adds all individual blocks to default grid
def draw_visual(screen, grid_width, num_rows, grid):
	screen.fill(black)

	for i in grid:	 # row
		for j in i:	 # block
			j.draw(screen)

	draw_grid_lines(screen, grid_width, num_rows)
	RUN.display.update()


# Draw Default Screen - Creates blank grid with separating lines
def set_default_screen(screen, grid_width, num_rows, grid):
    screen.fill(black)
    draw_grid_lines(screen, grid_width, num_rows)


# Find Mouse - Returns location of mouse when click input
def find_mouse(position, grid_width, num_rows):
	space = grid_width // num_rows
	return position[0] // space, position[1] // space
