from typing import Optional

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def kthSmallestInBST(self, root: Optional[TreeNode], k: int) -> int:
        

        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.kthSmallestInBST(*test)
        print(answer)
