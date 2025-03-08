"""
**************
Brute Approach
**********************************************
1. Iterate through the array from 1 -> n or n//2
2. Check if (i * i) <= n, if it's true store the (i) in an ans variable
3. If the above condition does not satisfy, break the loop
4. Return ans

TC : O(n)
SC : O(1)
**********************************************
"""

def sqrt(n):

    ans = 1
    for i in range(1,n):
        if i * i <= n:
            ans = i
        else:
            break

    return ans


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 1 and high = n or n//2
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Check
    - mid * mid == n : return mid
    - mid * mid < n : low = mid + 1
    - else : high = mid - 1
6. Once done return high ( Do it on a paper you would understand why high will be returned )

TC : O(log n)
SC : O(1)
**********************************************
"""

def sqrt(n):

    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2

        # If middle element itself equals n then return
        if mid * mid == n:
            return mid

        # If it is less, means need a greater value, shift low
        elif mid * mid < n:
            low = mid + 1

        # Else shift high backward
        else:
            high = mid - 1

    return high

# Input
n = 11
print(sqrt(n))