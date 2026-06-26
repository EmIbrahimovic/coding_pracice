---
strongly-connected:
- "[[duplicates]]"
- "[[sorting]]"
- "[[set]]"
tags:
- problem
favorite: False
---

# LeetCode 217. containsDuplicate

what are we doing?

assume all numbers 1 to n or?? ok no, any numbers.

simple solution: set/hashmap. set as a hashmap. 
an O(1) memory solution?
sort in-place and compare.


an O(1) sum-style solution? hard to make work in the case of arbitrary numbers:
a1 + a2 + a3 + ... + an 
and if ai != aj for i != j then what?
a1 + a2 + a3 + ... + an-1 = S - an
ai = aj for some two numbers.
ai - aj = 0 for some two numbers

## approach lessons



## cpp optimizations
