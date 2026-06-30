from typing import List, Optional
from collections import deque

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []
        def dfs(node, level):
            if node is None:
                return

            # levels increase one by one
            if level >= len(levels):
                levels.append([])
            levels[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return levels


    def levelOrderBfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        levels = []
        while q:
            node, level = q.popleft()
            if node is None:
                continue

            if level >= len(levels):
                levels.append([])
            levels[-1].append(node.val)

            for child in (node.left, node.right):
                q.append(child, level + 1)

        return levels

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.levelOrder(*test)
        print(answer)
