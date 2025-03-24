"""
**************
Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. Traverse in LL until the fast pointer reaches last Node or out of LL.
3. If any moment slow and fast pointer meet at same location, means we have a loop and
    return True
4. If there is no loop then fast will be pointing to the end of LL, then return False.

TC : O(n)
SC : O(1)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def loopDetect(self, head):

    slow = head
    fast = head

    while None != fast and None != fast.next:

        slow = head.next
        fast = head.next.next

        if slow == fast:
            return True

    return False
