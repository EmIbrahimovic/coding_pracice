---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# LeetCode 438. findAnagrams

both strings could be long.
i could simply do a running count on s.

sliding window type of counter. specifically a counter of differences between s and p

for each letter cnt_s - cnt_p. and keep a variable that's the sum of squares of these values. 
every time i slide, i increment and decrement appropriate counters. every time i do that, i add and subtract from that running sum thing.
```
abcdefgh
   ^^^

def

...
a 0
b 0
c 0
d 0
e 0
f 0
...
abs_sum = 0
```
when abssum = 0, add to list


## approach lessons



## cpp optimizations
