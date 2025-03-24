"""
**************
Brute Approach
************************************************************
1. Initialize a dictionary to hold the visited nodes
2. Traverse through the LL until it reaches end, and check if the node is in dictionary or
    not, if not then insert the node else return True because it was already there, and
    it is revisited again.
3. Once traversal is done, return False. In case if LL is not in a loop.

TC : O(n)
SC : O(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def loopDetect(self, head):

    mapp = dict()

    currentNode = head

    while None != currentNode:

        if currentNode not in mapp:
            mapp[currentNode] = 1
        else:
            return True

        currentNode = currentNode.next

    return False



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. Traverse in LL until the fast pointer reaches last Node or out of LL.
3. If any moment slow and fast pointer meet at same location, means we have a loop and
    return True
4. If there is no loop then fast will be pointing to the end of LL, then return False.

TC : O(n)
SC : O(1)
"""

def loopDetect(self, head):

    slow = head
    fast = head

    while None != fast and None != fast.next:

        slow = head.next
        fast = head.next.next

        if slow == fast:
            return True

    return False
