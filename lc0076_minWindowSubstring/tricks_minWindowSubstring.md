---
strongly-connected:
  - "[[substrings]]"
  - "[[sliding window]]"
  - "[[linked list]]"
tags:
  - problem
favorite: false
---

# LeetCode 76. minWindowSubstring

i simulated a sliding window approach with slightly more memory usage and slightly less time. 

my idea:
* have a deque of relevant letters currently contained in the range in s which contains all letters in t
* iterate through letters of s - if it's relevant, add it to deque, increment range-lettercount. then, while the letter at the front of the deque is _extra_ (there's more of it in the range than we need), kick it out
* keep track of the min range length

how did i come to this?
* original idea: for every index i, keep track of the last time each letter in t appeared in s, and over all i's find the one with minimum difference between min and max of those indices
## approach lessons

* you also don't have to keep a letter deque, you can just keep the letter counts and a starting index - probably simpler

## cpp optimizations


