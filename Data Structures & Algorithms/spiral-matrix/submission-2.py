class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        r, c = 0, 0   # top and left edges; ROWS and COLS are bottom and right (exclusive)

        while r < ROWS and c < COLS:
            # across the top row
            for i in range(c, COLS):
                res.append(matrix[r][i])
            r += 1

            # down the right column
            for i in range(r, ROWS):
                res.append(matrix[i][COLS - 1])
            COLS -= 1

            # back along the bottom row (only if a row remains)
            if r < ROWS:
                for i in range(COLS - 1, c - 1, -1):
                    res.append(matrix[ROWS - 1][i])
                ROWS -= 1

            # up the left column (only if a column remains)
            if c < COLS:
                for i in range(ROWS - 1, r - 1, -1):
                    res.append(matrix[i][c])
                c += 1

        return res