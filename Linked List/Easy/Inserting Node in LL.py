"""
**************
Approach
************************************************************
1. Create a node with the value to be inserted in the LL
2. Initially the currentNode will be pointing to head node.
3. Now iterate through the LL and stop until you find the node next to be None.
4. Now insert the new node at the last of the node.

TC : O(n)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def insertAtEnd(head, x):
    # code here
    newNode = Node(x)

    # If no node in the LL, then head would be the new node
    if None == head:
        head = newNode
        return head

    # Iterate using the currentNode in the entire LL
    currentNode = head

    # Stop when you find the end node
    while None != currentNode.next:
        currentNode = currentNode.next

    # Insert new node
    currentNode.next = newNode

    return head

