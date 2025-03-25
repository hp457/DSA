"""
**************
Brute Approach
************************************************************
1. Initialize a variable totalNodes and count number of nodes in LL.
2. Traverse through the Ll and update node count in totalNodes variable.
3. Now initialize another variable removeNode which will be the node to be removed,
    it is calculated by totalNodes - n
4. Now we need to perform three checks here to remove node
    - If the node we're deleting is the first node, then move head to next node and
        return head.
    - If it is middle node, then traverse till last second node, and reassign the front,
        prev and currentNode accordingly to point right node and return head ( Do it on
        paper, you'll understand )
    - If it is last node, then anyway above loop exits and once it exits then, we just
        needs to assign the prev next node pointing to None, and return head

TC : O(2n)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def deleteNthNode(self, head, n):

    # Variable to count total number of nodes
    totalNodes = 0
    currentNode = head
    prev = None

    # Traverse through the LL and count number of nodes
    while None != currentNode:
        totalNodes += 1
        currentNode = currentNode.next

    # The node to be removed
    removeNode = totalNodes - n
    # Initially we're at node 1 ( 0-based indexing )
    node = 0
    currentNode = head

    # If the node is front/head node, then move the head node to next and return it.
    if removeNode == node:
        newHead = head.next
        return newHead

    # If the node is in the middle, point front, prev and currentNode accordingly.
    # Also, update visited node, prev node and next node.
    while None != currentNode.next:
        if node == removeNode:
            front = currentNode.next
            prev.next = front
            currentNode.next = None
            return head

        node += 1
        prev = currentNode
        currentNode = currentNode.next

    # If the above loop breaks, means the node is the last node, then simply reassign
    # last second node to None and return head.
    prev.next = None
    return head



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. The fast pointer will be pointing to head and will move forward n steps.
    
    - There will be a case where fast reaches None, means the node to be deleted would be
        head, so return head->next.

3. Now slow will be pointing to head, and both the pointer will move one step till
    fast -> next not reaches None.
4. Once this is done, you'll be pointing to the node before the node to be deleted.
5. Now simply bypass the node to be deleted and point it to next node.
6. Return head.

TC : O(n)
SC : O(1)
"""

def deleteNthNode(self, head, n):

    fast = head
    # Move the fast pointer n steps
    for i in range(n):
        fast = fast.next

    # If the moment fast reaches end, means the node to be deleted is head, return head->next.
    if None == fast:
        return head.next

    slow = head
    # Traverse until fast reaches None.
    while None != fast.next:
        fast = fast.next
        slow = slow.next

    # Slow will be pointing to the node to be deleted before, just bypass the deleted node.
    slow.next = slow.next.next

    return head
