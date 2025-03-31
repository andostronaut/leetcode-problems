from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]):
        if len(set(nums)) == len(nums):
            print('false')
        else:
            print('true')


sol = Solution()
sol.contains_duplicate([1, 2, 3, 4])
sol.contains_duplicate([1, 2, 3, 1])
