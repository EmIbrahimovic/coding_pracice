from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]] :
        intervals.sort()

        merged_intervals = []
        if len(intervals) > 0:
            merged_intervals.append(intervals[0])
        for s, e in intervals[1:]:
            if s <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], e)
            else:
                merged_intervals.append([s, e])

        return merged_intervals

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], ),
        ([[1,4],[4,5]], ),
        ([[4,7],[1,4]], ),
        ([[1,4],[2,3]], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.merge(*test)
        print(answer)

