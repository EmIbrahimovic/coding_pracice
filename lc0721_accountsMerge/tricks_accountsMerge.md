---
strongly-connected:
- "[[adhoc]]"
- "[[hash map simple]]"
- "[[sorting]]"
tags:
- problem
favorite: False
---

# LeetCode 721. accountsMerge

koncept:
- drzi mapu emailova s listom str.
	- "john at mail dot com": [0, 4, 6, 7] -> ovi svi trebaju biti mergeani
	- "john at mail dot com": [1, 2, 5, 7] -> ovi svi trebaju biti mergeani

to znaci da imas parove mail1 -> meganode1
n^2 algoritmom mozes medjusobno povezati meganodeove

isti problem, samo dual. moras mergeat liste brojeva ako dvije liste sadrze isti broj
moze li se nesto pomocu ufds-a.

mailovi imaju parent - ime
kad mail ima 

![[accountsMerge.excalidraw]]

```
0. have: index (name) to email
1. email to index
2. BFS from any name (index) - when you "visit" an email, you assign it the new index (name). when you visit a name, you just act as if it's a connection point. you can also assign it an index
3. go through all emails and create a new index -> email hash map.
4. convert the hash map to list
```

## approach lessons



## cpp optimizations
