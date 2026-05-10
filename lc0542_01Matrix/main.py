from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class Solution:


    def get_dist_mat(self, mat: List[List[int]], dir: tuple[int, int], init: tuple[int, int], end_condition, boundary_condition, reset_indices):
        n, m = len(mat), len(mat[0])
        i, j = init
        running_dist = 1e9
        dists = [[1e9] * m for _ in range(n)]

        while not end_condition(i, j):
            # print(i, j)
            if mat[i][j] == 0:
                running_dist = 0
            else:
                running_dist += 1
            
            dists[i][j] = running_dist

            i += dir[0]
            j += dir[1]
            if boundary_condition(i, j):
                i, j = reset_indices(i, j)
                running_dist = 1e9

        return dists

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        dists_u = self.get_dist_mat(
            mat,
            (-1, 0),
            (n - 1, 0),
            lambda i, j: (j >= m),
            lambda i, j: (i < 0),
            lambda i, j: (n - 1, j + 1)
        )
        dists_d = self.get_dist_mat(
            mat,
            (+1, 0),
            (0, 0),
            lambda i, j: (j >= m),
            lambda i, j: (i >= n),
            lambda i, j: (0, j + 1)
        )
        dists_l = self.get_dist_mat(
            mat,
            (0, -1),
            (0, m - 1),
            lambda i, j: (i >= n),
            lambda i, j: (j < 0),
            lambda i, j: (i + 1, m - 1)
        )
        dists_r = self.get_dist_mat(
            mat,
            (0, +1),
            (0, 0),
            lambda i, j: (i >= n),
            lambda i, j: (j >= m),
            lambda i, j: (i + 1, 0)
        )

        # print(dists_u)
        # print(dists_d)
        # print(dists_l)
        # print(dists_r)
        return [[min(dist_u, dist_d, dist_l, dist_r) 
                 for dist_u, dist_d, dist_l, dist_r in zip(row_u, row_d, row_l, row_r)]
                 for row_u, row_d, row_l, row_r in zip(dists_u, dists_d, dists_l, dists_r)]

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

