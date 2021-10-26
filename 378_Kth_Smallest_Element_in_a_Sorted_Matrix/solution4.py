'''
Runtime: 4325 ms, faster than 5.01% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.6 MB, less than 90.56% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
from typing import List


class Solution:
    def _index_of_min_value(self, values: List[int]):
        idx = None
        for i, v in enumerate(values):
            if v is None:
                continue
            if idx is None or v < values[idx]:
                idx = i
        return idx

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k > len(matrix) * len(matrix):
            raise ValueError(f'k argument equels to {k}. Must be less then {len(matrix)*len(matrix)}')
        if len(matrix) == 1:
            return matrix[0][0]

        count = 0 
        value = None
        while count < k:
            idx = self._index_of_min_value([r[0] for r in matrix])
            value = matrix[idx].pop(0)
            if not matrix[idx]:
                matrix[idx].append(None)

            count += 1

        return value
            

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

