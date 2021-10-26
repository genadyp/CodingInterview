'''
Runtime: 220 ms, faster than 50.95% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.8 MB, less than 27.71% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = sum(matrix, [])
        print(result)
        result.sort()
        for i in range(len(result)+1):
            if i==k:
                return result[i-1]
            else:
                continue    


if __name__ == '__main__':
    testcases = [
        {
            'inputs': {
                'matrix': [[1,5,9],[10,11,13],[12,13,15]],
                'k': 8
            },
            'expected': 13
        },
        {
            'inputs': {
                'matrix': [[-5]],
                'k': 1
            },
            'expected': -5
        },
        {
            'inputs': {
                'matrix': [[0,0,0],[2,7,9],[7,8,11]],
                'k': 7
            },
            'expected': 8
        }
    ]

    for t in testcases:
        solution = Solution()
        result = solution.kthSmallest(**t['inputs'])
        assert result == t['expected'], f'Got {result} - Expected {t["expected"]}'

    print('Success')

