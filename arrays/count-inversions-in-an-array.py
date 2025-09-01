from typing import List

class Solution:
    def count_inversions(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums)-1)

    def merge(self, nums: List[int], low: int, mid: int, high: int) -> int:
        count = 0
        temp: List[int] = []
        left, right = low, mid+1

        while left <= mid and right <= high:
            if nums[right] <= nums[left]:
                temp.append(nums[right])
                count += mid - left + 1
                right += 1
            else:
                temp.append(nums[left])
                left += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(len(temp)):
            nums[low+i] = temp[i]

        return count

    def merge_sort(self, nums: List[int], low: int, high: int) -> int:
        count = 0
        if low < high:
            mid = (low + high) // 2
            count += self.merge_sort(nums, low, mid)
            count += self.merge_sort(nums, mid+1, high)
            count += self.merge(nums, low, mid, high)
        return count


print(Solution().count_inversions([5, 3, 2, 1, 4]))
