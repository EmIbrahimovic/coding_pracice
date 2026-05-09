import typing
from collections import defaultdict, Counter

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def longestPalindrome(self, s: str) -> int :
        
        # cnts = defaultdict(int)
        # for l in s:
        #     cnts[l] += 1
        cnts = Counter(s)

        max_pali = 0
        pot_1 = False
        for l, cnt in cnts.items():
            max_pali += cnt - cnt % 2
            pot_1 = pot_1 or (cnt % 2)
        
        return max_pali + pot_1

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abccccdd", ),
        ("a", ),
        ("ab", ),
        ("aab",)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.longestPalindrome(*test)
        print(answer)

