"""
**************
Approach
************************************************************
1. Keep a cnt variable to count the length of LL.
2. Traverse until you reach none, means out of LL.
3. Return the length.

TC : O(n)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def lenOfLL(head, x):

    cnt = 0

    # If no node in the LL, then head would be the new node
    if None == head:
        return 0

    # Iterate using the currentNode in the entire LL
    currentNode = head

    # Stop when you find the none, means no node
    while None != currentNode:
        cnt += 1
        currentNode = currentNode.next

    return cnt

