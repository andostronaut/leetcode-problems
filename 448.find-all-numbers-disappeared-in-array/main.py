from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        set_nums = set(nums)
        ret = []

        for idx in range(1, len(nums) + 1):
            if idx not in set_nums:
                ret.append(idx)

        print(ret)


sol = Solution()
sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
sol.findDisappearedNumbers([1, 1])
