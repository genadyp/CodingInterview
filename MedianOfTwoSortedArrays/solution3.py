"""
Runtime: 80 ms, faster than 98.74% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 93.55% of Python3 online submissions for Median of Two Sorted Arrays.
"""

from typing import List, Tuple, Optional

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l = nums1 + nums2
        l.sort()
        mid1 = 0
        mid2 = 0
        median = 0
        if len(l)%2 == 0:
            mid1 = len(l)//2
            mid2 = mid1 -1
            median = (l[mid1] + l[mid2])/2
        else:
            mid1 = len(l)//2
            median = l[mid1]
        return median
            
            
if __name__ == '__main__':
    testcases = [
        {
            'inputs': [[3], [-2, -1]],
            'expected': -1.0
        },{
            'inputs': [[1,3], [2, 7]],
            'expected': 2.5
        },
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
        assert result == t['expected'], f'Actual {result} != Expected {t["expected"]}'

    # solution = Solution()

    # lst = [5, 7, 40]
    # value = 50
    # idx = solution.find_index(lst, value)
    # print(f'{lst[0:idx+1] if idx is not None else []} < {value} < {lst[idx+1:] if idx is not None else lst}')

    print('Success')
        