---
strongly-connected:
- "[[lru cache]]"
- "[[priority queue]]"
- "[[OrderedDict]]"
- "[[linked list]]"
tags: 
- problem
- to-study
---

# LeetCode 146 . lruCache

the way i did is:
* dict with key -> (value, time of last use)
* then a lru priority queue - min heap - with (time of last use, key)
* when i did get, i updated the time of last use and appended to the pq
* when i did put, i evicted (removing stale values from pq by comparing to dict), erased from dict and finally put new value

## approach lessons

python:
* [[OrderedDict]] is a thing you should learn how to use!!
    * the solution is 10 lines of code shorter! and simpler conceptually
* C++ apparently there's a way to solve this with a linked list

__study this problem__

## cpp optimizations


