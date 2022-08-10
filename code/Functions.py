# Settings
from BlockState import *
from Grid import *


# Declarations
# h (AKA heuristic/taxi cab)

# Definitions

# For now, not going to add any lines between grid until I test

# in function for A*, h
# "Taxi Cab" Distance / Heuristic function
def heuristic(fst_coord, snd_coord):
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
    x1, y1 = fst_coord
    x2, y2 = snd_coord

    taxi_cab_dist = ( abs(x2 - x1) + abs(y2 - y1) )
    return taxi_cab_dist


def final_path(previous, this_node, draw):
    # using linked_list method of interacting back
    while this_node in previous:  # adding all nodes from previous and setting as path
        this_node = previous[this_node]  # linked list idea
        this_node.set_path()
        draw()
