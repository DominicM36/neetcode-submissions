class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #use dfs to recursively visit every node touching the 1 we found, mark them as 0 and add to a count
        #save all directions to check in dfs can be accessed by index
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0]) #get grid size
        islands = 0

        def dfs(r,c):
            #check if r or col out of bounds, or position at place is island
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            #sink island spot
            grid[r][c] = '0'

            #recursively check all directions
            for dr,dc in directions:
                dfs(r + dr, c+dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    #if island found, sink entire section
                    dfs(r,c)
                    islands += 1
        return islands