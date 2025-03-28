from typing import List


class Solution:
    def containeDuplicate(self, nums: List[int]):
        if len(set(nums)) == len(nums):
            print('false')
        else:
            print('true')


sol = Solution()
sol.containeDuplicate([1, 2, 3, 4])
sol.containeDuplicate([1, 2, 3, 1])
