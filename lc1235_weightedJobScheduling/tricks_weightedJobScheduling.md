---
strongly-connected:
- "[[dp simple]]"
tags:
- problem
favorite: False
---

# LeetCode 1235. weightedJobScheduling



## approach lessons

approach: i did it sort by end time and binsrch to get the last we could have possibly added
possible also: sort by start time and bin srch end time arrays for next beginning

* python syntax trick:
```python
jobs = sorted(zip(endTime, startTime, profit))

@lru_cache(None) # for dp
```

## cpp optimizations


