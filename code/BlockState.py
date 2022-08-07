# Settings
from config import *


# BlockState
# Class to define all things blocks
class Block:
    def __init__(self, grid_width, row, col, num_rows):      # CONSTRUCTOR
        self.grid_width = grid_width
        self.row = row
        self.col = col
        self.block_colour = None  # default grid set to black
        self.block_colour = black  # default grid set to black
        self.num_rows = num_rows

    # Reset board
    def reset(self):
        self.block_colour = black

    # Get block position (row, column)
    def get_position(self):
        return self.row, self.col

    # Get block colour (corresponds to block state)
    def get_colour(self):
        return self.block_colour

    # Get y coordinate, for draw
    def get_y_pos(self):
        return self.col*self.grid_width

    # Get x coordinate, for draw
    def get_x_pos(self):
        return self.row*self.grid_width

    # Check if beginning position
    def is_start(self):
        return self.block_colour == blue

    # Check if adjacent tile is free
    def is_free(self):
        return self.block_colour == red

    # Check is a block has been seen
    def is_passed(self):
        return self.block_colour == seashell4

    # Check if block is a set obstacle
    def is_obstacle(self):
        return self.block_colour == white

    # Check if block is final target
    def is_target(self):
        return self.block_colour == green

    # User creating obstacle, as defined in run format
    def draw(self, screen):
        # We need to x and y coordinates, from getters
        run.draw.rect(screen, self.block_colour, (self.get_x_pos(), self.get_y_pos(), self.grid_width, self.grid_width))

    def set_start(self):
        self.block_colour = blue

    # Check if adjacent tile is free
    def set_free(self):
        self.block_colour = red

    # Check is a block has been seen
    def set_passed(self):
        self.block_colour = seashell4

    # Check if block is a set obstacle
    def set_obstacle(self):
        self.block_colour = white

    # Check if block is final target
    def set_target(self):
        self.block_colour = green
