from typing import List
from collections import deque
from math import inf

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def trap2(self, heights: List[int]) -> int :
        """
        There's good things about this approach. There's also bad ones. Namely it doesn't completely work.
        There's issues with:
        * deciding bin border based on adjacent index
        * deciding bin border based on equal heights
        """
        n = len(heights)
        h_right = [-1] * n
        h_left = [-1] * n

        hstack = deque()
        hstack.append((-1, inf))
        for i, h in enumerate(heights):
            while h > hstack[-1][1]:
                hstack.pop()

            if hstack[-1][0] != i - 1 and hstack[-1][1] != h:
                h_left[i] = hstack[-1][0]
            if hstack[-1][1] == h:
                hstack.pop()
            hstack.append((i, h))
        
        hstack.clear()
        hstack.append((-1, inf))
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while h > hstack[-1][1]:
                hstack.pop()

            if hstack[-1][0] != i + 1 and hstack[-1][1] != h:
                h_right[i] = hstack[-1][0]
            if hstack[-1][1] == h:
                hstack.pop()
            hstack.append((i, h))

        bins = set()
        for i, h in enumerate(heights):
            if h_left[i] != -1 and h_right[i] != -1:
                continue

            if h_left[i] != -1 and h_left[i] != i - 1:
                bins.add((h_left[i], i))
            if h_right[i] != -1 and h_right[i] != i + 1:
                bins.add((i, h_right[i]))

        print(bins)
        all_water = 0
        for bin in bins:
            for i in range(bin[0] + 1, bin[1]):
                all_water += min(heights[bin[0]], heights[bin[1]]) - heights[i]
        
        return all_water
    
    
    def trap(self, heights: List[int]) -> int :
        """
        There's good things about this approach. There's also bad ones. 
        """
        n = len(heights)
        pref_max = heights[:]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], heights[i])
        suf_max = heights[:]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], heights[i])

        all_water = 0
        for h, lmax, rmax in zip(heights, pref_max, suf_max):
            all_water += min(lmax, rmax) - h

        return all_water


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], ),
        ([4,2,0,3,2,5], ),
        ([1], ),
        ([1, 2, 3, 2, 1], ),
        ([2, 0, 2], ),
        ([5,5,1,7,1,1,5,2,7,6], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.trap(*test)
        print(answer)

