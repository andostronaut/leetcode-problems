from typing import List


class Solution:
    def smaller_number_than_current(self, nums: List[int]):
        temp = sorted(nums)

        d = {}

        for idx, num in enumerate(temp):
            if num not in d:
                d[num] = idx

        ret = []

        for idx in nums:
            ret.append(d[idx])

        print(ret)


sol = Solution()
sol.smaller_number_than_current([8, 1, 2, 2, 3])
sol.smaller_number_than_current([6, 5, 4, 8])
