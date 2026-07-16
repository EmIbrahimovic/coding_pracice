
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{__class__.__name__}({self.val}, {self.left}, {self.right})"
    

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(ll: ListNode):
    print("Printing the linked list: ")
    while ll is not None:
        print(ll.val)
        ll = ll.next
