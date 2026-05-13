from bisect import bisect_left

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return -1 if target != nums[0] else 0

        l, r = 0, n - 1

        k = n - 1
        while nums[l] > nums[r]:
            m = (l + r) // 2
#            # print(f"l is {l}, r is {r}, m is {m}, nums[l] is {nums[l]}, nums[r] is {nums[r]}")

            if l == m:
                k = l
                break

            if nums[l] < nums[m]:
                l = m
            else:
                r = m

#        print(f"k is {k}")

        base_idx = 0 if nums[0] <= target <= nums[k] else k + 1
        new_nums = nums[:k + 1] if nums[0] <= target <= nums[k] else nums[k + 1:]
#        print(f"new nums is {new_nums} and base_idx is {base_idx}")

        idx = bisect_left(new_nums, target)
        if idx + base_idx < n and nums[base_idx + idx] == target:
            return base_idx + idx

        return -1

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([4,5,6,7,0,1,2], 0),
        ([4,5,6,7,0,1,2], 1),
        ([4,5,6,7,0,1,2], 3),
        ([4,5,6,7,0,1,2], 4),
        ([4,5,6,7,0,1,2], 7),
        ([4,5,6,7], 6),
        ([1], -1),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.search(*test)
        print(answer)
