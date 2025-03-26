"""
**************
Brute Approach
************************************************************
1. Initialize three variables to cnt0, cnt1 and cnt2.
2. Traverse through the LL, and check the data at the current node, if it is zero then update
    cnt0, if one then cnt1, if two then cnt2.
3. Traverse again and update the currentNode first cnt0, then cnt1, then cnt2.
4. return head.

TC : O(2n)
SC : O(1)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def sort0s1s2s(self, head):

    cnt0, cnt1, cnt2 = 0, 0, 0

    # Traverse through the LL, and count 0's, 1's and 2's.
    currentNode = head
    while None != currentNode:
        if currentNode.data == 0:
            cnt0 += 1
        elif currentNode.data == 1:
            cnt1 += 1
        else:
            cnt2 += 1

        currentNode = currentNode.next

    # Traverse again and update currentNode values to 0's, 1's and 2's.
    currentNode = head
    while None != currentNode:
        if cnt0 != 0:
            currentNode.data = 0
            cnt0 -= 1
        elif cnt1 != 0:
            currentNode.data = 1
            cnt1 -= 1
        else:
            currentNode.data = 2
            cnt2 -= 1

        currentNode = currentNode.next

    return head


"""
**************
Optimal Approach
************************************************************
1. This approach uses creation of three new dummy nodes -> zeroHead, oneHead, twoHead
2. Also, initialize the pointer nodes which will be moving across this nodes and initially
    pointing to zeroHead-> zero, oneHead -> one, twoHead -> two
3. Traverse through the LL, and if the currentNode.data is zero then append to dummy node 
    zeroHead and move moving pointer (zero) for that dummy node. Vice-versa for other
    nodes.
4. Once all the traversal is done, assign/connect zero -> one -> two. Cover all the edge 
    cases, having zero not ones and twos, similar kind of.
5. Return newHead which is nothing but zeroHead->next.

TC : O(n)
SC : O(1)
"""

def sort0s1s2s(self, head):

    # Creation of dummy nodes
    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)

    # Moving pointer for each dummy node
    zero = zeroHead
    one = oneHead
    two = twoHead

    currentNode = head

    # Traver through LL, assign currentNode to respective dummy node according to the value.
    while None != currentNode:

        if currentNode.data == 0:
            zero.next = currentNode
            zero = zero.next
        elif currentNode.data == 1:
            one.next = currentNode
            one = one.next
        else:
            two.next = currentNode
            two = two.next

        currentNode = currentNode.next

    # Mapping zero -> one -> two and covering all the edge cases.
    zero.next = oneHead.next if None != oneHead.next else twoHead.next
    one.next = twoHead.next if None != twoHead.next else None
    two.next = None

    # new head would be zeroHead.next and return it.
    newHead = zeroHead.next
    return newHead
