---
strongly-connected: [[hash map standard]], [[sliding window]], [[substrings]]
---

# LeetCode 3. Longest Substring Without Repeating Characters

we're observing a non-repeating substring at each step
i move the end of the substring index by index and move the start so that the start is always one character after the last repeat of one of the characters in the substring
i know this because i keep track of the last occurence of each character

* first attempt, used a map to track the indices 5ms
* then i remembered yesterday and used an [[unordered_map]] 4ms
* then i realized the letters are ascii so i used a vector hash-map 3ms (still 78% speed) - allocated 260 spaces in the vector
* then i allocated 255 spaces in the vector and that got me to 0ms

## approach lessons

* i think this has something to do with the way memory works
    * [[memory]]
    * 255, 256, 257 have 0ms but 258 has 6ms. 259 has 1ms.
    * with 255, my vector is probably able to fit into a cache block. 
    * oh ok nvm i just ran with 260 again and it's 0

* submit the same code multiple times, maybe you'll get faster clock time

* ohhhh - in order to get less memory, i can literally just do two pointers. the start pointer does not need to be jumping, it can just walk until we find a character that matches the current character
* in this approach we just need to know whether or not we've _seen_ the current character in the current substring - don't need to know its index. as we walk the start pointer to a valid point, we reset the "seen" array
* the seen array can simply be a bitset because it's just bools.
> * lesson - if we can do something with a jumping start pointer - which needs to know more information, try to see whether it's possible to do a walking start pointer - which may only need to know boolean information

## cpp code optimization lessons

* [[unordered_map]] seems to be faster than [[map]]
