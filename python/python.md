![[python collections]]

## bisect
[https://docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html)

```python
import bisect
```
#### bisect_left
> Locate the insertion point for _x_ in _a_ to maintain sorted order. The parameters _lo_ and _hi_ may be used to specify a subset of the list which should be considered; by default the entire list is used. If _x_ is already present in _a_, **the insertion point will be before (to the left of) any existing entries**. The return value is suitable for use as the first parameter to `list.insert()` assuming that _a_ is already sorted.

since 3.10 - added key function to compare each elem of array

#### bisect_right
> insertion point which comes after (to the right of) any existing entries of _x_ in _a_.