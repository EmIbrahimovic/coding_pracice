from typing import List
from bisect import *

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]] :
        # firstConflict = bisect_left(intervals, newInterval[0], key=lambda a: a[0])
        # lastConflict = bisect_left(intervals, newInterval[1], key=lambda a: a[0])

        # if firstConflict == len(intervals):
        #     intervals.append(newInterval)
        #     return intervals
        # elif firstConflict == 0:
        #     # something
        # else:
        #     firstConflict -= 1

        # intersectsFirst = intervals[firstConflict][1] >= newInterval[0]
        # intersectsLast = intervals[lastConflict][]

        newIntervals = []
        s, e = newInterval
        startMerged = -1
        endMerged = -1
        for si, ei in intervals:
            if si <= s <= ei:
                startMerged = si
                
            if startMerged > 0:
                if si <= e <= ei:
                    endMerged = ei
                    newIntervals.append([startMerged, endMerged])
                    startMerged = -2
                    continue
                elif si <= e:
                    endMerged = e
                    continue
                else:
                    newIntervals.append([startMerged, endMerged])
                    newIntervals.append((si, ei))
                    startMerged = -2
                    continue
            
            if startMerged == -1 and e <= si:
                newIntervals.append(newInterval)
                startMerged = -2
            if startMerged < 0:
                newIntervals.append([si, ei])
        if len(newIntervals) == 0:
            newIntervals.append(newInterval)


        return newIntervals

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
        ([], [1, 1]),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.insert(*test)
        print(answer)

