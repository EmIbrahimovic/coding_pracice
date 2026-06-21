from typing import List
from collections import defaultdict

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)
        
        state = defaultdict(int) # unvisited, started, finished; if i go back to a node that's started - that's a back edge.
        def hasCycle(u):
            state[u] = 1

            for n in adjList[u]:
                if state[n] == 1:
                    return True
                
                if state[n] == 0 and hasCycle(n):
                    return True

            state[u] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0 and hasCycle(i):
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (2, [[0, 1], [1, 0]], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.canFinish(*test)
        print(answer)

