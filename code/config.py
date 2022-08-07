# Settings
import math
import pygame as run
import pygame.mouse
# Dimensions
ScreenWidth = 1000            # width
ScreenLength = ScreenWidth    # length
screen = run.display.set_mode((ScreenWidth, ScreenLength)) # Square window, ignoring other var like resize

# Text
run.display.set_caption("Path Finder")

# Colours
# https://www.webucator.com/article/python-color-constants-module/

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
seashell4 = (139, 134, 130)
silver = (192, 192, 192)

Conversions = {
    white: 0,
    black: 1,
    red: 2,
    green: 3,
    blue: 4,
    seashell4: 5,
    silver: 6
}
