class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #trying single pass
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key is (r // 3, c //3) to get 1 of 9 squares

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                #need to see if its been seen before
                if (board[r][c] in rows[r] or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


                #if not seen add to all row, sqr, col set
