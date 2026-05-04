
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(ll: ListNode):
    print("Printing the linked list: ")
    while ll is not None:
        print(ll.val)
        ll = ll.next
