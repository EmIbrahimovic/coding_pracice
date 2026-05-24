from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def sprialMatrix(self, matrix:List[List[int]]) -> List[int] :
        dir = 0
        dir_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur = 0, 0
        traversal = []

        n, m = len(matrix), len(matrix[0])
        def is_valid(coor):
            r, c = coor
            return 0 <= r < n and 0 <= c < m and matrix[r][c] is not None
        def update_coor(coor, d):
            return coor[0] + d[0], coor[1] + d[1]

        while len(traversal) < n * m:
            traversal.append(matrix[cur[0]][cur[1]])
            matrix[cur[0]][cur[1]] = None
            
            if not is_valid(update_coor(cur, dir_vectors[dir])):
                dir = (dir + 1) % 4
            
            cur = update_coor(cur, dir_vectors[dir])
        
        return traversal

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])

        i = 0
        j = -1
        spiral = []
        while n and m:
            for _ in range(m):
                j+=1
                spiral.append(matrix[abs(i)][abs(j)])
            i*=-1
            n-=1
            for _ in range(n):
                i+=1
                spiral.append(matrix[abs(i)][abs(j)])
            m-=1
            j*=-1

        return spiral

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1,2,3],[4,5,6],[7,8,9]], ),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.sprialMatrix(*test)
        print(answer)

