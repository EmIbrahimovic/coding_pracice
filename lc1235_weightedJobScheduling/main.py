from typing import List
from bisect import bisect_right
from dataclasses import dataclass

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

@dataclass
class Interval:
    s: int
    e: int
    p: int

class Solution:
    def weightedJobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int :
        max_profit = [0] * len(startTime) 

        intervals = [Interval(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        intervals.sort(key=lambda a: a.e)

        for i, interval in enumerate(intervals):
            s, e, p = interval.s, interval.e, interval.p
            j = bisect_right(intervals, s, key=lambda itvl: itvl.e)
            j -= 1

            if j == -1:
                max_profit[i] = max(p, max_profit[i - 1])
            else:
                max_profit[i] = max(max_profit[i - 1], max_profit[j] + p)

        if len(intervals) == 0:
            return 0
        return max_profit[len(intervals) - 1]

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([], [], []),
        ([1], [2], [5]),
        ([1,2,3,3], [3,4,5,6], [50,10,40,70]),
        ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]),
        ([1,1,1], [2,3,4], [5,6,4]),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.weightedJobScheduling(*test)
        print(answer)

