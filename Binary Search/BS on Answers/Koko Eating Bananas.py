import math
"""
**************
Brute Approach
**********************************************
1. Take out the maximum value from the array, which will be max bananas, can be consumed
    over the array/piles
2. Run a loop i from 1 -> maximumPileBanana + 1 calculated from above step
3. Declare/Take two variables, r pointer for moving across the array/piles
    and a timeConsumed variable to calculate hours be taken eating that number of bananas
    piles[r]/(i) --> i is the number of bananas can be taken.
4. Once timeConsumed is calculated, check if it is <=h as per the question, if it is then
    return the value

TC : O(max(array) * n)
SC : O(1)
**********************************************
"""

def kokoEatingBananas(piles, h):

    # Maximum bananas that can be consumed
    maxBananaPile = max(piles)
    n = len(piles)

    # Iterate over each banana that can be consumed
    for i in range(1, maxBananaPile + 1):
        r = 0
        totalHoursConsumed = 0

        while r < n:
            # If koko is on a pile and if he used to eat i number of bananas at given pile
            # It would take piles[r]/i hours to finish that pile.
            totalHoursConsumed += math.ceil(piles[r] / i)
            r += 1

        # If the time taken is lesser than h then this would be by answer
        if totalHoursConsumed <= h:
            return i



"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 1 and high = maxEle of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Calculate the hours required for that mid element using a calculateHours func, If :
    - It is within the stipulated time means we can get a smaller element on left so h = m-1
    - Else l = mid + 1
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(maxEleOfArray))
SC : O(1)
**********************************************
"""

def kokoEatingBananas(piles, n):
    maxBananaPile = max(piles)
    low = 1
    high = maxBananaPile

    # Function to calculate totalHours for the middle element.
    def calculateHours(piles, mid):

        totalHoursConsumed = 0
        for num in piles:
            totalHoursConsumed += math.ceil(num / mid)

        return totalHoursConsumed

    # Perform BS on the range
    while low <= high:

        mid = (low + high) // 2

        # Calculate totalHours for midElement
        totalHours = calculateHours(piles, mid)

        # If it is within the stipulated time, let's check on left if there is any smaller
        # number.
        if totalHours <= h:
            high = mid - 1

        # Else on right side
        else:
            low = mid + 1

    return low

# Input
piles = [3,6,7,11]
h = 8
print(kokoEatingBananas(piles, h))