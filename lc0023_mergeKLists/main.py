from typing import List, Optional
import heapq

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        merged_head = ListNode()
        merged_tail = merged_head
        pq = [list for list in lists if list is not None]
        heapq.heapify(pq)

        while pq:
            new_element = heapq.heappop(pq)
            merged_tail.next = new_element
            if new_element.next is not None:
                heapq.heappush(pq, new_element.next)
            
            new_element.next = None
            merged_tail = merged_tail.next

        return merged_head.next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        someone else's solution.
        have a dummy node as the third head so that we dont have to have
        a special case when the list is empty.
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        def _mergeK(l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None

            mid = (l + r) // 2
            listL = _mergeK(l, mid)
            listR = _mergeK(mid + 1, r)

            return self.mergeTwoLists(listL, listR)

        return _mergeK(0, len(lists) - 1)

if __name__ == "__main__":
    sol = Solution2()

    tests = [
        ([ListNode(0, ListNode(5)), ListNode(3, None)], )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.mergeKLists(*test)
        print_ll(answer)

