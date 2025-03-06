"""
**************
Brute Approach
***************
1. Declare two variables missing and repeating initialized to -1.
2. Run outer loop 1 -> n
3. Inner loop will run from 0 -> n-1
4. If cnt is equal to 2 then we got the repeating number
   else if cnt is zero then we got missing number
5. If the moment missing and repeating not equal to -1 return

TC : O(n^2)
SC : O(1)
"""

def missingAndRepeating(arr, n):

    missing = -1
    repeating = -1

    for i in range(1,n+1):
        cnt = 0
        for j in range(n):
            if arr[j] == i:
                cnt += 1

        if cnt == 0:
            missing = i
        elif cnt == 2:
            repeating = i

        if missing != -1 and repeating != -1:
            return missing, repeating


"""
****************
Better Approach
****************
1. Initialize two variables missing and repeating with -1.
2. Initialize a array of size (n+1) visited to keep track of count of number
3. Iterate through original array and increment the number index
4. Now, iterate over the visited array and check if cnt is equal to 2 then you can repeating
    number and if cnt equals zero then missing number.

TC : O(2n)
SC : O(n)
"""

def missingAndRepeating(arr, n):

    missing = -1
    repeating = -1
    visited = [0] * (n+1)

    for i in range(n):

        visited[arr[i]] += 1

    for i in range(1,n+1):
        if visited[i] == 2:
            repeating = i
        elif visited[i] == 0:
            missing = i

        if missing != -1 and repeating != -1:
            return missing, repeating


"""
************************************************************************
Optimal Approach - 01 (Maths) Consider in terms of Mathematical Equation
************************************************************************
1. Declare two variables SN, S2N. SN will hold sum of first n natural numbers and S2N will
    hold sum of square of first n natural number
2. Take another two variable S and S2 which hold the sum of number and sum of square of numbers in array
3. Simply we create a equation using S - S2 and SN - S2N which is nothing but 
    (x-y) and (x^2-y^2)
4. And the solve the equation, you'll get the result.
5. Don't think in terms of coding, it is totally on mathematics equations.

TC : O(n)
SC : O(1)
"""

def missingAndRepeating(arr, n):

    SN = (n * (n+1)) / 2 # y
    S2N = (n * (n+1) * (2*n+1)) / 6 # y^2
    S, S2 = 0, 0

    for i in range(n):
        S += arr[i] # x
        S2 += arr[i] * arr[i] # x^2

    val1 = S - SN # (x - y) is val1
    val2 = S2 - S2N # x^2 - y^2

    # x^2 - y^2
    # Above equation can be written as (x+y)(x-y) = val2
    # (x+y) which is val2 will be (val2 / (x-y))
    val2 = val2 / val1 # We got value for (x + y) which is val2

    # Add the equation (x-y) = val1 and (x+y) = val2
    # You'll get 2x = (val1 + val2)
    # x = (val1 + val2) / 2. You got x which is MISSING number.
    x = (val1 + val2) / 2

    # Since we get the value of x we can put this value in equation (x+y) = val2
    # y = val2 - x. You got the REPEATING number
    y = val2 - x

    return x, y


"""
****************************
Optimal Approach - 02 (XOR)
****************************
1. Get the XOR of all the values in the array and first n natural numbers
2. And now get the rightmost bit of the XOR, the rightmost bit would be that bit which is 
    having difference in the bits, in below case 2 idx bit.
    1 --> 001
    5 --> 101
3. And decide each number in array and first natural array are part of which bit either
    zero or one and do XOR of it.
4. And now to know which is missing and repeating between zero and one, iterate through
    the array and keep a cnt variable to keep count.
5. At the end check if cnt equals 2 then the comparing element is repeating and another is missing
    else missing and repeating
     
TC : O(n)
SC : O(1)
"""
def missingAndRepeating(arr, n):

    xorVal = 0

    # Get the xor of all array elements
    # And numbers from 1 to n
    for i in range(n):
        xorVal ^= arr[i]
        xorVal ^= (i + 1)  # 1 to n numbers

    # Get the rightmost set bit in xorVal
    setBitIndex = xorVal & ~(xorVal - 1)

    zero, one = 0, 0

    # Now divide elements into two sets (which is nothing but zero or one)
    # by comparing rightmost set bit
    for i in range(n):

        # Decide whether arr[i] is in first set
        # or second
        if arr[i] & setBitIndex:
            zero ^= arr[i]
        else:
            one ^= arr[i]

        # Decide whether (i+1) is in first set
        # or second
        if (i + 1) & setBitIndex:
            zero ^= (i + 1)
        else:
            one ^= (i + 1)

    # zero and one are the repeating and missing values.
    # to know which one is what, traverse the array
    xCnt = sum(1 for num in arr if num == zero)

    if xCnt == 0:
        missing, repeating = zero, one
    else:
        missing, repeating = one, zero

    return [repeating, missing]


# Input to Code
arr = [4,3,6,2,1,1]
n = len(arr)
print(missingAndRepeating(arr, n))
