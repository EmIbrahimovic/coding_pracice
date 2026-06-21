from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]] :
        out = []
        n = len(nums)

        subset = []
        def _subsets(i):
            if i == n:
                out.append(subset.copy())
                return
            
            _subsets(i + 1)
            subset.append(nums[i])
            _subsets(i + 1)
            subset.pop()

        _subsets(0)
        return out
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        for i in range(1 << len(nums)):
            subset = []
            for j in range(len(nums)):
                if (1 << j) & i:
                    subset.append(nums[j])
            out.append(subset)
        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3], ),
        ([0], ),
        ([], ),
        ([1, 2, 3, 4], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.subsets(*test)
        print(answer)

