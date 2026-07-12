
Additionally, while you opt to use your new diamond-placing machine to start all your paintings immediately and simultaneously, your friend opts for the old-school way of working by hand, so she can only work on one painting at a time. Luckily, you have estimates for the time it takes to complete each of these steps – denoted by , , and  for the respective three steps – for every painting.


```
1 2 3
2 3 4
```

times for frend to receive
```
3 - 3
5 - 4
```

3 -> 6 -> 10


```
2 
1 2 3
4 5 6
```

3 - 3 -> 6
9 - 6 -> 15

1) figure out the start times.
2) sort the painintings by start times, see how long it takes

1 3 4 5 
3 5 6 7

at each p, if i can't start it immediately, reset counter to its s
if i can start imm, increment counter by its ti

---

```
2 10
20
10
```

1) drink 20
2) at h = 1, she's at 10 and after she cant continue, so at h=1 drink 1 more
3) at h = 2, she's done

if she did 30 immediately: 30/16 =
30/2^x = a
2^x = 30/a
x = log2(30/a) = 1.5

```
3 1
5
2
8
```
7.16992500144231

1) drink 8
2) at h=3 she's done, drink another one


(a + b + c) / 2^h

vs

a/2^ha + b/2^hb

just drink them sequentially, order doesn't matter? never overlap???
drink the max energy first and then yea. 

---

```
3
2 1 0
```

among the right, 2 ppl are facing back -> locked in
at index 1 - either one person facing front OR one person facing back BUT not both -> uniquely determined

3
1 0 0
```
< < >
```


3
2 1 2
```
. < <
> > .
```
(high end values, xx)
the end values give us a LOT of information. outside going in constructing the numbers

3
1 1 1
```
. < >
. > <
```
comparing adjacent values, we see whether or not the current guy is looking or not.
if values are equal, then he's facing the right. if values decreased he's facing the left. if values jumped by more than 1, (lowkey wrong)
if values decreased by more than 1 - 

```
* if 1 - must be 0
* if 2 - must be idk 1 1 or 0 1 or 0 1
* if >= 3 - then we have a party.
	  0 1 are incr. > >
	  0 1 are decr. < < 
	  0 1 are equal > < or < >, the right has (n[1] - 1 or n[1]) look at third guy. 
		  if n[2] - 1 = n[1] - 1, he's turned to the left and there's n[2] - 2 ppl on that side of the array && ? ? < (x = n[1] - 1)
		  if n[2] - 1 = n[1], he's turned to the right and there's n[2] - 2 ppl on that side of the array && ? ? > (x = n[1])
		  if it's any other value, it's impossible
		  so based on his value

* then we know exactly how many people are turned to the right in the array and are unsure about how many people are looking at me - situation is still uncertain; we can keep resolving it in a similar way n[1] or n[1] - 1, compare to the next guy, determine his direction, keep uncerainty; 
* when you get to the end, 
```

```
> < <
< > >
  
      3

       5
1/2.     2/3
1) value empirically; value hypothetically - take the combo that sums to 5 i suppose.
```