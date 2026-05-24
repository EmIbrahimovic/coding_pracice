from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int :
        if not nums:
            return None
        
        curr_sum = -1
        curr_start = 0
        best_sum = -1e9
        best_start = 0
        best_end = -1
        for i, el in enumerate(nums):
            if curr_sum < 0:
                curr_sum = 0
                curr_start = i
            
            curr_sum += el
            
            if curr_sum > best_sum:
                best_sum = curr_sum
                best_start = curr_start
                best_end = i

        print(nums[best_start:best_end + 1])
        return best_sum

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], ),
        ([], ),
        ([0, -1, 2], ),
        ([1], ),
        ([5, 4, -1, 7, 8], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.maxSubArray(*test)
        print(answer)

