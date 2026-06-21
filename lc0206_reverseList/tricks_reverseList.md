---
strongly-connected:
- "[[linked lists]]"
tags:
- problem
favorite: False
---

# LeetCode 206. reverseList

inductive. build reverse list by keeping pointer to the last element currently in it.

in-place version is actually cute.
keep head, tail, temp.
* head = head of remaining original list
* teil = head of the reversed list so far
* temp = head of the remaining list while relinking

going through original list, take the current element, chop it off the list, (let temp be the rest of the list)
(and head is just that element). relink head's next to tail. set tail to that head. 
and finally move head to the temp.

## approach lessons



## cpp optimizations


