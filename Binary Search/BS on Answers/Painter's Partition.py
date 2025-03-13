"""
**************
Brute Approach
**********************************************
1. For an array what could be the minimum time to paint a single board, definitely it is max of that
    array right, and what could be the maximum time, sum of array
2. So, iterate over the range --> (max, sum + 1)
3. For each time, calculate the number of painter required the paint all boards.
4. If it is lesser or equals k, return the time

TC : O(sum(arr) - max(arr) + 1) * O(n)
SC : O(1)
**********************************************
"""

def findLargestMinDistance(boards, n, k):

    maximumTime = max(boards)
    totalTime = sum(boards)

    for time in range(maximumTime, totalTime + 1):

        painter = 1
        totalBoardsPainted = 0

        for board in boards:
            if totalBoardsPainted + board <= time:
                totalBoardsPainted += board
            else:
                painter += 1
                totalBoardsPainted = board
                if painter > k:
                    break

        if painter <= k:
            return time


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = max(arr) and high = sum(arr) of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Now using a function, calculate if we can the mid/time can paint all the boards
    - The same function used in brute approach.
    - Iterate through the array using the mid/time and count the painters
    - If they exceeds k return false else true
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(sum - max + 1))
SC : O(1)
**********************************************
"""

def findLargestMinDistance(boards, n, k):

    low = max(boards)
    high = sum(boards)

    def canPaint(boards, mid):

        painter = 1
        totalBoardsPainted = 0

        for board in boards:
            if totalBoardsPainted + board <= mid:
                totalBoardsPainted += board
            else:
                painter += 1
                totalBoardsPainted = board
                if painter > k:
                    return False

        if painter <= k:
            return True

    while low <= high:

        mid = (low + high) // 2

        if canPaint(boards, mid):
            high = mid - 1
        else:
            low = mid + 1

    return low

# Input
boards = [2, 1, 5, 6, 2, 3]
n = len(boards)
k = 2
print(findLargestMinDistance(boards, n, k))