class Solution(object):
    def numIslands(self, grid):
        def dfs(row:int,col:int):
            
            if row < 0 or row >= (len(grid)) or col <0 or  col >= (len(grid[0])) or grid[row][col] != "1":
                return 
            grid[row][col] = "#"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)     
               
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)

                    count += 1
        return count