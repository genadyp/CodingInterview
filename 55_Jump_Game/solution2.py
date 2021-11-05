"""
Runtime: 508 ms, faster than 59.54% of Python3 online submissions for Jump Game.
Memory Usage: 15.1 MB, less than 91.37% of Python3 online submissions for Jump Game.
"""

from typing import List

class Solution:        
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
    
        cursor = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if cursor <= i:
                    return False
                #zero_idx = i

            if i + nums[i] >= len(nums) - 1:
                return True
            cursor = max(cursor, i + nums[i])
        
        

if __name__ == '__main__':
    testcases = [
        {
            'inputs': {
                'nums': [1,1,2,2,0,1,1]
            },
            'expected': True
        },
        {
            'inputs': {
                'nums': [2,3,1,1,4],
            },
            'expected': True
        },
        {
            'inputs': {
                'nums': [3,2,1,0,4],
            },
            'expected': False
        }    ]

    for t in testcases:
        solution = Solution()
        result = solution.canJump(**t['inputs'])
        assert result == t['expected'], f'Got {result} - Expected {t["expected"]}'

    print('Success')
     
