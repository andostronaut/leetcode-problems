from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]):
        set_nums = set(nums)
        ret = []

        for idx in range(1, len(nums) + 1):
            if idx not in set_nums:
                ret.append(idx)

        print(ret)


sol = Solution()
sol.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
sol.find_disappeared_numbers([1, 1])
