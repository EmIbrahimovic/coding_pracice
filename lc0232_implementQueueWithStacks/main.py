# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *

class MyQueue:

    def __init__(self):
        self.to_pop = []
        self.to_push = []

    def push(self, x: int) -> None:
        self.to_push.append(x)

    def turn_over(self) -> None:
        while self.to_push:
            self.to_pop.append(self.to_push[-1])
            self.to_push.pop()

    def pop(self) -> int:
        if not self.to_pop:
            self.turn_over()
        
        return self.to_pop.pop()

    def peek(self) -> int:
        if not self.to_pop:
            self.turn_over()
        
        return self.to_pop[-1]

    def empty(self) -> bool:
        return not self.to_pop and not self.to_push


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# if __name__ == "__main__":
#     sol = Solution()

#     tests = [
#         # Test Cases
#     ]

#     for t, test in enumerate(tests):
#         print(f"======= Test {t} ========")
#         answer = sol.implementQueueWithStacks(*test)
#         print(answer)

