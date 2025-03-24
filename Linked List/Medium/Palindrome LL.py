"""
**************
Brute Approach
************************************************************
1. Initialize a numbers array/list to store all the numbers from the LL
2. Traverse through the LL, and store the number in numbers array.
3. Again traverse in LL and check if the last/topmost element of array
    is same of currentNode val, if not return False.
    While performing this operation keep popping out the last element and update
    the currentNode to nextNode.
4. Once iteration/array is empty or traversal is done, return True.

TC : O(2n)
SC : O(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def palindromeLL(self, head):

    numbers = list()
    currentNode = head

    #Traverse LL and store number in numbers array
    while None != currentNode:
        numbers.append(currentNode.val)
        currentNode = currentNode.next

    # Again iterate through the LL and check if the last element of array is similar to current
    # If not return False else continue
    currentNode = head
    while numbers:
        if currentNode.val != numbers[-1]:
            return False

        # Remove last element and update currentNode to next
        numbers.pop()
        currentNode = currentNode.next

    return True



"""
**************
Optimal Approach
************************************************************
1. The approach we will be using is, slow and fast pointers.
2. Traverse in LL until the fast pointer reaches last Node or out of LL.
3. Once you traversed, you will get the middle node.
4. Now reverse the LL, from middleNode to the end.
5. Now compare the first half and second half values till, second not equals None.
6. If not equal return False.
7. Else once loop completes, return True

TC : O(n)
SC : O(1)
"""

def palindromeLL(self, head):

    if None == head or None == head.next:
        return True  # Empty list or a single element is a palindrome

    slow = head
    fast = head

    # Move fast to the end and slow to the middle
    while None != fast and None != fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list
    second_half = self.reverseLL(slow)

    first = head
    second = second_half

    # Compare the first half and the reversed second half
    while None != second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


def reverseLL(self, head):
    prev = None
    current = head

    while None != current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
