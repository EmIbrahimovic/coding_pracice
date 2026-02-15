---
strongly-connected:
- "[[standard array]]"
---

# LeetCode 15. threeSum

-1 0 1 2 0 -1 4

sort

-1 -1 0 0 1 2 4

desired = 0

1) generate all pair sums and do lookup of third for each number. 

## approach lessons

there's a better way than my count then binary search: you can two pointer in a[i :]
it straigt up gives us n^2 without additional log factors

## python optimizations

defaultdict is good but Counter is better

