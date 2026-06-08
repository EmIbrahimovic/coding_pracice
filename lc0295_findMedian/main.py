import heapq as hpq
from sortedcontainers import SortedList

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class MedianFinder:

    def __init__2(self):
        self.n = 0
        self.smallestHalf = []
        self.largestHalf = []

    def addNum2(self, num:int) -> None:
        self.n += 1
        if len(self.largestHalf) == 0 and len(self.smallestHalf) == 0:
            self.smallestHalf.append(num)
            return
        if len(self.largestHalf) == 0:
            if num > self.smallestHalf[0]:
                self.largestHalf.append(num)
            else:
                self.largestHalf.append(self.smallestHalf[0])
                self.smallestHalf[0] = num
            return
        
        if num >= self.largestHalf[0]:
            hpq.heappush(self.largestHalf, num)
            if len(self.largestHalf) == len(self.smallestHalf) + 2:
                smallestLarge = hpq.heappop(self.largestHalf)
                hpq.heappush_max(self.smallestHalf, smallestLarge)
        if num <= self.smallestHalf[0]:
            hpq.heappush_max(self.smallestHalf, num)
            if len(self.smallestHalf) == len(self.largestHalf) + 2:
                largestSmall = hpq.heappop_max(self.smallestHalf)
                hpq.heappush(self.largestHalf, smallestLarge)

    def findMedian2(self) -> float:
        if self.n % 2 == 0:
            return (self.smallestHalf[0] + self.largestHalf[0]) / 2

        if len(self.smallestHalf) > len(self.largestHalf):
            return self.smallestHalf[0]
        return self.largestHalf[0]
    
    def __init__(self):
        myList = SortedList()

    def addNum(self, num: int) -> None:
        myList.insert(num)

    def findMedian(self) -> float:
        if len(myList) % 2:
            return myList[len(myList) // 2 + 1]
        return (myList[len(myList) / 2] + myList[len(myList) / 2 + 1]) / 2


class Solution:
    def findMedian(self, inputs) -> None:
        out: None

        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [(MedianFinder.addNum, 1), (MedianFinder.addNum, 2), (MedianFinder.findMedian,), (MedianFinder.addNum, 3), (MedianFinder.findMedian, )],
        ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        finder = MedianFinder()
        for cmdd in test:
            c, args = cmdd
            print(c(finder, *args))

