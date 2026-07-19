---
strongly-connected:
- "[[scheduling]]"
- "[[greedy]]"
- "[[difficult greedy]]"
tags:
- problem
favorite: True
---

# LeetCode 621. taskScheduler

not obvious to prove greedy solution. yikes problem

similar
```
767. Reorganize String
1054. Distant Barcodes
1405. Longest Happy String
1953. Maximum Number of Weeks for Which You Can Work
2335. Minimum Amount of Time to Fill Cups
358. Rearrange String k Distance Apart (premium)
984. String Without AAA or BBB
```

imas 
```
xa x A
xb x B
xc x C
xd x D
xe x E
...
n = 4
```

in an interval of length 4, you can fit 4 unique tasks
A B C D - A B C D - ...
i mean... basically just go down the list. once you run out but still have some cnt, just idle.

that's how to simulate it. the greedy would work trust. since you need either max of all xs cycles. or the sum of all xs / num xs.

3a 3b n = 2 (essentially 3)
minimum 3 length 3 cycles (with a caveat)

ok essentially its: sum of xs plus optional padding; q is, how much padding

1) tally everything
2) if there's more than n task types, find task with min xs. 
3) if there's less than or equal to n task types; 

2 B 3 A
n = 2

num caught = min(i + n + 1, len(vals)) - i + 1
2 + 2 + (vals[i] * (n + 1 - num_caugt))

## approach lessons



## cpp optimizations
