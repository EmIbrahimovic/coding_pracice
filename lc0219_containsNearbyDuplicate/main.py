from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = min(k, len(nums))
        unique = set(nums[:k])
        if len(unique) < k:
            return True
        for i in range(len(nums) - k):
            unique.add(nums[i + k])
            unique.remove(nums[i])
            if len(unique) < k:
                return True

        return False

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.containsNearbyDuplicate(*test)
        print(answer)
