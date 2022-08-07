from Grid import *

def main(screen, grid_width):
    num_rows = 50
    grid = set_grid(grid_width, num_rows)
    start_block = None
    end_block = None
    go = True
    started = False

    while go:
        draw_visual_grid(screen, grid_width, num_rows, grid)
        for event in run.event.get():
            if event.type == run.QUIT:
                go = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1]:  # left click OR middle click
                position = pygame.mouse.get_pos()
                block_row, block_col = find_mouse(position, grid_width, num_rows)
                block = grid[block_row][block_col]

                if block is not start_block:
                    start_block = block
                    start_block.set_start()

                elif block is not end_block:
                    end_block = block
                    end_block.set_target()

                elif block is not end_block and block is not start_block:
                    block.set_obstacle()

            elif pygame.mouse.get_pressed()[2]:  # right click
                pass

    run.quit()


main(screen, ScreenWidth)
