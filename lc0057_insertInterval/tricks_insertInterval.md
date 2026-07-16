---
strongly-connected:
- "[[intervals]]"
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

---

essentially, it's doing an inflight merge. 
if while going through intervals, the start point of the new interval is near the current looping interval,
set the start of the new insert to 

new interval is going to grow to catch all the intervals it completely overlaps, extends or merges.
provided we secure this, insert an existing interval if it comes fully before the new interval.
-> before we've identified what needs to be merged, it's still safe to insert existing inverval if it ends before new interval starts (because it ends before any other interval starts anyway)
if the existin interval comes fully after the new interval - then we've ended its reign, it can no longer be extended or merged
if the existing interval neither fully ends nor fully begins after/before the new interval - then there's some overlapping happening:
> don't append anything, just extend the new interval. to the min of currstart, new interval start and similarly with the end.

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for l, r in intervals:
            if newInterval[0] > r:
                output.append([l, r])
            elif newInterval[1] < l:
                output.append([newInterval[0], newInterval[1]])
                newInterval = [l, r] # this just makes sure we keep inserting intervals; you could just as well set it to [inf, inf + 1]
            else:
                newInterval[0] = min(l, newInterval[0])
                newInterval[1] = max(r, newInterval[1])
        output.append(newInterval)
        return output
```

## approach lessons



## cpp optimizations


