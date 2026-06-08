from typing import List
from collections import defaultdict

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:       
        if len(p) > len(s):
            return []
        if len(s) == 0:
            return []

        cnt_s = defaultdict(int)
        cnt_p = defaultdict(int)
        for i in range(len(p)):
            cnt_s[s[i]] += 1
            cnt_p[p[i]] += 1
        
        abs_diff = sum(abs(cnt_s[l] - cnt_p[l]) for l in set(cnt_s.keys()) | set(cnt_p.keys()))


        indices = []
        if (abs_diff == 0):
            indices.append(0)
        for i in range(0, len(s) - len(p)):
            abs_diff -= abs(cnt_s[s[i]] - cnt_p[s[i]])
            cnt_s[s[i]] -= 1
            abs_diff += abs(cnt_s[s[i]] - cnt_p[s[i]])
            i += len(p)
            abs_diff -= abs(cnt_s[s[i]] - cnt_p[s[i]])
            cnt_s[s[i]] += 1 
            abs_diff += abs(cnt_s[s[i]] - cnt_p[s[i]])
            i -= len(p)
            if abs_diff == 0:
                indices.append(i+1)

        return indices

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abab", "ab"),
        ("cbaebabacd", "abc")
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.findAnagrams(*test)
        print(answer)
