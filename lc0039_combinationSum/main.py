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

        def _combinationSum(i, t):
            if t == 0:
                return [[]]
            if i < 0:
                return []
            
            answer = []
            for k in range(t // candidates[i] + 1):
                answer.extend(
                    combo + [candidates[i]] * k 
                    for combo in _combinationSum(i - 1, t - k * candidates[i])
                )
            
            return answer

        return _combinationSum(n - 1, target)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        def _combinationSum(i, t):
            if t < 0:
                return []
            if t == 0:
                return [[]]
            if i < 0:
                return []
            
            answer = []
            answer.extend(
                [candidates[i]] + combo for combo in _combinationSum(i, t - candidates[i])
            )
            answer.extend(_combinationSum(i - 1, t))
            
            return answer

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
