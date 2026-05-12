from typing import Optional

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs_down(self, node: TreeNode, distance, parent):
        if node is None:
            return
        for child in (node.left, node.right):
            if child is None:
                continue
            parent[child] = node
            distance[child] = distance[node] + 1
            self.dfs_down(child, distance, parent)

    def dfs_up(self, node: TreeNode, distance, parent):
        if node is None:
            return
        
        for neigh in (node.left, node.right, parent[node]):
            if neigh is not None and neigh not in distance:
                distance[neigh] = distance[node] + 1
                self.dfs_up(neigh, distance, parent)


    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        parent = {root: None}
        distance = {root: 0}
        self.dfs_down(root, distance, parent)

        farthest = root
        for node in distance:
            if distance[node] > distance[farthest]:
                farthest = node

        distance = {farthest: 0}
        self.dfs_up(farthest, distance, parent)
        return max(distance.values())


    def max_path(self, root: TreeNode):
        if root is None:
            return 0, -1
        
        lchild_d, lchild_h = self.max_path(root.left)
        rchild_d, rchild_h = self.max_path(root.right)

        print(root.val, max(
            lchild_d, rchild_d,
            lchild_h + rchild_h + 2
        ), max(lchild_h, rchild_h) + 1)
        return max(
            lchild_d, rchild_d,
            lchild_h + rchild_h + 2
        ), max(lchild_h, rchild_h) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.max_path(root)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),),
        (TreeNode(1, TreeNode(2), None), )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.diameterOfBinaryTree(*test)
        print(answer)

