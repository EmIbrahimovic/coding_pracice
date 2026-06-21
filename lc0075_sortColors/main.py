from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def sortColors(self, inputs) -> None :

        c = [0, 0, 0]
        for cc in inputs:
            c[cc] += 1
        
        ind = [0, c[0], c[0] + c[1]]
        lim = [c[0], c[0] + c[1], c[0] + c[1] + c[2]]
        while True:
            print(ind)
            print(inputs)
            
            cond = True
            for i in range(3):
                while ind[i] < lim[i] - 1 and inputs[ind[i]] == i:
                    ind[i] += 1
                if ind[i] != lim[i] - 1:
                    cond = False
            
            if cond:
                break

            swapt = False
            # swap anything
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    if inputs[ind[i]] == j and inputs[ind[j]] == i:
                        inputs[ind[i]] = i
                        inputs[ind[j]] = j
                        swapt = True
                        break
                if swapt:
                    break

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([0, 0, 0, 1, 1, 1, 2, 2, 2],),
        ([0, 1, 0, 1, 0, 1, 2, 2, 2],),
        ([2, 1, 0, 1, 1, 0, 2, 1, 2],),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.sortColors(*test)
        print(answer)

