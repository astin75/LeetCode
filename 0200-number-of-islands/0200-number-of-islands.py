class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 섬의 개수를 구하는 문제 입니다
        # 육지는1이고, 물은 0 입니다.
        # 섬의 조건은 연결된 육지의 개수 입니다. 
        
        #문제 풀이
        #먼저 모든 행렬을 방문 해야하고
        #방문해서 인접한 곳에 육지가 있는지 확인 해야 함으로
        #dfs를 사용해서 풀겠습니다. 
        
        #조건 2 인접한 곳에 육지가 있는지 확인하고 
        # 방문했으면 '#' 처리하여 재방문 하지 않게 만든다.
        def dfs(row, col):
            #escape case
            if row <0 or col<0 or row >= len(grid) or \
            col >= len(grid[0]) or grid[row][col] != '1':
                return
            grid[row][col] = '#'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        
        #모든 행렬방문하기
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #조건 1 : 육지인 섬만 탐색을 하면 된다.
                if grid[row][col] == '1':
                    count +=1
                    dfs(row, col)
        return count
                    
                    
        