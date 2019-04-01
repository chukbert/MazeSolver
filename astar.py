import heapq 

def solve_maze(maze, start, finish):
	
	movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]

	maze[start[0]][start[1]] = 0
	maze[finish[0]][finish[1]] = 0
	
	row = len(maze)
	col = len(maze[0])

	visited = [[False for _ in range(col)] for _ in range(row)]
	cost = [[-999 for _ in range(col)] for _ in range(row)]

	def f(x, y):
		return cost[x][y] + abs(x-finish[0]) + abs(y-finish[1])

	def is_valid(x, y):
		return x >= 0 and y >= 0 and x < row and y < col
		
	def set_path(x, y):
		maze[x][y] = 2
		x_after = -1
		y_after = -1
		for movement in movements:
			next_x = x + movement[0]
			next_y = y + movement[1]
			if is_valid(next_x, next_y):
				if (cost[next_x][next_y] == cost[x][y] - 1):
					x_after = next_x
					y_after = next_y
		if x_after != -1:
			set_path(x_after, y_after)

	cost[start[0]][start[1]] = 0
	pq = [(0, start)]

	heapq.heapify(pq)

	while (pq):
		cur = heapq.heappop(pq)
		x = cur[1][0]
		y = cur[1][1]
		visited[x][y] = True
		for movement in movements:
			next_x = x + movement[0]
			next_y = y + movement[1]
			if is_valid(next_x, next_y):
				if maze[next_x][next_y] == 0 and not visited[next_x][next_y]:
					cost[next_x][next_y] = cost[x][y] + 1
					heapq.heappush(pq, (f(next_x, next_y), (next_x, next_y)))
					
	if cost[finish[0]][finish[1]] != -999:
		set_path(finish[0], finish[1])
