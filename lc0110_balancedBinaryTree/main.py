from typing import List, Optional`

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def _isBalanced(self, node) -> bool, int:
            if node is None:
                return True, 0

            hleft, bleft = _isBalanced(root.left)
            hright, bright = _isBalanced(root.right)

            height = max(hleft, hright) + 1
            isbal = bleft and bright and (abs(hleft - hright) <= 1)

            return isbal, height

        return _isBalanced(root)[0]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.balancedBinaryTree(*test)
        print(answer)
