"""
Runtime: 2027 ms, faster than 5.01% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.9 MB, less than 27.71% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
from typing import List

class Solution:
    def __min_idx(self, values: List[int]):
        idx = 0
        for i, v in enumerate(values):
            if v is None:
                continue
            if values[idx] is None or v < values[idx]:
                idx = i
        return idx

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k > len(matrix) * len(matrix):
            raise ValueError(f'k argument equels to {k}. Must be less then {len(matrix)*len(matrix)}')
        if len(matrix) == 1:
            return matrix[0][0]

        count = 0 
        value = None
        dim = len(matrix)
        row_cursors = [-1] * dim
        next_values = [None] * dim
        next_values[0] = matrix[0][0]
        partition_cursor = 1

        while count < k:
            count += 1

            idx = self.__min_idx(next_values)
            value = next_values[idx]

            row_cursors[idx] += 1 
            next_values[idx] = matrix[idx][row_cursors[idx] + 1] if row_cursors[idx] < dim - 1 else None 

            if row_cursors[partition_cursor - 1] > -1 and partition_cursor < dim:
                next_values[partition_cursor] = matrix[partition_cursor][0]
                partition_cursor +=1
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
