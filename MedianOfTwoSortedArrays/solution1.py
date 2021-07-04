from itertools import chain
from typing import List

# Runtime: 132 ms, faster than 12.95% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.8 MB, less than 5.65% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        if not nums1:
            return self.get_median(nums2)
        if not nums2:
            return self.get_median(nums1)
        
        nums1 = [nums1]
        nums2 = [nums2]
        combined_nums = []
        
        while nums1 and nums2:
            left, right = (nums1, nums2) if nums1[0][0] < nums2[0][0] else (nums2, nums1)
            if self._last(left[0]) <= right[0][0]:
                combined_nums.extend(left.pop(0))
            else:
                for e in reversed(self._split_at_median(left.pop(0))):
                    left.insert(0, e)
        if nums1:
            combined_nums.extend(self._flatten(nums1))
        if nums2:
            combined_nums.extend(self._flatten(nums2))
        res = self.get_median(combined_nums)
        return res

                
                
    def _split_at_median(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        else:
            idx = int(len(nums)/2)
            return [nums[:idx], nums[idx:]]

    def _last(self, nums: List[int]) -> int:
        return nums[len(nums)-1]

    def _flatten(self, nums) -> List[int]:
        return chain.from_iterable(nums)

    def get_median(self, nums):
        idx = int(len(nums)/2)
        if len(nums)%2:
            return nums[idx]
        else:
            return (nums[idx-1] + nums[idx])/2
            
            
if __name__ == '__main__':
    testcases = [
        {
            'inputs': [[1,3], [2]],
            'expected': 2.0
        },
        {
            'inputs': [[1,2], [3,4]],
            'expected': 2.5
        },
        {
            'inputs': [[0,0], [0,0]],
            'expected': 0.0 
        },
        {
            'inputs': [[], [1]],
            'expected': 1.0
        },
        {
            'inputs': [[2], []],
            'expected': 2.0
        }
    ]

    for t in testcases:
        solution = Solution()
        result = solution.findMedianSortedArrays(*t['inputs'])
        assert result == t['expected']

    print('Success')
        