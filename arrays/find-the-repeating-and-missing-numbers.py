from typing import List

class Solution:
    def find_repeating_and_missing_numbers(self, nums: List[int]) -> List[int]:
        magic = 0
        for i in range(len(nums)):
            magic ^= nums[i]
            magic ^= i+1

        bit = 0
        while True:
            if magic & 1:
                break
            magic >>= 1
            bit += 1

        g0 = g1 = 0
        for n in nums:
            if (n >> bit) & 1:
                g1 ^= n
            else:
                g0 ^= n
        for i in range(len(nums)+1):
            if (i >> bit) & 1:
                g1 ^= i
            else:
                g0 ^= i

        return [g0, g1]
