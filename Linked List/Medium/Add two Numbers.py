"""
**************
Approach
************************************************************
1. Initialize a dummyNode with -1 and a mover will be initially at dummyNode and
    a variable carry with 0.
2. Traverse until you reach at the end of you reach end of both LL, one might be shorter
    and another would be larger.
3. Get digit1 and digit2 from both the LL, if you have value else 0
4. Sum digit1, digit2 and carry. Now calculate the node value by (value % 10) and carry(//).
5. Create a new node and add it to mover->next and move mover to current Node/ newNode.
6. At the end check, if there is carry or not, if it is there create a node of it and add
    it to mover->next.
7. Return dummyNode.next

TC : O(max(l1,l2))
SC : O(max(l1,l2))
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def addTwoLL(self, l1, l2):

    dummyNode = Node(-1)
    mover = dummyNode
    carry = 0

    # Traverse until both reaches end of LL
    while l1 is not None or l2 is not None:

        # If had value then val else 0
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        value = digit1 + digit2 + carry
        digit = value % 10
        carry = value // 10

        # Create a node with the value and append to mover->next.
        newNode = Node(digit)
        mover.next = newNode
        mover = mover.next

        # Check if we have a node or not.
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    # If there is carry, then create a new node and add it to mover->next
    if carry:
        newNode = Node(carry)
        mover.next = newNode

    return dummyNode.next