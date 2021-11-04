"""
Runtime: 124 ms, faster than 31.91% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 19.5 MB, less than 5.76% of Python3 online submissions for Median of Two Sorted Arrays.
"""

from typing import List, Tuple, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        if not nums1:
            return self.get_median(nums2)
        if not nums2:
            return self.get_median(nums1)
        
        total_size = len(nums1) + len(nums2)
        idx1, idx2 = self.sorted_partition(nums1, nums2, int(total_size/2) + 1)

        nums1_left = nums1[:idx1 + 1] if idx1 is not None else []
        nums2_left = nums2[:idx2 + 1] if idx2 is not None else []

        if total_size % 2:
            return max(*nums1_left, *nums2_left)
        else:
            largest = sorted([*nums1_left[:-3:-1], *nums2_left[:-3:-1]])
            return (largest[-1] + largest[-2]) / 2

    def sorted_partition(self, nums1: List[int], nums2: List[int], size: int) -> Tuple[Optional[int], Optional[int]]:
        if len(nums1) + len(nums2) < size:
            raise Exception(f'Size {size} is bigger then the common size of {nums1} and {nums2}')
        if not nums1:
            return None, size - 1
        if not nums2:
            return size - 1, None
        if size == 1:
            return (0, None) if nums1[0] < nums2[0] else (None, 0)
        
        idx1, idx2 = None, None

        if len(nums1) < len(nums2):
            idx1 = len(nums1) - 1 if len(nums1) < size/2 else int(size/2) - 1
            idx2 = size - idx1 - 2
        else:
            idx2 = len(nums2) - 1 if len(nums2) < size/2 else int(size/2) - 1
            idx1 = int(size/2) - idx2 - 1

        cursor1, cursor2 = None, None

        if nums1[idx1] < nums2[idx2]:
            cursor1 = idx1
            if nums2[0] <= nums1[cursor1]:
                cursor2 = self.find_index(nums2, nums1[cursor1])
        else:
            cursor2 = idx2
            if nums1[0] <= nums2[cursor2]:
                cursor1 = self.find_index(nums1, nums2[cursor2])
        
        if (cursor1 + 1 if cursor1 is not None else 0) + (cursor2 + 1 if cursor2 is not None else 0) == size:
            return cursor1, cursor2
        else:
            size_left = size - (cursor1 + 1 if cursor1 is not None else 0) - (cursor2 + 1 if cursor2 is not None else 0)
            cursor1_part2, cursor2_part2 = self.sorted_partition(nums1[cursor1 + 1 if cursor1 is not None else 0:],
                                                                 nums2[cursor2 + 1 if cursor2 is not None else 0:],
                                                                 size_left)
            if cursor1 is None:
                if cursor1_part2 is not None:
                    cursor1 = cursor1_part2
            elif cursor1_part2 is not None:
                cursor1 += cursor1_part2 + 1

            if cursor2 is None:
                if cursor2_part2 is not None:
                    cursor2 = cursor2_part2
            elif cursor2_part2 is not None:
                cursor2 += cursor2_part2 + 1

            return cursor1, cursor2


    def find_index(self, nums: List[int], value: int) -> Optional[int]:
        if not nums:
            return None
        if nums[0] > value:
            return None
        if len(nums) == 1:
            return 0
    
        mid_idx = int(len(nums) / 2)
        
        if nums[mid_idx] == value:
            return mid_idx
        elif nums[mid_idx] > value:
            return self.find_index(nums[:mid_idx], value)
        else:
            idx = self.find_index(nums[mid_idx + 1:], value)
            return mid_idx + idx + 1 if idx is not None else mid_idx
                

    def get_median(self, nums):
        idx = int(len(nums)/2)
        if len(nums)%2:
            return nums[idx]
        else:
            return (nums[idx-1] + nums[idx])/2
            
            
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
        