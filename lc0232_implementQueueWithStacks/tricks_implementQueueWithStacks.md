---
strongly-connected:
- "[[queue]]"
- "[[stack]]"
tags:
- problem
favorite: True
---

# LeetCode 232. implementQueueWithStacks

i like this one. v cute idea. 
a queue is just a reversed stack. and when you're popping this is exactly what it needs to be.
but when you're pushing what do you do? well throw it onto a second stack, keep it for later.
once the popper stack empties - then we'll consult the second stack. in fact we just need to flip it over, dump it into the popper array.
and we're ready to go again


## approach lessons



## cpp optimizations


