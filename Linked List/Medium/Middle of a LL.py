"""
**************
Brute Approach
************************************************************
1. Initialize a counter variable cnt to zero, to get the length of LL.
2. Now traverse through the LL, till you find None and keep increasing the counter.
3. Now you get the length of the LL, get the middle node in case of odd length, else
    middle + 1 in case of even length
4. Again iterate through the LL, and return the respective middle Node.

TC : O(n + n/2)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def middleNode(self, n, head, key):
    # Code here

    cnt = 0
    currentNode = head

    # Traverse until you find None and keep increasing count
    while None != currentNode:
        cnt += 1
        currentNode = currentNode.next

    # Get middle Node index both in case of even/odd length
    res = (cnt // 2 + 1) if cnt % 2 == 0 else (ceil(cnt / 2))

    cnt = 0
    currentNode = head

    # Iterate again to fetch the respective middle Node
    while None != currentNode:
        cnt += 1
        if cnt == res:
            return currentNode

        currentNode = currentNode.next


"""
**************
Optimal Approach ( Slow and Fast pointers )
************************************************************
1. This approach uses two pointers, slow and fast. slow would be moving one step, while fast
    moves two steps.
2. Initially both would be at head node.
3. Traverse through the LL until you crosses or reaches at the end of the LL. Meaning the fast
    pointer will either stop at last node or after the last node (None).
4. Return the slow pointer, because if fast is covering the distance by d using two steps, 
    then slow be at d/2.

TC : O(n)
SC : O(1)
"""


def middleNode(self, n, head, key):
    # Code here
    slow = head
    fast = head

    # Traverse until you are at last node or after last node (None)
    while None != fast and None != fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow