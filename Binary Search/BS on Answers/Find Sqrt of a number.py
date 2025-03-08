"""
**************
Brute Approach
**********************************************
1. Store all the non-zero number to the temp array
2. Place back these number to original array
3. And fill zeros for the rest of the indexes

TC : O(n) + O(x) + O(n-x) --> O(2n)
SC : O(x)
**********************************************
"""

def sqrt(arr,n):

    temp = list()
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    temp_size = len(temp)
    for i in range(temp_size):
        arr[i] = temp[i]

    for i in range(temp_size,n):
        arr[i] = 0

    return arr


"""
**************
Optimal Approach
**********************************************
1. Use two pointer approach i, j
2. First loop will find the first zero element and break it using j
3. Second loop will run from (j+1) -> n and replace all zero to nonZero and vice-versa

TC : O(n)
SC : O(1)
**********************************************
"""

def zerosToTheEnd(arr,n):

    j = 0
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

# Input
arr = [100, 0, 7, 0, 90]
n = len(arr)
print(zerosToTheEnd(arr,n))