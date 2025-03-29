"""
**************
Brute Approach
************************************************************
1. Initialize a dictionary to store the nodes of LL1.
2. Traverse through the LL1 and store all the nodes in the dictionary/map.
3. Traverse through the LL2 and check if the currentNode is there in dictionary or not, if
    it is there, means we got the intersecting node, return currentNode.
4. Return None.

TC : O(n1 + n2)
SC : O(n)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def intersectionOfTwoLL(self, headA, headB):

    mapp = dict()
    moverNodeA = headA
    moverNodeB = headB

    # Traverse through the one LL, and store all nodes in map.
    while None != moverNodeA:
        if moverNodeA not in mapp:
            mapp[moverNodeA] = 1

        moverNodeA = moverNodeA.next

    # Traverse in the second LL, and check if the node is already there or not, if it is
    # there means we got the intersection node, return it.
    while None != moverNodeB:
        if moverNodeB in mapp:
            return moverNodeB

        moverNodeB = moverNodeB.next

    # Else return None, in case of no intersection.
    return None


"""
**************
Better Approach
************************************************************
1. The idea behind this approach is to start traversing in both LL from the same node to find the
    the intersecting node and to do use below approach.
2. Initially get the length of both the LL.
3. Now subtract the length from largestLL minus smallestLL to get the initial starting node.
4. Now create a function which takes three argument first -> L1, second -> L2, and the
    starting node which is calculated from step 3.
5. In the function, first traverse till the common node then,
    traverse through both LL, by one step and return L1, either they will meet or point to None.

TC : O(n1 + 2n2)
SC : O(1)
"""


def intersectionOfTwoLL(self, headA, headB):

    currentNodeA = headA
    n1 = 0
    currentNodeB = headB
    n2 = 0

    # Func to find collision point
    def collisionPoint(moverNodeA, moverNodeB, d):

        # Traverse till common node
        while d:
            moverNodeB = moverNodeB.next
            d -= 1

        # Now move in parallel in both LL, until you find intersection point or None and return it.
        while moverNodeA != moverNodeB:
            moverNodeA = moverNodeA.next
            moverNodeB = moverNodeB.next

        return moverNodeA

    # Traverse in first LL, and get the length
    while None != currentNodeA:
        currentNodeA = currentNodeA.next
        n1 += 1

    # Traverse in second LL, and get the length
    while None != currentNodeB:
        currentNodeB = currentNodeB.next
        n2 += 1

    # If L1 is smaller than L2, then L2 would be moving else L1.
    if n1 < n2:
        return collisionPoint(headA, headB, n2-n1)
    else:
        return collisionPoint(headB, headA, n1-n2)


"""
**************
Optimal Approach
************************************************************
1. Initially traverse through both the LL, the moment you reaches at the end of the LL,
    point that particular LL, to another LL head means
        LL1 -> headB
        LL2 -> headA
2. Traverse until LL1 and LL2, not meets.
3. Return LL1 

TC : O(m + n)
SC : O(1)
"""


def intersectionOfTwoLL(self, headA, headB):

    currentNodeA = headA
    currentNodeB = headB

    # Traverse until both the LL, meet at same point
    while currentNodeA != currentNodeB:

        currentNodeA = currentNodeA.next
        currentNodeB = currentNodeB.next

        # Intersection Node
        if currentNodeA == currentNodeB:
            return currentNodeA

        # If LL1 reaches end, point to LL2 head
        if None == currentNodeA:
            currentNodeA = headB
        # If LL2 reaches end, point to LL1 head
        if None == currentNodeB:
            currentNodeB = headA

    return currentNodeA