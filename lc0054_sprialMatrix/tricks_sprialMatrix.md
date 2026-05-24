---
strongly-connected:
- "[[ad hoc]]"
tags:
- problem
favorite: False
---

# LeetCode 54. sprialMatrix

dfs? visited matrix (or just know which step of the spiral you're on and when to stop)
cycle through the directions `right`, `down`, `left`, `up` until we can't go on anymore

```
cur = 0,0
dir = 0
dir_order = r, d, l, u
visited = empty matrix
dir_vectors
traversal = []
while len(traversal) < nxm:
    if cur + dir_vector[dir] is visited or invalid:
        dir = dir + 1 mod 4
    update cur
    add to traversal
return traversal
```

what could go wrong? nothing tbh... memory consumption is possibly an issue? but we could modify the
matrix in place. but what if we're not allowed to do that?
then math out which index is supposed to be visited at which step.

## approach lessons

there's also a cool solution that multiplies i, j by -1 every time a row/col change is due, keeps adding 1
until you hit the row/col lim(which decreases by 1 every time) and appends mat[abs(i)][abs(j)] every step

## cpp optimizations


