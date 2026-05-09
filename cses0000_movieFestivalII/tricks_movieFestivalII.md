---
strongly-connected:
- "[[greeedy]]"
- "[[activity selection]]"
tags:
- problem
favorite: True
---

# CSES 0. movieFestivalII

how to retreive the max number of overlapping intervals at a given point in time?
i could do like a cumulative sum kinda thing

start and end times:

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7           |
| --- | --- | --- | --- | --- | --- | --- | ----------- |
| 2   | 3   | 4   | 6   | 8   | 11  | 15  | 16          |
| s0  | s2  | e0  | s1  | e1  | e2  | s3  | e3          |
| +1  | +1  | -1  | +1  | -1  | -1  | +1  | -1          |
| 1   | 2   | 1   | 2   | 1   | 0   | 1   | 0           |
|     |     |     |     |     |     |     | end to here |
i'm considering an interval $[s_f, e_f]$
look for where it fits in the list -> say s_f is between 4 and 6. so at the point where sf starts, we have 1 interval. and after that we have either 2 or 1 or 0 intervals.
so we know sf is overlapping 2 of our chosen intervals

say $t_j < s_f <  t_{j + 1} \leq e_f$ 
then: the max num of overlappings is $\max_{f \geq i \geq j} \{sum_i\}$

so we'd like to know after index i, what's the max number of overlapping intervals until the end. every time we insert a new interval, the tail numbers potentially increase

after time t, what's the max number of overlapping intervals in the selection
necessarily, this quantity updates every time we add a new interval. either it increases or stays the same. but the internal state should probably change.
would a segtree be able to solve this? can i insert into a segtree? i can insert into a bst in log n. and perform a rangequery on it as well. does that solve my issue?

oh yeah another issue with this datastruct is that we'd have to insert sf _inside_.
is there a way to insert?

genuinely, if i do a bst does that solve my issue? what if it's unbalanced? we'd have to do an avl tree. 
does a map do what i'd want it to? no bc it doesn't have range queries. 

i don't need every range query. i just need suffix queries.

can i precompute this list?? just exclude the non-chosen intervals from it.
the precomputation would be my cumulative sum list.
i can also do the "suffix" max on this. 
to remove something i'd need to update the vals in cumlist to 00. update the "suffix" max
## approach lessons



## cpp optimizations


