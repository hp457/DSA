"""
**************
Brute Approach
************************************************************
1. Initialize a dictionary to hold the visited nodes and length of the LL, till current
    node.
2. Traverse through the LL until it reaches end, and check if the node is in dictionary or
    not, if not then insert the node else return the ( totalLength - the node which is initiating
    the length and the length till that node of LL)

    To understand let's take this example:
               ->4->13->6->
    1->2->3->15`          `7
                 <-9<-8<-

    Till 15th node we have LL of length four, now when we reach again till 15 the length would
    be eleven. So we return, totalLength - Initial loop start node length

3. Once traversal is done, return 0. In case if LL is not in a loop.

TC : O(n)
SC : O(n)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def lengthOfLoop(self, head):
    mapp = dict()
    length = 1

    currentNode = head

    while None != currentNode and None != currentNode.next:

        if currentNode not in mapp:
            mapp[currentNode] = length
            length += 1
        else:
            return length - mapp[currentNode]

        currentNode = currentNode.next

    return 0


"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. Traverse in LL until the fast pointer reaches last Node or out of LL.
3. If any moment slow and fast pointer meet at same location, means we have a loop.
4. If there is a loop then, write a function to getLength of that loop.
5. Function takes two argument slow and fast.
    - Initialize initial length of node/loop as one.
    - Move fast pointer one step ahead and keep increasing length.
    - Keep on moving until you reaches slow pointer again and break it.
    - return the loop length
6. Return loop length
7. In no loop, then return 0.

TC : O(n)
SC : O(1)
"""


def lengthOfLoop(self, head):
    # Function to return length of loop
    def getLength(slow, fast):

        length = 1
        fast = fast.next

        # Move fast by one-step till it reaches, slow again and keep on increasing length
        while slow != fast:
            fast = fast.next
            length += 1

        return length

    slow = head
    fast = head

    while None != fast and None != fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return getLength(slow, fast)

    return 0
