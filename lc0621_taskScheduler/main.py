from typing import List
from collections import Counter
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def leastInterval(self, tasks: List[int], n: int) -> int:
        cnt = Counter(tasks)
        print(cnt)
        vals = list(cnt.values())
        vals.sort()
        print(vals)

        tally = 0
        for i in range(len(vals)):
            v = vals[i]
            for j in range(i, min(i + n + 1, len(vals))):
                vals[j] -= v
                tally += v
            num_caught = min(i + n + 1, len(vals)) - i + 1
            tally += v * (n + 1 - num_caught)

        return tally

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["A","A","A","B","B","B"], 2),
        (["A","C","A","B","D","B"], 1),
        (["A","A","A", "B","B","B"], 3),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.leastInterval(*test)
        print(answer)
