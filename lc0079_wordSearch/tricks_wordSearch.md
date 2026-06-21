---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# LeetCode 79. wordSearch

simple backtracking. start from every letter and see if you can find the word around it: 
* it's ok because it's easy to prune. only 4 options for direction and a clear sign when you should continue forward
* branching factor is at most 4, most of the times 3 or less because of visited limitations
* worst case, visit every endpoint in the len(word) square around each letter

interesting question: how would you mroe accurately analyze the the complexity of this algorithm.
how would you improve complexity: 
```
AAAAAA
AAAAAA
AAAAAA
AAAAAA
AAAAAB

word: AAB
```
find letter in word which appears the least in board. go only though instances of that letter on board
and start bidirectional searches out of it. (search for BAA, BCC if word is AABCC; tricky if AABAC or even AABAA) - 
search for one half, keep visited; search for other. do a handoff after the first half. 

## approach lessons



## cpp optimizations


