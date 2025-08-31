from collections import defaultdict
from typing import List

class Solution:
    @staticmethod
    def sortMatrix(grid: List[List[int]]):
        side = len(grid)
        diagonals = defaultdict(list)

        
        for row in range(side):
            for col in range(side):
                key = row - col
                value = grid[row][col]
                diagonals[key].append(value)

        
        for key in diagonals:
            is_reverse = key < 0
            diagonals[key].sort(reverse=is_reverse)

        
        for row in range(side):
            for col in range(side):
                key = row - col
                value = diagonals[key].pop()
                grid[row][col] = value

        return grid



"""Testing of the matrix"""

if __name__ == "__main__":
    grid = [
        [3, 3, 1],
        [2, 2, 1],
        [1, 1, 1]
    ]

    result = Solution.sortMatrix(grid)
    for row in result:
        print(row)