from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        hashMap = {}

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                print([idx, hashMap[diff]])

            hashMap[val] = idx


sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)
sol.twoSum([3, 2, 4], 6)
