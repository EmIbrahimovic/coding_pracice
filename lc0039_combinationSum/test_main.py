from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        memo = [[None for _ in range(target + 1)] for _ in range(n)]

        def _combinationSum(i, t):
            if memo[i][t] is not None:
                return memo[i][t]
            if t == 0:
                return [[]]
            if i < 0:
                return []

            memo[i][t] = []
            if t == 0:
                memo[i][t].append([])
            else:
                for k in range(t // candidates[i] + 1):
                    memo[i][t].extend(
                        combo + [candidates[i]] * k 
                        for combo in _combinationSum(i - 1, t - k * candidates[i])
                    )
            
            print(i, t)
            print(memo[i][t])
            return memo[i][t]

        return _combinationSum(n - 1, target)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2,3,6,7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.combinationSum(*test)
        print(answer)
