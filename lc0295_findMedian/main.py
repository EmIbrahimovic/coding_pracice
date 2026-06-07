import heapq as hpq

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class MedianFinder:

    def __init_(self):
        self.n = 0
        self.smallestHalf = []
        self.largestHalf = []

    def addNum(self, num:int) -> None:
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

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.smallestHalf[0] + self.largestHalf[0]) / 2

        if len(self.smallestHalf) > len(self.largestHalf):
            return self.smallestHalf[0]
        return self.largestHalf[0]


class Solution:
    def findMedian(self, inputs) -> None:
        out: None

        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.findMedian(*test)
        print(answer)
