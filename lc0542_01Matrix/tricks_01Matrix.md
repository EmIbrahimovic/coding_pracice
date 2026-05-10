---
strongly-connected:
- "[[dynamic programming]]"
- "[[dp path cost]]"
tags:
- problem
favorite: True
---

# LeetCode 542. updateMatrix



## approach lessons

started off with a kind-of 4-directional dp

didn't work (wasn't taking into account paths that had two directions) - did bfs from 0s

the correct approach is 2 2-directional dps
the first one - looking only at paths that use -> V. then, the second one, looking at the 
paths which use all directions but finish in a <- or A move.

insight: a path will never contain both A and V or both -> and <-. hence if a path ends on 
A, then it only used the dp values from BELOW. similarly, if a path ends on <-, it only used
the values of dp coming from the right. that's why the second dp can start from the lower right
corner and move up and left. 

insight: equivalence of paths. a path that goes from square x to y and moves ^^^^^----> is just 
as long as a path that starts from square x and moves ---->^^^^^. So we y will find out about 
square x through the bottom square!

think about it as square y finding out about relevant squares x.

## cpp optimizations


