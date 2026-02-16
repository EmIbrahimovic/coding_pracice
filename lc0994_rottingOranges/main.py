from typing import List
import typing
from collections import deque

class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return -1
        
        m = len(grid[0])

        agenda = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    agenda.append((i, j, 0))
        
        max_dist = 0
        d1 = [-1, 0, 1, 0]
        d2 = [0,  1, 0, -1]
        while agenda:
            r, c, my_dist = agenda.popleft()
            max_dist = max(my_dist, max_dist)

            for dd1, dd2 in zip(d1, d2):
                rr = r + dd1
                cc = c + dd2
                if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] == 1:
                    grid[rr][cc] = 2
                    agenda.append((rr, cc, my_dist + 1))
        

        max_dist = -1 if any(grid[i][j] == 1 for i in range(n) for j in range(m)) else max_dist

        return max_dist

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[2,1,1],[1,1,0],[0,1,1]],),
        ([[2,1,1],[0,1,1],[1,0,1]],),
        ([[0,2]], )
    ]

    for test in tests:
        answer_to_test = sol.orangesRotting(*test)
        print(answer_to_test)
