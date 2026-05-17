---
strongly-connected:
- "[[higher neighbors]]"
- "[[prefix and suffix max]]"
- "[[sorted stack]]"
tags:
- problem
favorite: True
---

# LeetCode 42. trapping rainwater

maybe have the solution. it's in the category of the cute adhoc higher neighbor problems like max area poster

this was frustrating

## approach lessons

i had some insights:
* figure out whether a particular pillar will be the edge of a bin (almost figured out):
    * if the guy has a **taller** guy to both sides of him - he's not going to be a pillar
    * if there's a guy that's taller to him to any side but not to the other side - he's going to be a pillar
    * **GOOD THING:** this part of the reasoning is correct and could have led me to the right solution; if i'd taken these independently of the
    approach i was trying to stick out (considering the first guy on his left/right, rather than just the largest guy to the left/right)
    * find this out by finding the _first guy to his right/left that's taller or equal to him_
    * **PROBLEM:** on any side, if the first (taller or equal) guy to his right is (equal) a guy that's equal height
        * i assumed that my guy will definitely be a pillar
        * however, this is not necessarily true, consider 8 . . . 5 . . 5 . . 5 . . . 8; then i assume that the middle five is a bin border, but it's just that
        * the equal height guys are blocking him. 

where i went wrong:
* failing to pull through with the reasoning on _how much water will be sitting on the current guy_
* i was too stuck on the idea of "find the first taller guy to my right or left"
* didn't hash out my edge cases and started coding immediately - after code was done, realized i need to go back to the drawing board
    * balance between "probability that this is correct and i'd be wasting time with edge cases" vs "probability that this is wrong and
    i'd be wasting time writing wrong code"

good things about my process:
* after figuring out the idea, i evaluated it to see how efficient it would be and changed my algorithm for finding first larger neighbor
    * this is also smthn that can break your approach
* listed out possible viewpoints - if i'd realized my new one doesn't work i could have gone back and taken a look at them - maybe have a tree?

lessons:
* if you have a particular approach in mind for a given problem - consider also some sister approaches - more local if the approach is global or more global if the approach is local
* figure out the edge cases before you start coding - edge cases don't resolve themselves on non-trivial problems and **may completely break your approach**
* figure out the complexity before you start coding - it can break your approach

## cpp optimizations


