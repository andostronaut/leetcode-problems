from typing import List


class Solution:
    def missingNumber(self, nums: List[int]):
        print(sum(range(len(nums) + 1)) - sum(nums))


sol = Solution()
sol.missingNumber([3, 0, 1])
sol.missingNumber([0, 1])
