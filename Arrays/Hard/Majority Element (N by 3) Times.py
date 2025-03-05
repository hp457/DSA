"""
There are chances that the array would have at max 2 unique elements in the array which are 
more than n/3 times. Below array has 8 elements.
Elements should present more than 8/3 which is 2 times and we have two elements.

e.g. --> [1,1,1,3,3,2,2,2] --> 1 appears (3 times) and 2 so.

**************
Brute Approach
*******************************************************************
1. Pick the first element
2. Iterate through entire array and count it's occurrence
3. After one iteration if cnt > n/3 times, add it to resultant array, if duplicate element
    no need to add.
4. Repeat Step 1 and Step 2 
5. Return the resultant array

TC : O(n^2)
SC : O(1)
***********************************************************
"""

def majorityElement(arr,n):

    res = list()
    elePresent = n // 3

    for i in range(n):
        cnt = 0
        for j in range(i,n):

            if arr[i] == arr[j]:
                cnt += 1

        if cnt > elePresent:
            if arr[i] not in res:
                res.append(arr[i])

    return res


"""
****************
Better Approach
************************************************************************************
1. Iterate through the entire array and count the frequency of numbers in the dict
2. Iterate through dict and check the element freq occuring more than n/3 times
3. Add that element to res array and return it.

TC : O(n) + O(n) --> O(2n)
SC : O(n)
********************************************************
"""

def majorityElement(arr,n):

    count_occur = dict()
    res = list()

    for num in arr:
        if num not in count_occur:
            count_occur[num] = 1
        else:
            count_occur[num] += 1

    for key,value in count_occur.items():
        if value > (n//3):
            res.append(key)

    if len(res) == 0:
        return -1
    else:
        return res

"""
******************
Optimal Approach - 
************************************************************************************

                            Moore's Voting Algorithm

The algorithm works by maintaining a candidate for the majority element and a count to 
track the number of times this candidate appears relative to other elements. 
It is based on the observation that if the majority element exists, 
it will "survive" a sequence of eliminations during the process.

*************************************************************************************
1. Similar intuition as what we did for n/2 element problem.
2. Firstly take two variables cnt1, ele1 and cnt2, ele2 initialize with zero
3. Iterate through the array and apply the algorithm
4. If cnt1 = 0 and ele2 != curr_ele then pick that element and iterate through array, 
    if next iterative element is same as the picked element then increase else decrease cnt.
5. If cnt2 = 0 and ele1 != curr_ele then pick that element and iterate through array, 
    if next iterative element is same as the picked element then increase else decrease cnt.
6. Once you got the majority element el1 and ele2, 
    iterate that elements again through the array to verify.

TC : O(n) + O(n) --> O(2n)
SC : O(1)
********************************************************
"""


def majorityElement(arr, n):

    cnt1, cnt2 = 0, 0
    ele1, ele2 = 0, 0

    for num in arr:
        if cnt1 == 0 and num != ele2:
            cnt1 = 1
            ele1 = num
        elif cnt2 == 0 and num != ele1:
            cnt2 = 1
            ele2 = num
        elif ele1 == num:
            cnt1 += 1
        elif ele2 == num:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = list()
    cnt1, cnt2 = 0, 0
    for num in arr:
        if num == ele1:
            cnt1 += 1
        if num == ele2:
            cnt2 += 1

    if cnt1 > (n//3):
        res.append(ele1)
    if cnt2 > (n//3):
        res.append(ele2)

    return res


# Input
arr = [1,1,1,2,2,3,3,3]
n = len(arr)
print(majorityElement(arr, n))
