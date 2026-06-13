---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# LeetCode 57. insertInterval

so what i'm thinking is we binary search the hell out of it.
brute force: single pass of the intervals array, find the intervals which we overlap with.
hence we need to do better than O(n) given the data in the form we have it.

hear this: 
1) find the index i such that si <= s < si+1
    since  ei-1 < si <= ei < si+1 then the new interval could intersect with si but definitely not with si-1 
    check if overlap with si
2) find index j such that sj <= e < sj+1
    then for sure i<=j since s <= e
    in this case newInt possibly overlaps with j (if i<j; also everything in between i and j; debatable on whether i)
    in the case i==j it's possible that e doesn't overlap with anything and simply needs to be inserted

the issue becomes that we have to delete some intervals or create a new array with O(n) intervals. both of which get us to at least O(n). so it's not even worth it
to optimize this stuff

## approach lessons



## cpp optimizations


