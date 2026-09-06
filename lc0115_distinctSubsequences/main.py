from typing import List
from functools import cache

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def matches(si: int, ti: int) -> int:
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            
            ans = matches(si + 1, ti)
            if s[si] == t[ti]:
                ans += matches(si + 1, ti + 1)
            
            return ans
        
        return matches(0, 0)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.numDistinct(*test)
        print(answer)

