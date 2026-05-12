---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# LeetCode 543. diameterOfABinaryTree

first approach: did the classic double dfs through a tree. the logic is:
the longest path is going to start from the guy farthest away from the root (greedy property).
(lowey starts from a falacious way of looking at things - the longest shortest path is the one
between root and another guy. or two guys farthest away from the root. but they could live 
in the same subtree and that's not great).
> anyway, it's possible to prove that the farthest from root guy has to be on the diamter by 
> contradiction. if diameter is path between x and y, and the farthest guy is z, find the lca
> of x and y. observe what happens when its the root and when its not. and also observe lca(
> x, z) and (y, z)


## approach lessons


however, we specifically have a binary tree and for that one a simple recursion suffices. let
`diam[node]` be the diam of subtree rooted at node.

```
diamter[node] = max(
    max_{child} (diameter[child]),
    max_{child1, child2} (height[child1] + height[child2]) + 2
)
```
(corresponding to cases when the diameter is between nodes that are in the same subtree or node and
when it's between nodes that are in different subtrees; uses the fact that there exists a unique
path between each pair of nodes)

## cpp optimizations


