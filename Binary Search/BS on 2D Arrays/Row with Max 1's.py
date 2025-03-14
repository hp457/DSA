"""
**************
Brute Approach
**********************************************
1. Initialize two variables idx and maxOnes with -1 and 0.
2. Iterate outer loop over the array
3. Iterate inner loop over inner array for each element.
4. For each sub array, count the number of ones within that sub array and check if cnt is greater
    than maxOnes then increase maxOnes and current index to idx
4.Return idx

TC : O(m * n)
SC : O(1)
**********************************************
"""

def rowWithMaxOnes(arr):

    idx = -1
    maxOnes = 0

    #Iterate over the array
    for i, rows in enumerate(arr):
        cnt = 0
        # Iterate for each sub array and count ones
        for ones in rows:
            if ones == 1:
                cnt += 1

        # Update maxOnes and index
        if cnt > maxOnes:
            maxOnes = cnt
            idx = i

    return idx

"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. First iterate over each sub-array in the array and pass that sub array to a user defined
    function to calculate the first ones index
3. Function takes argument as arr, low, high
4. Use the same binary search approach
5. Calculate mid and check if it equals zero, if it is then our first one is on the right
    else on the left( high = mid ) and capture that one index -n firstIdx variable.
    And return this.
6. This functions return the first index of one and now to calculate the number of ones
    in the sub_array, just use this index and subtract it from column length,
    you will number of ones.
     Also check if the func does not return minus one, means we didn't get ones in entire
    sub_array.
     ( Try it on paper on you better understand ) 
7. If C-index is greater than maxOnes, then update maxOnes and index to i (sub_array index)
8. Once all sub array processed, return index

TC : O(m * logN)
SC : O(1)
**********************************************
"""

def rowWithMaxOnes(arr):
    R = len(arr)
    C = len(arr[0])
    idx = -1
    maxOnes = 0

    # Calculate the first index of one and return it.
    def first(arr, low, high):

        firstIdx = -1
        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == 1:
                firstIdx = mid
                high = mid - 1
            else:
                low = mid + 1

        return firstIdx

    #Iterate over each sub array and pass it to first function to calculate first index of 1.
    for i in range(R):

        index = first(arr[i], 0, C - 1)
        # We got index where value is 1
        if index != -1:
            numOnes = C - index
            # If numOnes in that sub array greater than maxOnes, update it.
            if numOnes > maxOnes:
                maxOnes = numOnes
                idx = i

    return idx


# Input
arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(rowWithMaxOnes(arr))