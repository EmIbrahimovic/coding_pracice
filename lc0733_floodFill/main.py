from typing import List
from deepcopy import deepcopy
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        old_color = image[sr][sc]
        def ff_helper(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return
            
            if image[r][c] == color or image[r][c] != old_color:
                return
            
            image[r][c] = color
            ff_helper(r + 1, c)
            ff_helper(r - 1, c)
            ff_helper(r, c - 1)
            ff_helper(r, c + 1)
        
        ff_helper(sr, sc)
        return image


if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.floodFill(*test)
        print(answer)
