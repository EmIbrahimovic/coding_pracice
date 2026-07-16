---
strongly-connected:
- "[[trie]]"
tags:
- problem
favorite: False
---

# LeetCode 208. trie

first approach: no compression - just every letter is an edge in the trie.

start from empty node. each node contains a value: a cnt or a true/false for example. if it doesn't contain a value - it's just a transient node - if it does, there is a real word that ends here.

hence:
```
Trie:
- value
- children(letter -> trie node)
```

helper function: walk the tree and return the node at which we land - creating nodes along the way if necessary? (or not...)

insert - walk down, creating nodes if needed. search - walk down say yes/no. startswith - walk down say yes/no in a slightly different way.

## approach lessons



## cpp optimizations
