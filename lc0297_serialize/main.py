from typing import List

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Codec:
    def serialize1(self, root: TreeNode) -> str :
        import json
        arr = [None]

        curr_level = [root]
        next_level = []
        while curr_level:
            has_next = False
            for node in curr_level:
                arr.append(None if node is None else node.val)
                if node is not None:
                    has_next |= node.left is not None
                    has_next |= node.right is not None

            if has_next:
                for node, i in curr_level:
                    if node is None:
                        next_level.append(None)
                        next_level.append(None)
                    else:
                        next_level.append(node.left)
                        next_level.append(node.right)

            curr_level = next_level
            next_level = []

        return json.dumps(arr)

    def deserialize1(self, data):
        import json
        arr = json.loads(data)
        if not isinstance(arr, list):
            return None
        
        def _recurse(index):
            nonlocal arr
            if index >= len(arr) or arr[index] is None:
                return None
            
            node = TreeNode(arr[index])
            node.left = _recurse(index * 2)
            node.right = _recurse(index * 2 + 1)
            return node


        return _recurse(1)

    def serialize(self, root: TreeNode) -> str:

        arr = []
        id = 0

        def _recurse(node):
            nonlocal id
            if node is None:
                return None
            
            left_id = _recurse(node.left)
            right_id = _recurse(node.right)

            arr.append((id, node.val, left_id, right_id))
            id += 1
            return id - 1
        
        _recurse(root)
        import json
        return json.dumps(arr)

    def deserialize(self, data: str):
        import json
        arr = json.loads(data)
        nodes = {}

        for id, val, lid, rid in arr:
            node = TreeNode(val)
            if lid is not None:
                node.left = nodes[lid]
            if rid is not None:
                node.right = nodes[rid]
            nodes[id] = node

        if len(arr) == 0:
            return None
        
        # root_id = arr[-1][0]
        return nodes[id]

if __name__ == "__main__":
    sol = Codec()

    tests = [
        # ('[null, 1, 2, 3]', ),
        (TreeNode(1, TreeNode(2), TreeNode(3)), )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.serialize(*test)
        print(answer)
        answer = sol.deserialize(answer)
        print(answer.val, answer.right.val, answer.left.val)

