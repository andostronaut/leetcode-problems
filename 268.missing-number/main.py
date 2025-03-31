from typing import List


class Solution:
    def missing_number(self, nums: List[int]):
        print(sum(range(len(nums) + 1)) - sum(nums))


sol = Solution()
sol.missing_number([3, 0, 1])
sol.missing_number([0, 1])
