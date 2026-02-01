---
strongly-connected: 
- "[[palindrome]]"
- "[[substrings]]"
- "[[adhoc]]"
- "[[simple dp]]"
---

# LeetCode 5. Longest Plaindromic Substring

i did a dp where `ispal[i][j]` tells us whether s[i .. j] is a palindrome
we need to fill this in by palindrome length, so first fill all `[i][i]`, then all `[i][i + 1]` etc.

## approach lessons

however this has a bit of a catastrophic runtime somehow. 
i think we can shave it down by keeping two vectors (one for palindromes of length l - 2, one for l - 1)

but the solution that seems to work for people is: take an index, consider it a seed - a center. and expand the palindrome from that center. 
for each index have to expand even-length and odd-length palindromes separately.
> **why is this better?**
> it seems like worst-case runtime is going to be just as bad "aaaaa" unless we have a way to stop early when we run into a sequence of equal characters.
> in all other cases, i understand, most seeds will stop after 1 step

## cpp code optimization lessons

assigning a large vector kills your runtime as well?
