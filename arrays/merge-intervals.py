from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0], reverse=True)
        merged: List[List[int]] = []
        while intervals:
            x1, y1 = intervals[-1]
            while intervals and intervals[-1][0] <= y1:
                y1 = max(y1, intervals[-1][1])
                intervals.pop()
            merged.append([x1, y1])
        return merged
