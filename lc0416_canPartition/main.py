from typing import List
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        memory = {}
        def _canPartition(i, target):
            if target < 0 or i < 0:
                return False
            if target == 0:
                return True
            if (i, target) not in memory:
                memory[(i, target)] = _canPartition(i - 1, target - nums[i]) or _canPartition(i - 1, target)

            return memory[(i, target)]

        return _canPartition(len(nums) - 1, sum(nums) / 2)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,5,11,5], ),
        ([1,2,3,5], ),
        ([1,2,5], ),
        ([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.canPartition(*test)
        print(answer)

