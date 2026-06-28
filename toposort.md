---
aliases:
strongly-connected:
  - "[[dfs edge classification]]"
  - "[[kahn's algorithm]]"
  - "[[cycle detection]]"
  - "[[dfs]]"
  - "[[bfs]]"
  - "[[standard graph algorithm]]"
---
# toposort

## undirected graph

just check if you have more edges than nodes if you can. 

## directed graph

you can have a cycle in the undirected version of the graph that's not a cycle in the directed version.
```
a --> b --> c 
L-----------^
```

### [[dfs edge classification]]
then, you can't just dfs with a visited/unvisited signal. if you visit c first in this example and then b, you'll get WA

you track node state: 0 unvisited, 1 started/on-path, 2 finished. if your neighbor is an edge that's on-path, then you have a problem.

### bfs - [[kahn's algorithm]]
[[greedy]]

you generate a toposort on the fly bfs-style. you put a node on the toposort if the node has indegree 0 - that's right. and once you put the node on the toposort, you decrement the indegree of every one of its neighbors. the indegree is actually "number of prereqs i still need to complete"

you do this while you have nodes of indegree 0 that aren't on the toposort (some sort of queue). all the while you count the num of classes you've taken, and if you've taken them all at the end - well you've got a valid toposort. 

if at some moment you have all nodes of indegree > 0, well you cant _start_ anywhere. i'd call this greedy.