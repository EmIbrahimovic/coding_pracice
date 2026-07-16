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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        
        allPts = []
        for s, e in intervals:
            allPts.append((s, 'S'))
            allPts.append((e, 'e'))
        
        start_idx = bisect_left(allPts, (ns, 'S'))
        allPts.insert(start_idx, (ns, 'S'))
        end_idx = bisect_right(allPts, (ne, 'e'))
        allPts.insert(end_idx, (ne, 'e'))

        # print(allPts)

        newIntervals = []
        starts = []
        for i, t in allPts:
            if t == 'S':
                starts.append(i)
            else:
                last_start = starts[-1]
                starts.pop()
                if not starts:
                    newIntervals.append([last_start, i])

        return newIntervals

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]] :
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

