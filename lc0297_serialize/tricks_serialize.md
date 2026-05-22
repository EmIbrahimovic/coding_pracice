---
strongly-connected:
- "[[bfs]]"
- "[[tree]]"
tags:
- problem
favorite: False
---

# LeetCode 297. serialize

i'm thinking of doing this in layers, the way that a heap orders its stuff in memory

root -> l_child, r_child
root index i - start from index 1
l_child -> 2i
r_child -> 2i + 1 or something like that

1 -> 2 3
2 -> 4 5 
3 -> 6 7

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
and then lshift?

recursively???
(node, index)
if i am none, set ind
array[index] = node.value
recurse(node.left, 2 x index)
recurse(node.right, 2 x index + 1)
> problem: i don't know how much space to allocate initially.

iteratively.
```pseudocode
send (node, index) to current level
while current level not empty:
for node, index in current level:
if node not none ...
if node not none and node not leaf: add rchild to next level, lchild to next level
if next level not empty
for node, index in current level:
if node is none or node is leaf: add children to next level

curr level = next level
return arr
```

keep an array: current level, next level
pass through current level iteratively, add children incl none to next level if the node is NOT a leaf
after all this if next level is empty, terminate
otherwise go through current level again and check who was a leaf node and add Nones in place of their children

> deserialize:

```pseudocode
define recurse(index):
if arr[i] == null: return null
node = treenode(array[index])
lchild = recurse(2 x index)
rchild = recurse(2 x (index + 1))
node.lchild, node.rchild set
return node
```

---

alternative apprch: (node id, node val, child right id or None, child left id or None)
give ids of incremental value
- put it in topological order

deserialize: go from the last node, create them and put them in a dict id -> node
that way because it's reverse topological, we'll have the children ready before the parent needs them

## approach lessons

the second approach definitely works, however there is a middle approach between these two: simple BFS

add nodes to the array as you're traversing through them through BFS, including null children. but, if a node is null itself, don't add it to the array

then, as you're deserializing, also perform a bfs: if i see a node, i know i'll expect its left and right child to show up after all the nodes currently in my queue. 

lekcija: kad skontas komplikovano rjesenje koje zauzima puno memorije za nesto sto realno ne treba uopste da se pojavi u memoriji - probaj naci pojednostavljenje

dodatno pamcenje! dekodiranje koje zna nesto o redoslijedu u kojem enkodiranje fercera

## cpp optimizations


