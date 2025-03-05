import math
"""
**************
Brute Approach
*******************************************************************
1. Iterate through each element in the entire array using two loops
2. And take a counter variable
3. The moment it becomes greater than n/2, return the element

TC : O(n^2)
SC : O(1)
***********************************************************
"""

# def majorityElement(arr,n):
#
#     for i in range(n):
#         curr_ele = arr[i]
#         cnt = 0
#         for j in range(i,n):
#             if arr[j] == curr_ele:
#                 cnt += 1
#
#         if cnt > math.floor(n/2):
#             return curr_ele
#
#     return -1


"""
****************
Better Approach
************************************************************************************
1. Iterate through the entire array and count the frequency of numbers and return it.

TC : O(n) + O(n) --> O(2n)
SC : O(n)
********************************************************
"""

# def majorityElement(arr,n):
#
#     count_occur = dict()
#
#     for num in arr:
#         if num not in count_occur:
#             count_occur[num] = 1
#         else:
#             count_occur[num] += 1
#
#     for key,value in count_occur.items():
#         if value > math.floor(n/2):
#             return key
#
#     return -1

"""
****************
Optimal Approach
************************************************************************************
                            Moore's Voting Algorithm
                            

*************************************************************************************
1. Take two variables cnt = 0 and element initially.
2. If cnt = 0 then pick that element and iterate through array, if next iterative element is same as
the picked element then increase else decrease cnt.
3. Once you got the majority element, iterate that element again through the array to verify.

TC : O(n) + O(n) --> O(2n)
SC : O(1)
********************************************************
"""

def majorityElement(arr,n):

    cnt = 0
    element = int
    for num in arr:
        if cnt == 0:
            cnt = 1
            element = num
        elif num == element:
            cnt += 1
        else:
            cnt -= 1

    counter = 0
    for num in arr:
        if num == element:
            counter += 1

        if counter > math.floor(n/2):
            return element

    return -1



# Input
arr = [2,2,3,3,1,2,5]
n = len(arr)
print(majorityElement(arr,n))
