---
strongly-connected:
- "[[dynamic programming]]"
- "[[subset sum]]"
- "[[bitmask tricks]]"
tags:
- problem
favorite: False
---

# LeetCode 416. canPartition



## approach lessons

what i did is a nice simple top down dp.

other possible approaches is a nice simple bottom-up dp with a set keeping which 
sums we've been able to achieve (bc the i actually does not matter)

an interesting optimization is possible using bitshifting:
> keep your set of achieved numbers not a set but as a bitset (1 for achievable 0 for not)
> then, when we go to number i + 1, to get all the new achievable sums, shift the old bitset
> new_number times to the left. then or that with the old bitset to get all achievable sums.
> every time, simply ask whether bit [target] is on

## cpp optimizations


