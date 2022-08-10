# Settings
import math
import pygame as RUN
import pygame.mouse
from queue import PriorityQueue

# Dimensions
ScreenWidth = ScreenLength = 800   # width & length
screen = RUN.display.set_mode((ScreenWidth, ScreenLength))  # Square window, ignoring other var like resize
num_rows_config = 40  # official value of rows

# Text
RUN.display.set_caption("Path Finder: A* Algorithm - Sebastien Paradis")


# Colours RGB
# https://www.webucator.com/article/python-color-constants-module/

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
seashell4 = (139, 134, 130)
silver = (192, 192, 192)
yellow = (255, 255, 0)
gray = (127, 127, 127)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
antique_white3 = (205, 192, 176)
cadetblue = (95, 158, 160)
darkgoldenrod = (184, 134, 11)
darkorange2 = (238, 118, 0)
purple = (178, 58, 238)


# Game Colours
# Some preset looks

# #dark
# start_colour = blue
# target_colour = green
# obstacle_colour = red
# free_block_colour = white
# passed_block_colour = seashell4
# background_colour = black
# grid_line_colour = silver
# final_path_colour = yellow

#light
start_colour = blue
target_colour = green
obstacle_colour = black
free_block_colour = darkgoldenrod
passed_block_colour = antique_white3
background_colour = white
grid_line_colour = silver
final_path_colour = yellow

# start_colour = darkgoldenrod
# target_colour = green
# obstacle_colour = white
# free_block_colour = darkorange2
# passed_block_colour = purple
# background_colour = black
# grid_line_colour = silver
# final_path_colour = magenta
