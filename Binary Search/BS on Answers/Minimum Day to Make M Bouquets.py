"""
**************
Brute Approach
**********************************************
Base Check :- If flower and bouquets count exceeds n (length of array)
    return -1

1. Use two loops, a bloom_day in bloomDay array will iterate over the entire inner bloomDay array
2. Check if the current_day <= bloom_day, then increase the flower count and also check if,
    flower count equals to k, if it is so make a bouquet and set flower back to 0.
3. If this condition does not satisfy (current_day <= bloom_day) set flower to 0
4. In the inner loop check if there are (m) bouquets are made then update the min day.
5. Return min day

TC : O(n^2)
SC : O(1)
**********************************************
"""


def minDays(bloomDay, m, k):

    n = len(bloomDay)
    minDay = float('inf')

    # If flowers and bouquets exceeds n return -1
    if (m * k) > n:
        return -1

    # Iterate for each value/day in bloomDay array
    for i in range(n):
        bloom_day = bloomDay[i]
        bouquets, flower = 0, 0

        # For the bloomDay, cross-check entire array
        for j in range(n):

            # If it is bloom_day then increment the flower and also check if we can make bouquet
            if bloomDay[j] <= bloom_day:
                flower += 1
                if flower == k:
                    bouquets += 1
                    flower = 0
            # If it exceeds bloom_day set flower to zero
            else:
                flower = 0

            # If we are able to make bouquets on that bloom_day keep the min day stored.
            if bouquets == m:
                minDay = min(minDay, bloom_day)

    return minDay


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Base check if flowers and bouquets exceeds n return -1
3. Initially keep the pointer low = min(bloomDay) and high = max(bloomDay) of array
4. Calculate the mid element using (low + high) // 2
5. While loop till low <= high
6. For each mid element check if it is possible to make bouquet, and for checking that..create a
    function which will do work.
    - Function takes bloomDay array, bouquets(m), flowers(k), and bloom_day(midEle)
    - For the bloom_day check in the entire bloomDay array and count the flowers where day <= bloom_day array 
    - Check if we can make the required bouquets, if not return False else return True
7. Repeat the steps until we cross low and high
8. Return low (Do it with pen and paper, you would get it)

TC : O(n * log2(max - min) + 1)
SC : O(1)
**********************************************
"""

def minDays(bloomDay, m, k):

    def possibleBouquet(bloomDay, m, k, bloom_day):

        noOfBouquets = 0
        flower = 0

        for day in bloomDay:
            if day <= bloom_day:
                flower += 1
            else:
                noOfBouquets += flower // k
                flower = 0

        noOfBouquets += flower // k
        if noOfBouquets >= m:
            return True
        else:
            return False

    low = min(bloomDay)
    high = max(bloomDay)
    n = len(bloomDay)

    if (m * k) > n:
        return -1

    while low <= high:

        mid = (low + high) // 2

        if possibleBouquet(bloomDay, m, k, mid) == True:
            high = mid - 1

        else:
            low = mid + 1

    return low


# Input
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(minDays(bloomDay, m, k))