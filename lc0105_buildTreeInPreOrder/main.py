from typing import List, Optional, Tuple

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        in_index = 0
        path = []
        def constructTree(pre_index: int) -> Tuple[int, TreeNode]:
            nonlocal in_index
            path.append(preorder[pre_index])
            # print(f"preorder element: [{pre_index}], {preorder[pre_index]}")
            # print(f"inorder element: [{in_index}], {inorder[in_index]}")
            # print(f"path: {path}")

            left_child = None
            next_index = pre_index + 1
            if preorder[pre_index] != inorder[in_index]: # and inorder[in_index] not in path:
                left_child, next_index = constructTree(pre_index + 1)

            # at this point preorder[pre_index] = inorder[in_index], since in_index was moved
            node = TreeNode(preorder[pre_index])
            node.left = left_child

            # move to the in-order successor
            in_index += 1

            # there is no successor (end of array) or no right child
            if in_index >= len(inorder) or inorder[in_index] in path:
                return node, next_index

            # there's a right child!
            right_child, next_index = constructTree(next_index)
            node.right = right_child
            path.pop()

            return node, next_index
        
        return constructTree(0)[0]

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3,9,20,15,7], [9,3,15,20,7]),
        ([-1], [-1])
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.buildTree(*test)
        print(answer)

