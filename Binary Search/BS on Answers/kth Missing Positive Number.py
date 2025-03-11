"""
**************
Brute Approach
**********************************************
1. Take out the maxEle from the array
2. Run a loop till from 1 -> (n + maxEle + 1)
3. Take a counter variable if it equals k, return i

TC : O((maxOfArray + k) * n)
SC : O(1)
**********************************************
"""


def kthPositive(arr, k):

    maxEle = max(arr)
    cnt = 0

    for i in range(1, maxEle + k + 1):

        if i not in arr:
            cnt += 1
            if cnt == k:
                return i


"""
**********************************************
Optimal Approach ( A tricky and Good Problem )
**********************************************
1. In this BS problem, this will be slightly varying in terms of iteration, in normal we used
    to iterate over the array.
2. The same low -> 0 and high -> n - 1
3. And calculate the mid element.
4. Now to analyze which half to check whether left or right, what we are going to do is, we're
    going to calculate at current index value how many missing elements would be possible before that
    And this can be done using --> arr[current_idx] - (current_idx + 1)
    
    For e.g. --> [2,3,4,7,11] and k = 5
    According to formula the missing elements prio to current index would look like --> [1,1,1,3,6]
    
5. Since we get the hypothetical numbers/array where our k would be residing is between 3 and 6
6. Do BS on this.
7. Now to find the k missing element, we need to do some basic maths:
    - How you find missing at current index --> arr[high] - (high + 1)
    - How do you find more --> k - missing
    
    -----------> What we need to return --> arr[high] + more <------------
    
    So now let's calculate, let's put respective values of more and missing in above eqn,
    to cover all the cases
    
    -   arr[high] + k - (arr[high] - high - 1)
    -   arr[high] + k - arr[high] + high + 1
    -   k + high + 1 ( high + 1 can be written as low )
    -   low + k 
    
8. Return low + k.
9. Do it on paper, you would understand it.

TC : O(logN)
SC : O(1)
**********************************************
"""

def kthPositive(arr, k):

    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:

        mid = (low + high) // 2

        if (arr[mid] - (mid + 1)) < k:
            low = mid + 1

        else:
            high = mid - 1

    return low + k


# Input
arr = [1,2,3,4]
k = 2
print(kthPositive(arr, k))