import turtle
import astar
import bfs
import sys

import turtle

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

def setup_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -320 + (x*20)
            screen_y = 320 - (y*20)
            if character == 1:
                pen.goto(screen_x, screen_y)
                pen.stamp()
            elif character == 2:
                path.goto(screen_x, screen_y)
                path.stamp()
				
r = 0
try:
	r = open(input("Input file name: "), "r")
	maze = [[]]
	row = 0
	for line in r:
		for char in line:
			if char == '\n':
				maze += [[]]
				row = row + 1
			else:
				maze[row] += [int(char)]
	maze.pop()
	
	print("Read maze:")
	for row in maze:
		for char in row:
			print(char, end=" ")
		print()
	
	strategy = input("What strategy would you like to use? (bfs/astar): ")

	start = (int(input("Specify starting x position: ")), int(input("Specify starting y position: ")))
	finish = (int(input("Specify finish x position: ")), int(input("Specify finish y position: ")))
	
	wn = turtle.Screen()
	wn.bgcolor("black")
	wn.title("Maze Solver")
	wn.setup(1200,800)
	
	pen = Pen()
	path = Path()
	
	setup_maze(maze)
	if (strategy == "bfs"):
		bfs.solve_maze(maze, start, finish)
	else:
		astar.solve_maze(maze, start, finish)
	print("Read maze:")	
	setup_maze(maze)
	input("Press enter to exit...")
	
except FileNotFoundError:
	print("ERROR: File not found!")


