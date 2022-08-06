# Settings
from config import *


# BlockState
# Class to define all things blocks
class BlockState:
    # CONSTRUCTOR
    def __int__(self, block_width, row, col):
        self.block_width = block_width
        self.row = row
        self.col = col
        self.colour = black  # default grid set to black

    # RESET
    def reset(self):
        self.colour = black

    # GETTERS
    # Get block position (row, column)
    def get_position(self):
        return self.row, self.col

    # Get block colour (corresponds to block state)
    def get_colour(self):
        return self.colour

    # Get y coordinate, for draw
    def get_y_pos(self):
        return self.col*self.block_width

    # Get x coordinate, for draw
    def get_x_pos(self):
        return self.row*self.block_width

    # CHECKERS
    # Check if beginning position
    def is_start(self):
        return self.colour == blue

    # Check if adjacent tile is free
    def is_free(self):
        return self.colour == white

    # Check is a block has been seen
    def is_passed(self):
        return self.colour == seashell4

    # Check if block is a set obstacle
    def is_obstacle(self):
        return self.colour == red

    # Check if block is final target
    def is_target(self):
        return self.colour == green

    # SETTERS
    # User creating obstacle, as defined in pygame format
    def user_draw_obstacle(self, display):
        # We need to x and y coordinates, from getters
        pygame.draw.rect(display, self.colour, (self.get_x_pos(), self.get_y_pos(), self.block_width, self.block_width))

    def set_start(self):
        self.colour = blue

    # Check if adjacent tile is free
    def set_free(self):
        self.colour = white

    # Check is a block has been seen
    def set_passed(self):
        self.colour = seashell4

    # Check if block is a set obstacle
    def set_obstacle(self):
        self.colour = red

    # Check if block is final target
    def set_target(self):
        self.colour = green
