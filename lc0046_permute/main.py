from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]] :
        
        allperms = []
        def _permute(i):
            if i == -1:
                allperms.append(nums[:])
                return
            
            _permute(i - 1)
            for j in range(i):
                if i % 2 == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    nums[i], nums[0] = nums[0], nums[i]
                _permute(i - 1)
        
        _permute(len(nums) - 1)
        return allperms

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3], ),
        ([1], ),
        ([], ),

    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.permute(*test)
        print(answer)

