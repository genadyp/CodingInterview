"""
Runtime 67 ms Beats 94.61%
Memory 17.9 MB Beats 5.61%
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2:
            return [0,1]

        cache = dict()
        for i, v in enumerate(nums):
            if v in cache:
                return [cache[v], i]
            else:
                supl = target - v
                cache[supl] = i

