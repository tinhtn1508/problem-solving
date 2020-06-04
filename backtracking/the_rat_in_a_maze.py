def solveMaze(maze):
    N = len(maze)
    def isSafe(maze, x, y):
        if x >= 0 and x < N and y >= 0  and y < N: return True
        return False
    
    def helper(maze, x, y, sol):
        if x == N - 1 and y == N - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True
        
        if isSafe(maze, x, y):
            sol[x][y] = 1
            if helper(maze, x + 1, y, sol): return True
            
            if helper(maze, x, y + 1, sol): return True
                
            sol[x][y] = 0
            return False
        return False
    
    sol = [[0 for _ in range(N)] for _ in range(N)]
    if not helper(maze, 0, 0, sol):
        print("Solution doesn't exist !!!")
    return sol
        
if __name__ == "__main__":
    
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    sol = solveMaze(maze)
    print(sol)
