---
strongly-connected:
  - "[[]]"
  - "[[simple dp]]"
  - "[[number of combinations]]"
  - "[[dp path cost]]"
tags:
  - problem
favorite: false
---

# LeetCode 322. coinChange

to get to `t using the first i coins`, try using 0 coins of type i and `t using i - 1`; try using 1 coins of type i and using `t - c using i`

srtbot
s: t, i
r: `dp[i][t] = min(dp[i][t - c] + 1, dp[i - 1][t])` if both -1, then -1; if one -1, then the other.
t: increasing t and i
b: t = 0 return 0;  t < 0 return -1 (we overshot, didn't get an exact); i = -1 and t != 0, return -1 (special valuei!!)
o: `dp[n - 1][t]`
t: `n t`
## approach lessons

the imporant things for me here are the optimizations

one thing:
* cleverly collect all the possible sums
* there is a max num of coins that we can possibly use and its not giant:
```python
lass Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        coins = [c for c in sorted(coins) if c <= amount]

        ncoins = 0
        rem = 1 << amount
        while coins:
            current = rem
            for coin in coins:
                rem = rem | current >> coin
            
            rem = rem | current
            ncoins += 1

            if rem & 1 > 0:
                return ncoins

            coins = [c for c in coins if c*ncoins < amount]
        
        return -1
```
similar to [[subset sum]]


## cpp optimizations
