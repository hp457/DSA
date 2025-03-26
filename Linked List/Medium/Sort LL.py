"""
**************
Brute Approach
************************************************************
1. Initialize a numbers array to store values of LL.
2. Traverse through LL, and store values/number in numbers array.
3. Sort the list in reverse order.
4. Again traverse through LL and append last element of array to each node while
    traversing and pop it, do it until you reaches end of LL.
5. Return head

TC : O(n logN + 2n)
SC : O(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def sortLL(self, head):

    numbers = list()
    currentNode = head

    # Traverse through LL, and store the values
    while None != currentNode:
        numbers.append(currentNode.val)
        currentNode = currentNode.next

    # Sort the array in reverse order
    numbers.sort(reverse=True)
    currentNode = head

    # Again traverse and add last character to currentNode val and pop it, and continue
    # the operation till you reach end of LL
    while None != currentNode:
        currentNode.val = numbers[-1]
        numbers.pop()
        currentNode = currentNode.next

    return head



"""
**************
Optimal Approach
************************************************************
1. 

TC : 
SC : 
"""

def sortLL(self, head):

    pass
