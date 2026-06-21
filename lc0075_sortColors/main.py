from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = [0, 0, 0]
        for n in nums:
            c[n] += 1

        b = [0, c[0], c[0] + c[1]]
        e = [c[0], c[0] + c[1], c[0] + c[1] + c[2]]
        i = b
        def finished():
            nonlocal i, e
            return all(ej == ij for ej, ij in zip(e, i))

        while not finished():
            print(nums)
            print(i)
            cands = [(nums[i[j]], i[j]) for j in range(3) if i[j] < e[j]]
            min_eligible = min(cands)
            print(min_eligible)
            
            nums[min_eligible[1]] = nums[i[min_eligible[0]]]
            nums[i[min_eligible[0]]] = min_eligible[0]
            
            for j in range(3):
                while i[j] < e[j] and nums[i[j]] == j:
                    i[j] += 1


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2,0,2,1,1,0], ),
        ([2,0,1],),
        ([],),
    ]


    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.sortColors(*test)
        print(answer)
