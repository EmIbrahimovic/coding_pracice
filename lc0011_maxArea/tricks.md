---
strongly-connected:
- "[[binary search]]"
- "[[two pointers]]
---

# LeetCode 11. maxArea

i overkilled with binary search

i was trying to answer: for each element what's the element farthest to the right/left that's greater than me
such that the current element will determing the height of the water

i did this by keepig a running max at all times

lol i was also thinking abt using a bst to solve it. but maybe that's a connection [[binary search tree alternative]]

## approach lessons

what i was actually supposed to do is a two pointers. pointers moving inside somehow.

## cpp optimizations

when you're lowerbounding on an array partially filled with -1s make sure that your bounds are all right (not necessarily .begin(), .end())
