class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # #use dfs to recursively visit every node touching the 1 we found, mark them as 0 and add to a count
        # #save all directions to check in dfs can be accessed by index
        # directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # ROWS, COLS = len(grid), len(grid[0]) #get grid size
        # islands = 0

        # def dfs(r,c):
        #     #check if r or col out of bounds, or position at place is island
        #     if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
        #         return
        #     #sink island spot
        #     grid[r][c] = '0'

        #     #recursively check all directions
        #     for dr,dc in directions:
        #         dfs(r + dr, c+dc)
            
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             #if island found, sink entire section
        #             dfs(r,c)
        #             islands += 1
        # return islands

        #BFS attempt
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])

        visited = set()

        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) 
                        and grid[r][c] == '1' 
                        and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands