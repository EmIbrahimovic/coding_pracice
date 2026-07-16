from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_path = None
        q_path = None
        path = []
        def dfs(node):
            nonlocal p_path, q_path
            if node is None:
                return

            path.append(node)
            if node == p:
                p_path = path.copy()
            if node == q:
                q_path = path.copy()
            if p_path is not None and q_path is not None:
                return

            dfs(node.left)
            dfs(node.right)
            path.pop()
        
        dfs(root)
        ancestor = root
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                ancestor = p_path[i]
            else:
                break

        return ancestor

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.lowestCommonAncestorBinaryTree(*test)
        print(answer)
