import typing
from collections import defaultdict
from sortedcontainers import SortedList
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class TimeMap:

    def __init__(self):
        self.impossible_v = "z"*101
        self.key_maps = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_maps[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.key_maps[key].bisect_right((timestamp, self.impossible_v))
        if idx > 0:
            return self.key_maps[key][idx - 1][1]
        if idx == 0:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    sol = TimeMap()

#     #
#     ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    tests = [
        ("set", "foo", "bar", 1),
        ('get', 'foo', 1),
        ('get', 'foo', 3),
        ('set', 'foo', 'bar2', 4),
        ('get', 'foo', 4),
        ('get', 'foo', 5)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        print(test)
        answer = sol.__getattribute__(test[0])(*test[1:])
        print(answer)

