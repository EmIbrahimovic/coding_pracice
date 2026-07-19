from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sums = [1]
        suffix_sums = [1]

        for i in range(len(nums)):
            psum = prefix_sums[-1] * nums[i]
            prefix_sums.append(psum)

            ssum = suffix_sums[-1] * nums[len(nums) - 1 - i]
            suffix_sums.append(ssum)

        suffix_sums.reverse()

        nsums = []
        for i in range(len(nums)):
            nsums.append(prefix_sums[i] * suffix_sums[i + 1])

        return nsums

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,2,3,4], ),
        ([-1,1,0,-3,3], ),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.productExceptSelf(*test)
        print(answer)
