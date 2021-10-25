from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k > len(matrix) * len(matrix):
            raise ValueError(f'k argument equels to {k}. Must be less then {len(matrix)*len(matrix)}')
        if len(matrix) == 1:
            return matrix[0][0]

        count = 0 
        dim = len(matrix)
        row_cursors = [-1] * dim

        while count < k:
            candidate_row = None
            candidate_value = None
            for i, cursor in enumerate(row_cursors):
                if i == 0: 
                    if cursor < dim - 1:
                        candidate_value = matrix[0][cursor + 1]
                        candidate_row = 0
                elif cursor < row_cursors[i - 1]:
                    value = matrix[i][cursor + 1]
                    if candidate_value is None or value < candidate_value:
                        candidate_value = value
                        candidate_row = i
            row_cursors[candidate_row] += 1
            #print(candidate_value)
            count += 1
            if count == k:
                return candidate_value   

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
     
