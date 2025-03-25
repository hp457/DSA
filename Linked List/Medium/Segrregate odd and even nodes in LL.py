"""
**************
Brute Approach
************************************************************
1. Initialize two list for storing Odd and Even indices numbers.
2. Initialize a idx variable starting from 1. (1- based indexing)
3. Traverse through the entire LL, and store the odd/even indices into respective arrays.
4. Traverse back again in LL, now update the values of currentNode with odd indices numbers
    first, then even numbers.
5. Return head

TC : O(2n)
SC : O(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def oddEvenSegrregation(self, head):

    oddIndicesNumbers = list()
    evenIndicesNumbers = list()
    idx = 1

    currentNode = head
    # Traverse through the LL and store odd/even indices numbers in respective arrays.
    while None != currentNode:
        if idx % 2 != 0:
            oddIndicesNumbers.append(currentNode.val)
            idx += 1
        else:
            evenIndicesNumbers.append(currentNode.val)
            idx += 1

        currentNode = currentNode.next


    currentNode = head
    oddIndex, evenIndex = 0, 0
    oddLength = len(oddIndicesNumbers)

    # Again traverse through the LL, and update the value of the node with odd first then
    # even indices numbers.
    while None != currentNode:
        if oddIndex < oddLength:
            currentNode.val = oddIndicesNumbers[oddIndex]
            oddIndex += 1

        else:
            currentNode.val = evenIndicesNumbers[evenIndex]
            evenIndex += 1

        currentNode = currentNode.next

    return head



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, two pointers odd and even, odd is pointing to firstNode i.e. head node
    even is pointing to secondNode i.e. head.next
2. Also, point the head.next to evenNode, to connect later on with odd last node
3. Now point the odd.next to odd.next.next and same to the even node until even reaches to the
    end of the last node or end of LL.
4. Now point odd.next to evenHead node.
5. return head
6. Do it on pen and paper, you'll understand. 

TC : O(n)
SC : O(1)
"""

def oddEvenSegrregation(self, head):

    if None == head or None == head.next:
        return head

    odd = head
    even = head.next
    # Keeping in memory to rejoin with odd last node
    evenHead = even

    # Keep on traversing until even reaches the last or out of LL
    while None != even and None != even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    # Point odd last node to evenHead
    odd.next = evenHead

    return head
