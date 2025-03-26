"""
**************
Brute Approach
************************************************************
1. Initialize a variable totalNodes, to get length.
2. Traverse through the LL, and get the length of LL.
3. Now get the middleNode by dividing the length by 2, to remove the middle node.
4. Traverse back again in the LL, just before the middle node and update current next
    pointer to middleNext.
5. Return head

TC : O(n + n/2)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def deleteMiddleNode(self, head):

    if None == head or None == head.next:
        return None

    lengthOfLL = 0
    currentNode = head
    # Traverse and get the length of LL
    while None != currentNode:
        lengthOfLL += 1
        currentNode = currentNode.next

    # Finding the node to be removed
    middleNode = lengthOfLL // 2
    currentNode = head

    # Traverse again just before middle Node and point current next to middle next.
    while None != currentNode:
        if middleNode == 1:
            currentNode.next = currentNode.next.next

        middleNode -= 1
        currentNode = currentNode.next

    return head



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, the same slow and fast pointer of Tortoise and Hare
    algo, but slightly little change.
2. Initially slow and fast will be pointing to head.
3. We will skip one iteration of slow, and then will move both simultaneously slow by one step
    and fast by two step until fast reaches at last node or end of LL.
4. Now change the slow->next to slow->next->next ( Do it on paper, you'll understand )
5. Return head 

TC : O(n/2)
SC : O(1)
"""

def deleteMiddleNode(self, head):

    if None == head or None == head.next:
        return None

    slow = head
    fast = head
    # Initially move the fast pointer only.
    fast = fast.next.next

    # Move simultaneously until fast reaches end of LL or last node.
    while None != fast and None != fast.next:
        slow = slow.next
        fast = fast.next.next

    # Point/Bypass the node
    slow.next = slow.next.next
    return head
