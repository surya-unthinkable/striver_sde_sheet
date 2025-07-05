from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [ [1] ]

        for _ in range(1, numRows):
            last = result[-1]
            curr = []

            for j in range(len(last)+1):
                if j != 0 and j < len(last):
                    curr.append(last[j-1] + last[j])
                else:
                    curr.append(1)

            result.append(curr)

        return result
