---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# LeetCode 84. largestRectangleArea

find the minimum and his index. largest rectangle he's involved in is r - l + 1 x his height.
then split array into l, p - 1, and p + 1, r. recurse on both. 

question: how do you find range min efficiently. answer - segment tree. 
question: how do you make sure your splits are even every time. well. you kind of don't. since the range min is log(n) regardless of segment length. and combine takes O(1), as well as the split itself.

but - segment tree is complicated.

what about just splitting array in half. 

what about - for each number i obtain the position of the first number smaller than it on the left and on the right. 
```
idx 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
arr 2 4 6 3 3 4 6 3 6 6 3 4 6 4 5 3
lft 0 0 
rgh 5 3
```
between these two indices, my height is the smallest one. 
a   B    c
a < B and we have anything between a and B is >= B. yeah that's true.
so i can calc for each index what's the largest rect it's involved in. and just take the max of those.

so how would i calc: the first number on the right that's smaller than me.
well. look at the guy on my right. if he's smaller than me - that's him.
if he's larger than me. look at his "first guy smaller than me". if that guy is smaller than me, we win. if that guy is larger, we lose.
ok. and this can be somehow optimized with stacks..
if a large guy comes, plop him on top of the stack. if a small guy comes, pop from the top of the stack until i have a smaller guy as top. then plop my small guy onto stack.

tada. o(n)

ok. that seems fine then

## approach lessons



## cpp optimizations
