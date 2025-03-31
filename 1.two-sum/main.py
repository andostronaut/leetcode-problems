from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int):
        hashMap = {}

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                print([idx, hashMap[diff]])

            hashMap[val] = idx


sol = Solution()
sol.two_sum([2, 7, 11, 15], 9)
sol.two_sum([3, 2, 4], 6)
