# Settings
from BlockState import *


# Declarations
# h (AKA heuristic/taxi cab)

# Definitions

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
