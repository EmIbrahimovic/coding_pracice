import typing

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [2147483647]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]       

if __name__ == "__main__":
    sol = MinStack()

    tests = [
        lambda: sol.push(-2),
        lambda: sol.push(0),
        lambda: sol.push(-3),
        lambda: sol.getMin(),
        lambda: sol.pop(),
        lambda: sol.top(),
        lambda: sol.getMin()
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        print(test())

