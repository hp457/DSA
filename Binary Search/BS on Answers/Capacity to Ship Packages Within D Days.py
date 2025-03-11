"""
**************
Brute Approach
**********************************************
1. The extremely naive approach is to check all possible capacities
    from max(weights[]) to sum(weights[]). The minimum number for which the required
    days <= d value, will be our answer.
    - Why capacity is maximum(weights[])? --> Because if we tend to deliver all the packages,
        and it's capacity is less than weight then we would not be able to deliver.
2. Now take the capacity and iterate through the entire array and count noOfDays.
3. At the end, for the last iteration where it kept on adding items and array got completed,
    increase noOfDays by 1
4. At the end check the condition where noOdDays <= days, return capacity

TC : O(N * (sum(weights) - max(weights) + 1))
SC : O(1)
**********************************************
"""

def shipPackages(weights, days):

    # Calculate maxCapacity and maxTotalWeight that can be transferred in one go.
    maxTotalWeight = sum(weights)
    maxCapacity = max(weights)
    n = len(weights)

    for capacity in range(maxCapacity, maxTotalWeight + 1):
        totalWeight = 0
        noOfDays = 0
        for i in range(n):
            if totalWeight + weights[i] <= capacity:
                totalWeight += weights[i]
            else:
                noOfDays += 1
                totalWeight = weights[i]

        noOfDays += 1

        if noOfDays <= days:
            return capacity


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = maxELe and high = sumOfArray of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Calculate the days required for that mid/day element using a calculateDays func, If :
    - It is within the stipulated time means we can get a smaller element on left so h = m-1
    - Else l = mid + 1
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(sumOfArray - maxEleOfArray))
SC : O(1)
**********************************************
"""

def shipPackages(weights, days):

    high = sum(weights)
    low = max(weights)

    # Function to calculate totalDays for the middle element/day .
    def calculateDays(weights, days, capacity):

        noOfDays = 0
        totalWeight = 0
        for weight in weights:
            # Check if we can carry the weight
            if totalWeight + weight <= capacity:
                totalWeight += weight

            # If weight exceeds increase the days and point current weight to totalWeight
            else:
                noOfDays += 1
                totalWeight = weight

        noOfDays += 1

        if noOfDays <= days:
            return True
        else:
            return False

    # Perform BS on the range
    while low <= high:

        mid = (low + high) // 2

        # Calculate totalDays for midElement, if it returns True means we can have small
        # capacity on the left which can carry all the weights
        if calculateDays(weights, days, mid):
            high = mid - 1

        # Else check on right side
        else:
            low = mid + 1

    return low

# Input
weights = [1,2,3,1,1]
days = 4
print(shipPackages(weights, days))