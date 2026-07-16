from typing import Optional

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int :
        tour = []

        def _tour(node):
            if len(tour) == k:
                return
            
            if node is None:
                return
            
            _tour(node.left)
            tour.append(node.val)
            _tour(node.right)

        _tour(root)

        return tour[k - 1]

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.kthSmallestInBST(*test)
        print(answer)
