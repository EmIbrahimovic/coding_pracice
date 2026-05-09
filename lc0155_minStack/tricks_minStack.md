---
strongly-connected:
- "[[stack]]"
- "[[min heap]]"
tags:
- problem
favorite: True
---

# LeetCode 155. minStack



## approach lessons

really cute!

key is to divorce yourself from the idea of a min heap - we don't need that

keep two stacks: one for the elements themselves, one for the minimums of the current stack.

e.g.

```
        stack = [3, 5, 8, 1, 7]
stack_of_mins = [3, 3, 3, 1, 1]
```

## cpp optimizations


