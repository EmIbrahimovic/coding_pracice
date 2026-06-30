from typing import List, Optional

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def isValidBST(self, root: Optional[TreeNode], minVal=None, maxVal=None) -> bool:
        if root is None:
            return True
        
        if minVal is not None and root.val <= minVal:
            return False

        if maxVal is not None and root.val >= maxVal:
            return False

        if not self.isValidBST(root.left, minVal=minVal, maxVal=root.val):
            return False
        
        if not self.isValidBST(root.right, minVal=root.val, maxVal=maxVal):
            return False
        
        return True


if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.isValidBST(*test)
        print(answer)
