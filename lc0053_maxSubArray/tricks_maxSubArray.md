---
strongly-connected:
  - "[[]]"
  - "[[kadane's algorithm]]"
  - "[[subarray]]"
  - "[[dp simple]]"
  - "[[divide and conquer]]"
tags:
  - problem
favorite: false
---

# LeetCode 53. maxSubArray

[[kadane's algorithm]]

get the array, cumulative sum it up.
when the sum goes negative reset it
keep track of max sum from there on

why does this work? dynamic programming and local greedy property.
dp[i] = max(dp[i - 1] + el[i], el[i])
> max subarray sum necessarily ending with index i 
> the sum ending with i also picks up element i - 1. 

## approach lessons

there's also a (maybe) more parallelisable, divide and conquer solution
take the middle element out: the opt sol is either all left half or all right half or some left, some right plus middle. meaning that in both the left half and the right half we HAVE TO INCLUDE the middle.
so we get a cumulative sum starting from the middle element. find the max sum incl right els and max sum incl left els.
(seems suspiciously inefficient)
$$
T(n) = T(n/2)\times2 + O(n)
$$
$$
T(n) = O(n^2)
$$
the depth is $O(\log{n})$ though. this means that with $\log n$ processors we could finish this in $O(n)$ or less

## cpp optimizations


