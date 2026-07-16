---
strongly-connected:
  - "[[tree]]"
  - "[[inorder traversal]]"
  - "[[morris traversal]]"
tags:
favorite: false
---
# morris traversal

algorithm for finding an in-order traversal for a tree without recursion (call stack) or an explicit stack.

exploits the fact that finding the [[predecessor]] in an [[inorder traversal]] is really simple in one case:
> when the node has a left child, its predecessor is found by walking to that child, and then successively walking to the right child of the current node. if the curr node doesn't have one, it IS the predecessor

exploits the fact that to find the inorder traversal you need to successively find the successor. finding the [[successor]] in an [[inorder traversal]] is really easy in one case:
> if the current node has a right child, walk to the child and successively walk to the current node's _left_ child.

finally this is combined with the fact that if you don't have a left child, or you entered a node through its predecessor, you can add it to the predecessor.

---

combine to get:

if the root doesn't have a left child, add it to the traversal, and walk right. (the right will either exist organically, if we returned from a lower node into a parent that has a right child; or if we artificially created a link from a leaf to its successor)
_otherwise if the root has a left child_
find its predecessor.
either we just entered through the predecessor and need to add the curr node to traversal and remove the link from the predecessor and walk right
or we need to create the link from predecessor to current node and walk left.