from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m, n = m-1, n-1
        for k in range(m+n+1, -1, -1):
            if n < 0: break
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[m], nums1[k] = nums1[k], nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
