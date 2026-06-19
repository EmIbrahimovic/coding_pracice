from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def nchoosek(self, n, k):
        k = k if 2*k < n else n - k
        num = 1
        for i in range(n - k + 1, n + 1):
            num *= i
        denom = 1 
        for i in range(1, k + 1):
            denom *= i
        return num // denom

    def uniquePaths(self, m: int, n: int) -> int:
        return self.nchoosek(m + n - 2, n - 1)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (3, 7),
        (3, 2)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.uniquePaths(*test)
        print(answer)
