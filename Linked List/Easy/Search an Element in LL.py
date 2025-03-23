"""
**************
Approach
************************************************************
1. Traverse until you reach end of LL, i.e. None
2. Check if the currentNode.data equals to the key we're searching for.
3. Return True else False

TC : O(n)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def searchKey(self, n, head, key):
    # Code here

    currentNode = head

    while None != currentNode:
        if currentNode.data == key:
            return True

        currentNode = currentNode.next

    return False