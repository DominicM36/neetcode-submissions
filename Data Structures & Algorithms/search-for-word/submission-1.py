class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #general intuition: search the list in o(n) to find the first letter
        #from there use bfs to find the rest of the word:
        #iteratively add neighboring letters to a queue
        #check if the letter is correct and change it to a ? to mark as visited

        #update, need to use backtracking and not bfs directly
        #solution says dfs actually, lets see
        ROWS, COLS = len(board), len(board[0])
        #store set of visited path to contain r,c tuples to know if we have visited a word already
        path = set()

        #pass in row, colomn, and charCount variable
        def dfs(r,c,charCount):
            #base case good scenario means charCount == len(word)
            if charCount == len(word):
                return True
            if (r >= ROWS or c >= COLS
                or r < 0 or c < 0 or
                word[charCount] != board[r][c] or
                (r,c) in path):
                return False
            
            path.add((r,c))
            res = (dfs(r + 1, c, charCount + 1) or
                dfs(r - 1, c, charCount + 1) or
                dfs(r, c + 1, charCount + 1) or
                dfs(r, c - 1, charCount + 1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
            