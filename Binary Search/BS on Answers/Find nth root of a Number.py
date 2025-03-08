"""
**************
Brute Approach
**********************************************
1. Iterate through the array from 1 -> m
2. Check if pow(n,i) == n, if it's true return then and there.
3. Else If the pow(n,i) > n, break the loop
4. If no value found return -1

TC : O(m * log2n) log2n --> for finding the pow of a given number
SC : O(1)
**********************************************
"""

# def nthRoot(m,n):
#
#     for i in range(m):
#
#         if pow(i,n) == m:
#             return i
#         elif pow(i,n) > m:
#             break
#
#     return -1


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 1 and high = n
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Check
    - pow(mid,n) == n : return mid
    - pow(mid,n) < n : low = mid + 1
    - else : high = mid - 1
6. Once done return -1 because we didn't find any number

TC : O(log2m * log2n) --> log2m for searching and log2n for using power function
SC : O(1)
**********************************************
"""

def nthRoot(m,n):

    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2

        # If middle element power equals m then return
        if pow(mid, n) == m:
            return mid

        # If it is less, means need a greater value, shift low forwards
        elif pow(mid, n) < m:
            low = mid + 1

        # Else shift high backward
        else:
            high = mid - 1

    return -1

# Input
m = 9
n = 2
print(nthRoot(m,n))