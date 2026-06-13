---
strongly-connected:
- "[[bfs]]"
- "[[leaf peeling]]"
- "[[tree dp]]"
tags:
- problem
favorite: False
---

# LeetCode 310. findMinHeightTrees

this one was tricky for me to formalize ngl
i'm figuring out how to make a good data structure for a tree.
maybe a tree node instead of a whole bunch of vectors would make it easier to keep track. easier to think
about things better.

## approach lessons

one thing:
* the counter-example i'd made for "4 nodes could be the answer" was wrong

lesson:
* for every counter-example you give, check and recheck it. you have a tendency to make mistakes.
* analyze every line of your pseudocode for complexity (there are single lines that can cost you n^2)
* a leetcode medium should not have 3 lists and a dp and 2 closures. it's nice to 
figure out that solution, but don't implement it. unless you're ready to spend 2hrs on it

ponos: izgurala sam do kraja
losa stvar: trebalo mi je 2 sata

implementation comments:
> The function computes maxdist[u] but also maintains the running answer via nonlocal. It's cleaner to separate the two.
> calculating the max excluding a certain node is better done by remembering the top 2 max guyd ans checking if the current v is the max guy

## actual solution

repeatedly remove leaf nodes bfs style. idk how why or what.

## cpp optimizations


