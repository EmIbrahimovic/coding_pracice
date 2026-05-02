---
strongly-connected:
- "[[linked list]]"
- "[[sorting]]"
- "[[merge sort]]"
- "[[dummy trick]]"
tags: problem
---

# LeetCode 21 . mergeTwoLists

keep two pointers, one at the head of each list.

the whichever one points to the smaller element says put. 

3, naredni -> 4, naredni -> 5, nista

4, naredni -> 6, naredni -> 7, nista

1. create new LL
just append nodes

2. transplant elements of the second list into the first one

keep pointer to head of first
pointer to middle of first
pointer to head of second (slowly getting chopped)

when second needs to be transplanted:
1. move head forward
2. take the prev head, link the next el of first to it, unlink the next el from curr el of first,link the middle of first to the node from the second
3. advance current of first


## approach lessons

doing it at 2am led to a bad decision being made: not seeing that we can use the same nodes
to build up the third list (just chopping off the first and second - no copying necessary)
**lesson:** think more. don't be overconfident. draw it out on paper. and be patient with 
yourself when you're doing things late at night

there's a nice way to handle the construction of the third list:
* the fact that it could be None at the beginning creates unnecessary if statements
* so make it a dummy head instead and chain onto it
* return dummy.next

## cpp optimizations


