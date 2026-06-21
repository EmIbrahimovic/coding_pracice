from typing import List
from itertools import product

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool :
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        def is_valid(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, i):
            if i == len(word):
                return True

            if not is_valid(r, c) or board[r][c] != word[i] or visited[r][c]:
                return False
            
            visited[r][c] = True
            d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for d1, d2 in d:
                rr, cc = d1 + r, d2 + c
                if dfs(rr, cc, i + 1):
                    return True
            
            visited[r][c] = False
            
            return False

        for r, c in product(range(n), range(m)):
            if dfs(r, c, 0):
                return True

        return False

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB')
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.wordSearch(*test)
        print(answer)

