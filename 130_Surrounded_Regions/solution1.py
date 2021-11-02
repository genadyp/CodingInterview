"""
Runtime: 132 ms, faster than 92.60% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.5 MB, less than 91.42% of Python3 online submissions for Surrounded Regions."""

from typing import List


class Solution:
    def color_region(self, board: List[List[str]], x_start: int, y_start: int, color: str = 'Z'):
        stack = [(x_start, y_start)]
        while stack:
            x, y = stack.pop(0)
            if 0 > x or x >= len(board) or 0 > y or y  >= len(board[0]):
                continue
            if board[x][y] == 'X':
                continue
            if board[x][y] == 'O':
                board[x][y] = color
                stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        h = len(board)
        w = len(board[0])

        if h < 3 or w < 3:
            return

        for i in range(w):
            if board[0][i] == 'O':
                self.color_region(board, 0, i)
            if board[h-1][i] == 'O':
                self.color_region(board, h-1, i)
        for i in range(h):
            if board[i][0] == 'O':
                self.color_region(board, i, 0)
            if board[i][w-1] == 'O':
                self.color_region(board, i, w-1)
        
        for i in range(h):
            for j in range(w):
                if board[i][j] != 'O' and board[i][j] != 'X':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    testcases = [
        {
            'inputs': {
                'board': [["X","X","X","X"],
                          ["X","O","O","X"],
                          ["X","X","O","X"],
                          ["X","O","X","X"]],
            },
            'expected': [["X","X","X","X"],
                         ["X","X","X","X"],
                         ["X","X","X","X"],
                         ["X","O","X","X"]]
        },
        {
            'inputs': {
                'board': [["X"]]
            },
            'expected': [["X"]]
        },
    ]

    for t in testcases:
        solution = Solution()
        solution.solve(**t['inputs'])
        result = t['inputs']['board'] 
        assert result == t['expected'], f'Got {result} - Expected {t["expected"]}'

    print('Success')