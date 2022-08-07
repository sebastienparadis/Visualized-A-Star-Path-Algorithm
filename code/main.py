from Algorithm import *


def main(screen, grid_width, num_rows):

    # declarations
    #
    start_block = None
    end_block = None
    go = True
    started = False
    left_clicks = 0
    grid = set_grid(grid_width, num_rows)
    # definitions
    while go:
        draw_visual(screen, grid_width, num_rows, grid)
        for EVENT in run.event.get():
            if EVENT.type == run.QUIT:  # Defined as exit button has been clicked
                go = False

            if started:
                continue

            # once a user left-clicks their mouse, need to determine what the intention is
            # If it is the first click, it is the start.
            # if it is the second click, it is the end.
            # Otherwise, it is a barrier
            if pygame.mouse.get_pressed()[0]:  # left click OR middle click
                left_clicks += 1
                # print(left_clicks)
                x, y = find_mouse(pygame.mouse.get_pos(), grid_width, num_rows)  # returns mouse location
                block = grid[x][y]  # determines appropriate block
                if left_clicks == 1:
                    start_block = block
                    start_block.set_start()

                elif left_clicks == 2:
                    end_block = block
                    end_block.set_target()

                elif left_clicks > 2:
                    block.set_obstacle()

            # Thinking of using the middle or right mouse button as a function, either reset, erase, or both

    run.quit()  # exit PathFinder


main(screen, ScreenWidth, num_rows_config)  # run PathFinder
