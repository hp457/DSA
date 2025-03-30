"""
**************
Brute Approach
************************************************************
1. Create a reverse function which will reverse the LL.
2. Initially reverse the LL.
3. Now iterate through the reversed LL, and update the currentNode value and carry.
4. If carry is still there then
    - Create a node for carry.
    - Reverse the LL
    - Point carryNode -> next to newHead from above reversed LL.
    - point newHead to carryNode

    If no carry, reverse the LL.
5. Return newHead

TC : O(3n)
SC : O(1)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def addOneToLL(self, head):

    # Function to reverse the LL.
    def reverseLL(head):

        currentNode = head
        prev = None

        while None != currentNode:
            front = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = front

        return prev

    # Reversed LL
    newHead = reverseLL(head)

    carry = 1
    currentNode = newHead

    # Traverse through the LL, and update currentNode value and carry
    while None != currentNode:
        val = currentNode.data + carry
        currentNode.data = val % 10
        carry = val // 10

        currentNode = currentNode.next

    # Check if carry is still there or not, if there create a Node of carry
    # Reverse the LL
    # Point carryNode next to newHead
    # point newHead to carryNode
    if carry:
        carryNode = Node(carry)
        newHead = reverseLL(newHead)
        carryNode.next = newHead
        newHead = carryNode

    # If no carry, reverse the list and return it.
    else:
        newHead = reverseLL(newHead)

    return newHead


"""
**************
Better Approach (Recursive)
************************************************************
1. Create a helper function and call it recursively until you reach end of LL.
2. Base condition would be end of LL and value to be returned is 1, 
    as the carry to be added is one initially.
3. Whatever the carry has been returned check it with the data if, nodeValue and carry is less
    10, if it is less than 10, then return carry 0 else set nodeValue to zero and return
    carry 1.
4. At the end, check if any carry is there, create a node and add it to the head of LL.
5. Return new head. 

TC : O(n)
SC : O(n)
"""


def addOneToLL(self, head):

    # Helper func which will be called recursively.
    def helper(temp):

        if None == temp:
            return 1

        carry = helper(temp.next)

        # Add carry to the node
        temp.data += carry
        # If below 10, then return carry 0
        if temp.data < 10:
            return 0
        #Else set nodeValue to zero and return carry 1
        else:
            temp.data = 0
            return 1

    carry = helper(head)

    # At the end, if carry is there, create a node and attach it to head of LL.
    if carry:
        carryNode = Node(carry)
        carryNode.next = head
        head = carryNode
        return head
    else:
        return head