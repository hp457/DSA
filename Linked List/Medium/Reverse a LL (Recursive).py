"""
**************
Approach
************************************************************
1. Do it on paper, you'll understand it.

TC : O(n)
SC : O(n)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverseLL(self, head):

    if None == head or None == head.next:
        return head

    newHead = reverseLL(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead
