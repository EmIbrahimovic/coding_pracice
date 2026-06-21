from typing import List, Optional

# shenanegans to import utils
from pathlib import Path
import sys
current_file = Path(__file__).resolve()
parent_directory = current_file.parent.parent
sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode] :
        tail = None
        while head:
            tail = ListNode(head.val, tail)
            head = head.next

        return tail
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode] :
        # in-place
        tail = None
        temp = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp

        return tail

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.reverseList(*test)
        print(answer)

