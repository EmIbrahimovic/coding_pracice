---
strongly-connected:
- "[[dp simple]]"
- "[[string search]]"
---

# LeetCode 139. wordBreak

i'm thinking the best strat would be some kind of trie for the dictionary; but it's max length 20 so it's not even necessary

for every index in the haystack and every length of needle, check whether the substring starting at index of length matches any of the needles.
then, recurse on the string that's leftover.

the search space is huge this way. we could dp on it though. is it possible to split on every prefix.

pseudocode:
```
dp[0 ... n] = 0
dp[0] = 1
for i in 0 .. n:
    for each needle:
        if haystack[i - len(needle) : i] == needle:
            dp[i] or= dp[i - len(needle) - 1]
            if dp[i]: break

return dp[0]
```

## approach lessons

the editorial for this is really nice and presents some nice alternative dps, as well as a trie optimization.


## cpp optimizations


