---
aliases:
strongly-connected:
  - "[[cpp]]"
  - "[[data structs]]"
---
# casting .size()


* WHEN YOU SHOULD BE CAREFUL WITH CASTING vec.size() [[cpp - casting .size()]]
    - if you're subtracting a number e.g. `(int)nums.size() - k`, where k could be greater than the size of the array
    - this is gonna be unsigned subtraction, so in your loop, `for (int i = 0; i < (int)nums.size() - k; i++)`, what you 
    thought was a negative number is actually super positive right now. 

> seen in [[tricks_containsNearbyDuplicate]]