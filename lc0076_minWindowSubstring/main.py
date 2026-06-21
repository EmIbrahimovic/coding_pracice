from typing import List
from collections import deque, Counter

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def minWindowSubstring(self, s: str, t: str) -> str :
        letter_range = deque()
        letter_count_t = Counter(t)
        letter_count_r = Counter()
        min_range, min_range_l, min_range_r = 1e6, None, None
        letters_missing = len(t)
        
        for i, l in enumerate(s):
            if l not in letter_count_t:
                continue

            if letters_missing and letter_count_r[l] < letter_count_t[l]:
                letters_missing -= 1

            letter_range.append((i, l))
            letter_count_r.update(l)
            while letter_count_r[letter_range[0][1]] > letter_count_t[letter_range[0][1]]:
                letter_count_r.subtract(letter_range[0][1])
                letter_range.popleft()
            
            range_len = letter_range[-1][0] - letter_range[0][0] + 1

            if letters_missing == 0 and range_len < min_range:
                min_range = range_len
                min_range_l = letter_range[0][0]
                min_range_r = letter_range[-1][0]

        if min_range_l == None:
            return ''

        # Construct and return the range
        return s[min_range_l:(min_range_r + 1)]

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ('ADOBECODEBANC', 'ABC'),
        ('aa', 'a'),
        ('a', 'aa'),
        ('', 'abcde'),
        ('ABBBBBBCBA', 'ABC')
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.minWindowSubstring(*test)
        print(answer)

