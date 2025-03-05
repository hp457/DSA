"""
**************
Brute Approach
***********************************************************
Iterate through the array and store the element in Set

TC : O(n) + O(n) (In rare case Hash collision or resizing else O(1) while insert in set)
SC : O(n)
***********************************************************
"""

def removeDuplicates(arr,n):

    unique_num = set()
    for i in range(n):
        unique_num.add(arr[i])

    # Put back into list
    idx = 0
    for num in unique_num:
        arr[idx] = num
        idx += 1

    return arr

"""
****************
Optimal Approach
********************************************************
Iterate through the array and update only the current idx when you found a number which 
is not equal to current element

Alternate you can use two pointer approach which is a kind of similar approach

TC : O(N)
SC : O(1)
********************************************************
"""

def removeDuplicates(arr,n):

    idx = 1

    for i in range(1,n):
        curr_ele = arr[i]
        if arr[idx] != curr_ele:
            arr[idx] = curr_ele
            idx += 1

    return arr

# Input
arr = [1,1,2,2,3,3,3]
n = len(arr)
print(removeDuplicates(arr,n))