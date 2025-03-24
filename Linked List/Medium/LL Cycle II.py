"""
**************
Brute Approach
************************************************************
1. Initialize a dictionary to hold the visited nodes
2. Traverse through the LL until it reaches end, and check if the node is in dictionary or
    not, if not then insert the node else return currentNode because it was already there, and
    it is revisited again.
3. Once traversal is done, return None. In case if LL is not in a loop.

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
            return currentNode

        currentNode = currentNode.next

    return None



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. Traverse in LL until the fast pointer reaches last Node or out of LL.
3. If any moment slow and fast pointer meet at same location, means we have a loop.
4. Now to find which node initiates the loop, will do below steps
5. Now initialize the slow back to the head, and move slow and fast by one step, until they
    collide again, if they collide means, we got the initial node of the loop.
6. Return slow/fast.
7. At the end return None, if no loop.

TC : O(n)
SC : O(1)
"""

def loopDetect(self, head):

    slow = head
    fast = head

    while None != fast and None != fast.next:

        slow = head.next
        fast = head.next.next

        # We have detected a loop
        if slow == fast:
            # slow will be pointing to head now
            slow = head
            # If the moment they collide again means we got the initial node
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None
