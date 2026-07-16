---
strongly-connected:
  - "[[dutch national flag]]"
  - "[[sorting]]"
  - "[[adhoc]]"
  - "[[in-place sorting]]"
tagsit
  - problem
favorite: true
---

# LeetCode 75. sortColors


```
0 0 0 1 1 1 2 2 2
0 0 0 1 1 1 2 2 2
    ^       ^   ^rR
```

there exists a swap that gets at leas 2 0
    ^  t one number in the right place. do that swap.
if there is a 0 among the 3 numbers, move the 0 to its spot. if there is not and there's a 1, move it to its spot. if there isn't and it's just twos, something is wrong

pseudocode. every pointer has its start and its limit.
it all pointers are past their limit, we've won. 
otherwise, while there is a pointer who's inside their limit:
* loop through the pointers: if the pointer is alive, append (value, index) to a list.
* find the min element in the list. swap it into the place of its current pointer. 
* advance pointers most 

each pointer advances at most num 0, 1, 2 times. = n total
we append elements which are going to be swapped. -> oop. 
about complexity.
at each step we append 3 elements - that's 3n. _but_, at least one element will stay there still. so maybe this swap list is a pending swap list. 

## approach lessons

new algo unlocked: dutch flag. a two pointers approach.
`lo` `mid` `hi` pointers: each keeping track of 0s 1s or 2s in some sense:

lo and mid start at the beginning, high starts at the end of the array.
lo keeps track of the last 0 (everything before lo is a 0)
hi keeps track of the 2s (everything after hi is a 2)
mid keeps track of 1s (everything before mid is all 0s and then all 1s)
between mid and hi is the wild west

mid also points at the current value which needs sorting: 
0) mid is a 0 - swap els at mid and lo (lo points after the latest known 0). increment both mid and lo
1) mid is a 1 - increment mid (it's possible that lo will move over this value at some point. if that's the case, when mid comes across another 0, it will swap it with this 1 and all is well)
2) mid is a 2 - swap els at mid and hi, decrement hi and (increment mid?)

0 0 0 1 1 1 1 - - - - 2 2 2
      ^        ^       ^


0 0 0 1 1 1 1 0 - - - 2 2 2
      ^        ^       ^

0 0 0 1 1 1 1 0 - - - 2 2 2
      ^        ^       ^

lo and hi are points where we extend the subarr of 0s and 2s - shoving them to the sides of the array as you go along. - i was shoving them to their rightful spots as i went along. swapping with hi is just appending to 2s. swapping with 0 is just appending a certain . displacing whatever was at ther 

if mid crossed over a 0 - it is behind lo now. if mid crossed over a 2 - its over in . the only things between lo and mid are 1s 

> start with the concept of 2 arrays

```
0 0 1 - - - - -
  ^           ^

0 1 0 2 2 0 1 1
    ^
``` 
fill in the new array with 0s and 2s in one pass. everything else is a 1.
then remember it's a game of swaps. smthn needs to be swapped for the 0, 2 to be where they need to be. 

## cpp optimizations
