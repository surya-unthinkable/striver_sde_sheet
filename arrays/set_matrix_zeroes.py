from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in zero_rows:
            for c in range(cols):
                matrix[r][c] = 0

        for c in zero_cols:
            for r in range(rows):
                matrix[r][c] = 0

