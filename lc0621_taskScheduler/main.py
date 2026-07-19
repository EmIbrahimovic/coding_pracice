from typing import List
from collections import Counter
from heapq import *

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def taskScheduler(self, tasks: List[str], n: int) -> int:
        task_cnt = Counter(tasks)
        candidates = [(-cnt, el) for el, cnt in task_cnt.items()]
        candidates.sort()
        candidates.reverse()

        topn = []
        while candidates and len(topn) <= n:
            topn.append(candidates.pop())
        heapify(candidates)

        # Now for counting
        cycles = 0
        while topn or candidates:
            print("new round")
            print(topn)
            print(candidates)
            for i in range(len(topn)):
                cycles += 1
                topn[i] = (topn[i][0] + 1, topn[i][1])

            if topn[0][0] != 0 or candidates:
                cycles += n + 1 - len(topn)

            # pop
            for i in range(len(topn) - 1, -1, -1):
                if topn[i][0] == 0:
                    topn.pop()
            # replace
            for i in range(len(topn)):
                if candidates and topn[i][0] > candidates[0][0]:
                    topn[i] = heappushpop(candidates, topn[i])
            # refill
            while candidates and len(topn) <= n:
                topn.append(candidates[0])
                heappop(candidates)
            
        return cycles

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        
        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            time += task_count if not pq else n + 1
        return time
            
if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["A","A","A","B","B","B"], 2),
        (["A","C","A","B","D","B"], 1),
        (["A","A","A", "B","B","B"], 3),
        (["A","A","A", "A","B","C", "D", "E"], 1),
        (["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2)
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.taskScheduler(*test)
        print(answer)

