import typing
from collections import OrderedDict

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_head = list1
        second_head = list2

        third_head = None
        third_tail = None

        while first_head is not None and second_head is not None:
            transplant = None
            if first_head.val <= second_head.val:
                transplant = first_head
                first_head = first_head.next
            else:
                transplant = second_head
                second_head = second_head.next
            
            if third_head is None:
                third_head = transplant
                third_tail = transplant
            else:
                third_tail.next = transplant
                third_tail = third_tail.next
        
        transplant = first_head if first_head is not None else second_head
        if third_tail:
            third_tail.next = transplant
        else:
            third_head = third_tail = transplant

        return third_head

    def mergeTwoLists2(self, list1, list2):
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



def printll(ll):
    print("Printing the linked list: ")
    while ll is not None:
        print(ll.val)
        ll = ll.next

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (ListNode(1, ListNode(2, ListNode(4, None))),
         ListNode(1, ListNode(3, ListNode(4, None)))),
        (ListNode(2, None),
         ListNode(1, None)),
         (None, None),
         (None, ListNode(1, None))
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.mergeTwoLists(*test)
        printll(answer)

