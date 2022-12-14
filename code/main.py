from Algorithm import *
from Grid import *

def main(screen, grid_width, num_rows):
    # num_rows = num_rows_config  # changeable in config.py
    grid = set_grid(grid_width, num_rows)
    start_block = target = None
    pathfinding = True  # determine whether to keep running program
    # left_clicks = 0


    # Run the screen with the grid, where user can make maze and run the pathfinder
    while pathfinding:
        draw_visual(screen, grid_width, num_rows, grid)

        for EVENT in RUN.event.get():
            if EVENT.type == RUN.QUIT:  # Defined as exit button has been clicked
                pathfinding = False

            if RUN.mouse.get_pressed()[0]:  # left-click
                # left_clicks += 1
                x, y = find_mouse(RUN.mouse.get_pos(), grid_width, num_rows)
                block = grid[x][y]
                if block is not target and not start_block:
                    # if left_clicks == 1:
                    RUN.time.wait(50)  # avoids double-click
                    start_block = block
                    start_block.set_start()

                elif not target and block is not start_block:
                    RUN.time.wait(50)  # avoids double-click
                    target = block
                    target.set_target()

                elif block is not target and block is not start_block:
                    block.set_obstacle()


            elif RUN.mouse.get_pressed()[1]:  # use right-click to remove obstacles
                x, y = find_mouse(RUN.mouse.get_pos(), grid_width, num_rows)  # returns mouse location
                block = grid[x][y]
                block.reset()
                if block == start_block:
                    start_block = None  # this way, if we remove the start block, the next one we place is the new start
                elif block == target:
                    target = None  # this way, if we remove the start block AND the target block, the next one we place will still be the new start


            if EVENT.type == RUN.KEYDOWN:  # runs the game
                if EVENT.key == RUN.K_RETURN and start_block and target:  # start game with RETURN key
                    for i in grid:
                        for block in i:
                            # First, get the adjacent blocks for algorithm calculations
                            block.get_adjacent(grid)
                        # Start the algorithm.
                    algorithm(grid, start_block, target, lambda: draw_visual(screen, grid_width, num_rows, grid)) #, num_rows_config

                elif EVENT.key == RUN.K_KP_ENTER and start_block and target:  # or start game with ENTER key (was not working on my mac)
                    for i in grid:
                        for block in i:
                            block.get_adjacent(grid)

                    algorithm(grid, start_block, target, lambda: draw_visual(screen, grid_width, num_rows, grid)) #, num_rows_config

                if EVENT.key == RUN.K_r:  # reset with R key
                    start_block = target = None  # reset backend values
                    grid = set_grid(grid_width, num_rows)  # reset the grid

    # Standard pygame quit call
    RUN.quit()  # exit PathFinder


main(screen, ScreenWidth, num_rows_config)  # run PathFinder
