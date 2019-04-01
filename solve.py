import turtle
import astar
import bfs
import sys

r = 0

try:
	r = open(sys.argv[1], "r")
	maze = [[]]
	row = 0
	for line in r:
		for char in line:
			if char == '\n':
				maze += [[]]
				row = row + 1
			else:
				maze[row] += [char]
	maze.pop()
	print(maze)
	
	strategy = input("What strategy would you like to use? (bfs/astar): ")

	start = (int(input("Specify starting x position: ")), int(input("Specify starting y position: ")))
	finish = (int(input("Specify finish x position: ")), int(input("Specify finish y position: ")))

	if (strategy == "bfs"):
		
	
	
except IndexError:
	print("Please specify maze_input_file.")
	print()
	print("Usage: python solve.py [maze_input_file]")


