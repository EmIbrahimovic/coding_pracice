from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, cnt = nums[0], 1

        for e in nums:
            if e == el:
                cnt += 1
            
            if e != el and cnt > 0:
                cnt -= 1
            
            if e != el and cnt == 0:
                el = e
                cnt = 1

        return el
    
    def majorityElement2(self, nums: List[int]) -> int:
        el, cnt = nums[0], 1

        for e in nums:
            if cnt == 0:
                el = e
            
            if e == el:
                cnt += 1
            else:
                cnt -= 1

        return el

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3,2,3], ),
        ([2,2,1,1,1,2,2], ),
        ([1], ),
        ([2, 2, 2, 1, 1, 1, 2], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.majorityElement(*test)
        print(answer)

