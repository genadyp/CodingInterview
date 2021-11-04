
"""
Runtime: 720 ms, faster than 27.66% of Python3 online submissions for Jump Game.
Memory Usage: 25.1 MB, less than 5.18% of Python3 online submissions for Jump Game.
"""

from typing import List, Set


class Solution:
    def jump(self, idx: int, nums: List[int], visited: Set[int]) -> bool:
        if idx == len(nums) - 1:
            return True
        if len(nums) - idx - 1 <= nums[idx]:
            return True
        if idx in visited:
            return False

        visited.add(idx)

        for length in range(1, nums[idx] + 1):
            if length >= len(nums) - idx:
                return False
            if len(visited) == len(nums) - 1:
                return False                
            if self.jump(idx + length, nums, visited):
                return True

             
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        return self.jump(0, nums, visited)
        

if __name__ == '__main__':
    testcases = [
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
     

