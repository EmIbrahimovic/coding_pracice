---
strongly-connected:
  - "[[]]"
  - "[[dp simple]]"
  - "[[number of paths]]"
  - "[[combinatorics]]"
tags:
  - problem
favorite: false
---

# LeetCode 62. uniquePaths
easy version of the: coming from any direction problem. we've got it here [[tricks_01Matrix]]

3
extremely standard dp.

to get to `[i][j]` i move in from `[i - 1][j]` or `[i][j - 1]`. every path that comes in from either of those is distinct (last step is distinct). thus just add the num of those paths.

alternatively - theres also a math formula. its (n + m) choose n. 

## approach lessons



## cpp optimizations

specifically for space-optimized dps:
```
class Solution:
    def nchoosek(self, n, k):
        k = k if 2*k < n else n - k
        num = 1
        for i in range(n - k + 1, n + 1):
            num *= i
        denom = 1 
        for i in range(1, k + 1):
            denom *= i
        return num // denom

    def uniquePaths(self, m: int, n: int) -> int:
        return self.nchoosek(m + n - 2, n - 1)
```