def solve_maze(maze, start, finish):     
	
	maze[start[0]][start[1]] = 0
	maze[finish[0]][finish[1]] = 0
	
    def searchStart(maze):
        i = 0
        while (i < len(maze) and maze[i][0] != 0) :
            i = i + 1
        return i

    def makeDeep(deep, maze):
        i = 0
        while i < len(maze) :
            j = 0
            temp = []
            while j < len(maze[i]) :
                temp.insert(len(temp), -1)
                j = j + 1
            deep.insert(len(deep), temp)
            i = i + 1

    # x kebawah y ke kanan
    def isThereAPath(list, deep, x, y):
        return (x >= 0) and (y >= 0) and (x < len(list)) and (y < len(list[0])) and (list[x][y] == 0) and (deep[x][y] == -1)

    def isExit(list, x, y, finish):
        return (x == finish[0]) and (y == finish[1])

    def bfs(start, maze, deep, finish):
        queue = []
        now = start
        solve = False
        queue.insert(len(queue),now)
        while len(queue) > 0 and solve is False :
            now = queue.pop()
            x = now[0]
            y = now[1]
            if (isThereAPath(maze, deep, x+1, y)) :
                deep[x+1][y] = deep[x][y] + 1
                queue.insert(len(queue), (x+1, y))
                if (isExit(maze, x+1, y, finish)) :
                    solve = True
            if (isThereAPath(maze, deep, x-1, y)) :
                deep[x-1][y] = deep[x][y] + 1
                queue.insert(len(queue), (x-1, y))
                if (isExit(maze, x-1, y, finish)) :
                    solve = True
            if (isThereAPath(maze, deep, x, y+1)) :
                deep[x][y+1] = deep[x][y] + 1
                queue.insert(len(queue), (x, y+1))
                if (isExit(maze, x, y+1, finish)) :
                    solve = True
            if (isThereAPath(maze, deep, x, y-1)) :
                deep[x][y-1] = deep[x][y] + 1
                queue.insert(len(queue), (x, y-1))
                if (isExit(maze, x, y-1, finish)) :
                    solve = True
        return solve

    def isParent(deep, x, y, before):
        return (x >= 0) and (y >= 0) and (x < len(deep)) and (y < len(deep[x])) and ((deep[x][y] + 1) == deep[before[0]][before[1]])

    def makePath(maze, deep, finish):
        x = finish[0]
        y = finish[1]
        maze[x][y] = 2
        if (deep[x][y] == 0):
            return
        elif (isParent(deep, x+1, y, finish)):
            nxt = (x+1,y)
            makePath(maze, deep, nxt)
        elif (isParent(deep, x-1, y, finish)):
            nxt = (x-1,y)
            makePath(maze, deep, nxt)
        elif (isParent(deep, x, y+1, finish)):
            nxt = (x,y+1)
            makePath(maze, deep, nxt)
        elif (isParent(deep, x, y-1, finish)):
            nxt = (x,y-1)
            makePath(maze, deep, nxt)

    deep = []
    makeDeep(deep, maze)
    deep[start[0]][start[1]] = 0
    if (bfs(start, maze, deep, finish)):
        makePath(maze, deep, finish)
        print("YA")



