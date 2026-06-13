from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int :
    
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            for di, dj in d:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i + di][j + dj] == '1' and not visited[i + di][j + dj]:
                    visited[i + di][j + dj] = True
                    dfs(i + di, j + dj)

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and not visited[r][c]:
                    num_islands += 1
                    dfs(r, c)
                print(visited)

        return num_islands

class SolutionConcise:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], ),
([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
],),
([["1","1","1"],["0","1","0"],["1","1","1"]], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.numIslands(*test)
        print(answer)

