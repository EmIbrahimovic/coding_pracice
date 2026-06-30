from typing import List, Optional

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:

    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if node is None:
            return None
        
        node.left, node.right = node.right, node.left
        self.invertTree(node.left)
        self.invertTree(node.right)

        return node

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]
    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.invertTree(*test)
        print(answer)
