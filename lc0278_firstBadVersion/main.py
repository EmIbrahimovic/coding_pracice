import typing
from collections import OrderedDict
from bisect import *

class Solution:

    def firstBadVersion(self, n, isBadVersion=lambda x: False) -> int:
        first_bad_version = bisect_left(range(1, n + 1), 1, key=isBadVersion)

        return first_bad_version + 1

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (5, lambda x: x >= 4),
        (1, lambda x: x >= 1),
        (16, lambda x: x >= 2)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.firstBadVersion(*test)
        print(answer)

