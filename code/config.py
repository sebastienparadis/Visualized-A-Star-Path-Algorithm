# Settings
import math
import pygame


# Dimensions
ScreenWidth = 1000            # width
ScreenLength = ScreenWidth    # length
screen = pygame.display.set_mode( (ScreenWidth, ScreenLength) ) # Square window, ignoring other var like resize

# Text
pygame.display.set_caption("Path Finder")

# Colours
# https://www.webucator.com/article/python-color-constants-module/

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
seashell4 = (139,134,130)


colourConversions = {
    white: 0,
    black: 1,
    red: 2,
    green: 3,
    blue: 4,
    seashell4: 5,
}
