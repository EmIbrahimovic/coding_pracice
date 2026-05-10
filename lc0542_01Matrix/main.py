from typing import List
import queue
from math import inf
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class Solution:

    def updateMatrix(self, mat):

        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                mat[r][c] = min(
                    inf if c == 0 else mat[r][c-1],
                    inf if r == 0 else mat[r-1][c]
                ) + 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] == 0:
                    continue
                mat[r][c] = min(
                    mat[r][c],
                    inf if c == n-1 else mat[r][c+1] + 1,
                    inf if r == m-1 else mat[r+1][c] + 1
                )

        return mat

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        agenda = queue.Queue()
        dists = [[1e9 + 10] * m for _ in range(n)]
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if mat[i][j] == 0:
                    dists[i][j] = 0
                    agenda.put((i, j))
        

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while not agenda.empty():
            i, j = agenda.get()
            # print(i, j)

            for d1, d2 in dirs:
                i_n, j_n = i + d1, j + d2
                # if valid(i_n, j_n):
                #     print(dists[i_n][j_n])
                if valid(i_n, j_n) and dists[i_n][j_n] >= 1e9:
                    dists[i_n][j_n] = 1 + dists[i][j]
                    agenda.put((i_n, j_n))
        
        return dists
        

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[0,0,0],[0,1,0],[0,0,0]], ),
        ([[0,0,0],[0,1,0],[1,1,1]], ),
        ([[0,0,1,0,1,1,1,0,1,1],
          [1,1,1,1,0,1,1,1,1,1],
          [1,1,1,1,1,0,0,0,1,1],
          [1,0,1,0,1,1,1,0,1,1],
          [0,0,1,1,1,0,1,1,1,1],
          [1,0,1,1,1,1,1,1,1,1],
          [1,1,1,1,0,1,0,1,0,1],
          [0,1,0,0,0,1,0,0,1,1],
          [1,1,1,0,1,1,0,1,0,1],
          [1,0,1,1,1,0,1,1,1,0]], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.updateMatrix(*test)
        print(answer)

