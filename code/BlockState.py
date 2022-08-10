# Settings
from config import *


# BlockState
# Class to define all things blocks
class Block:
    def __init__(self, block_width, row, col, num_rows):      # CONSTRUCTOR
        self.block_width = block_width
        self.row = row
        self.col = col
        self.block_colour = None  # default grid set to background_colour
        self.block_colour = background_colour  # default grid set to background colour (config.py)
        self.num_rows = num_rows

        self.adjacent = []  # needed for algorithm

    # Reset board
    def reset(self):
        self.block_colour = background_colour

    # Get block position (row, column)
    def get_position(self):
        return self.row, self.col

    # Get block colour (corresponds to block state)
    def get_colour(self):
        return self.block_colour

    # Get y coordinate, for draw
    def get_y_pos(self):
        return self.col*self.block_width

    # Get x coordinate, for draw
    def get_x_pos(self):
        return self.row*self.block_width

    # Check if beginning position
    def is_start(self):
        return self.block_colour == start_colour

    # Check if adjacent tile is free
    def is_free(self):
        return self.block_colour == free_block_colour

    # Check is a block has been seen
    def is_passed(self):
        return self.block_colour == passed_block_colour

    # Check if block is a set obstacle
    def is_obstacle(self):
        return self.block_colour == obstacle_colour

    # Check if block is final target
    def is_target(self):
        return self.block_colour == target_colour

    # User creating obstacle, as defined in run format
    def draw(self, screen):
        # We need to x and y coordinates, from getters
        RUN.draw.rect(screen, self.block_colour, (self.get_x_pos(), self.get_y_pos(), self.block_width, self.block_width))

    # Setting the starting block
    def set_start(self):
        self.block_colour = start_colour

    # Check if adjacent tile is free
    def set_free(self):
        self.block_colour = free_block_colour

    # Check is a block has been seen
    def set_passed(self):
        self.block_colour = passed_block_colour

    # Check if block is a set obstacle
    def set_obstacle(self):
        self.block_colour = obstacle_colour

    # Check if block is final target
    def set_target(self):
        self.block_colour = target_colour

    def set_path(self):
        self.block_colour = final_path_colour

    # Get Adjacent Blocks
    def get_adjacent(self, grid):
        # To run the algorithm, we need to know the neighbours of every block in the grid. This function stores
        # every block's non-obstacle neighbour for algorithm calculations

        # UP: If we are not at the top row (row != 0) and the block above is not an obstacle
        self.adjacent = []
        if self.row < self.num_rows - 1 and not grid[self.row + 1][self.col].is_obstacle():  # DOWN
            self.adjacent.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():  # UP
            self.adjacent.append(grid[self.row - 1][self.col])

        if self.col < self.num_rows - 1 and not grid[self.row][self.col + 1].is_obstacle():  # RIGHT
            self.adjacent.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():  # LEFT
            self.adjacent.append(grid[self.row][self.col - 1])
