"""
**************
Brute Approach
************************************************************
1. Initially check if LL has one no node, i.e. head equals None, then return None
2. Initialize a temporary array to hold numbers of LL.
3. Traverse through the LL, and store that number into temporary array.
4. Now again traverse through the LL and replace the currentNode value with stack/array
    top element, repeat this step until you reach end of LL.
5. Return head


TC : o(2n)
SC : o(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverseLL(self, n, head, key):
    # Code here
    # Check if no elements in the LL
    if None == head:
        return None

    #Initialize a temporary array
    numbers = list()

    currentNode = head

    # Traverse through the LL and store the number in temporary array.
    while None != currentNode:
        numbers.append(currentNode.val)
        currentNode = currentNode.next

    currentNode = head
    # Now traverse the LL again and replace the node value with stack top value and pop the
    # Element
    while None != currentNode:
        currentNode.val = numbers[-1]
        numbers.pop()
        currentNode = currentNode.next

    return head


"""
**************
Better Approach
************************************************************
1. This approach moves the pointer to the back/previous node.
2. It uses prev, front pointers to hold the previous and next node.
3. Traverse the way you traverse through the LL, and keep on updating the pointers.
4. Give it a dry run on pen and paper with three nodes, and you are at the center node.
5. Return prev (You'll understand why prev when you do it on paper)

TC : O(n)
SC : O(1)
"""


def reverseLL(self, head):

    currentNode = head
    prev = None

    while None != currentNode:
        front = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = front

    return prev