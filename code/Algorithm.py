from Grid import *
from Functions import *

# Algorithm functions and helper functions


# #1.  Initialize the open list
# 2.  Initialize the closed list
#     put the starting node on the open
#     list (you can leave its f at zero)
# 3. while the open list is not empty
#       a) find the node with the least f on the open list, call it "q"
#       b) pop q off the open list
#       c) generate q's 8 successors and set their parents to q
#       d) for each successor
#           i) if successor is the goal, stop search
#           ii) else, compute both g and h for successor:
#               successor.g = q.g + distance between successor and q
#               successor.h = distance from goal to successor (This can be done using many ways, we will discuss
#               three heuristics-Manhattan, Diagonal and Euclidean Heuristics)
#
#               successor.f = successor.g + successor.h
#
#           iii) if a node with the same position as successor is in the OPEN list which has a lower f than
#           successor, skip this successor
#
#           iV) if a node with the same position as successor is in the CLOSED list which has a lower f than
#           successor, skip this successor otherwise, add  the node to the open list
#       end ( for loop)
#
#   e) push q on the closed list
# end (while loop)


def algorithm(grid, start_block, target_block, draw):
	# Need: priority-queue, start and target blocks, g and f accumulated values, and previous node value
	pq = PriorityQueue()
	num_stored = 0
	pq.put((0, num_stored, start_block))
	pq_hash = {start_block}
	previous = {}
	g = []
	f = []

	g = {block: 9999 for row in grid for block in row}
	f = {block: 9999 for row in grid for block in row}
	#print(start_block.get_position(), target_block.get_position())
	g[start_block] = 0
	f[start_block] = heuristic(start_block.get_position(), target_block.get_position())

	while not pq.empty():
		# Adding standard pygame quitting sequence
		for EVENT in RUN.event.get():
			if EVENT.type == RUN.QUIT:
				RUN.quit()

		# Algorithm logic
		# Need to check a few things and respond accordingly

		this_node = pq.get()[2]  # returns list of three (None, None, this_node)
		# print(this_node)
		if this_node is not None:  #in case
			pq_hash.remove(this_node)
		else:
			return 0 		   # error handling

		# Once reached the final target
		if this_node == target_block:
			# want to retrace the path before finalizing program
			final_path(previous, target_block, draw)
			target_block.set_target()
			return 1

		# print(this_node.get_adjacent_blocks(grid, num_rows))
		for next_node in this_node.adjacent:  # Up, Right, Left, and Down
			temp_g = g[this_node] + 1

			if temp_g < g[next_node]:  # temp_g is a better path, update value
				previous[next_node] = this_node
				g[next_node] = temp_g  # update g value
				f[next_node] = temp_g + heuristic(next_node.get_position(), target_block.get_position())  # update f value

				if next_node not in pq_hash:
					num_stored += 1
					pq.put((f[next_node], num_stored, next_node))
					pq_hash.add(next_node)
					next_node.set_free()

		draw()

		if this_node != start_block:
			this_node.set_passed()

	return 0


