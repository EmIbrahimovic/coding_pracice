---
strongly-connected:
- "[[permutations]]"
tags:
- problem
favorite: False
---

# LeetCode 46. permute

backtracking solution.
how to generate a permutation of a list: generate a permutation of 0-(n - 1) and order the elements acc to that
OR generate a permutation of the list with the same process we used to make the 0 to n - 1 permutation.

let's say:
1. cycle the first element through all n entries
2. cycle the second element through the remaining n - 1 entries (i have to know which prev entries were chosen)
- in order not to have this cycle through all n elements of the array, we might want to find an intelligent way to skip already chosen elements
- the thing that i'm ruling out is a simple mask
- other possibility: remove the offending element from a list.
    - if my curr element is passing through list [1, 2, ..., x, x + 1, ..., n], then i start from the back
    - i tell the next element to go up to all elements until element x .e.g plus a suffix which i create as i loop through the list
    - problem: have to create the suffix list over and over again

recursive:
- all permutations with list [1, 2, ..., n] are all permutations with list [1, 2, ..., n - 1] but with element n inserted at all places:
    - this suggests a linked list approach perhaps, where an insertion will not take an impossibly long amt of time
    - generate a list of linked lists and as a preprocessing step convert them into actual lists n * n!
- all permutations with list [1, 2, ..., n] are all permutations with list [1, 2, ..., n - 1] with n appended. then for each one of those,
swap the i'th element with the last element. each thing we get is unique: a length n list with the number n in a different place. eventually
you'd generate: n-1 factorial lists with 1 in the last place, n-1 factorial lists with 2 in the last place, ..., n - 1 fact lists with n in the 
last place. and these are all permutations

ohhh... except for the fact that i can't just append to the old lists. i have to copy them...
in that case i might just go for the simple approach

[1, 2, 3]

[1, 2, 3] -> [3, 2, 1] -> [1, 3, 2]
[2, 1, 3] -> [3, 1, 2] -> [2, 3, 1]
across all the generated lists that have n in the first spot: it's basically the n - 1 fact permutations of [1, .. n -1 ] but with the first element brought to the back. this still gets us n - 1 unique permutations

runtime: generate prev permutations T(n - 1) and for each one of them (n - 1)!, go through the whole thing (n - 1), append and swap (1 + 1)
T(n) = T(n - 1) + (n - 1)! * (n + 1) = little O(sum of factorials)

which is the best i can do kinda. i have to return n! * n integers so T(n) will take at least that much.


## approach lessons

* when calculating runtime always think of what data you have to pass to your function, what data you get out of a recursive call
and whether or not you have to copy it.
* regardless, the asymptotics are interesting O (sum factorials) = theta(n!) bc factorials grow fast i suppose.
* regardless, the asymptotics are interesting O (sum i * factoril) = theta(n * n!) bc factorials grow fast i suppose.

learned about [[heap's permutation algorithm]]

## cpp optimizations


