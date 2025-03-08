"""
**************
Brute Approach
**********************************************


TC : O(n)
SC : O(1)
**********************************************
"""

def kokoEatingBananas(piles, h):
    pass



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

def kokoEatingBananas(n):

    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2

        # If middle element itself equals n then return
        if mid * mid == n:
            return mid

        # If it is less, means need a greater value, shift low forward
        elif mid * mid < n:
            low = mid + 1

        # Else shift high backward
        else:
            high = mid - 1

    return high

# Input
piles = [3,6,7,11]
h = 8
print(kokoEatingBananas(piles, h))