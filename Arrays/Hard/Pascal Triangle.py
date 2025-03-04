"""
################################Pascal Triangle###################################
                                  1
                                1   1
                              1   2   1
                            1   3   3   1
                          1   4   6   4   1
########################################################################################
                            Variation - 01 (Along with Code)
            Q. Given Row and Column, tell the element at that index
########################################################################################
Brute Approach
***************
You can get the element using the formula of combination formula (nCr) which is
                        nCr = n! / r! * (n-r)!

1. Get the factorial of (n) as numerator
2. Get the factorial of (r) as denominator1
3. Get the factorial of (n-r) as denominator2

TC : O(n) + O(r) + O(n-r)
SC : O(1)

==========================================================================================
Better than Brute
******************
Since we know that the at a point where (n-r)! would be cancel out from (n!) so we can run loop max
till (r!) e.g. 5C3 will be (5 * 4 * 3 * 2! / 3! * 2!) here 2!(n-r) will cancel out and remaining
would be calculated.

TC : O(r)
SC : O(1)

==========================================================================================

"""

def funcnCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = int(res / (i + 1))  # 5/1 * 4/2 * 3/3

    return res


"""
########################################################################################
                            Variation - 02 (Along with Code)
                        Q. Print any nth row of pascal triangle
########################################################################################
Approach
*********
We will be calling the above function for numRows times to get each row and column value and print
it and store it in the res array

TC : O(n*r)
SC : O(1)
"""

numRows = 5

for col in range(1,numRows+1):
    print(funcnCr(numRows-1, col-1))

"""



########################################################################################
                            Variation - 03 (Along with Code)
                             Q. Print the whole pascal triangle  
########################################################################################
Brute Approach - (Recursive Way)
********************************
1. Recursively calling till n == 1, adding it to resultant array and returning it.
2. Store the result into a temp array and using this array defining the elements of next array[idx]
within the array
3. At last return the resultant array

TC : O(numsRows ^ 2)
SC : O(numsRows ^ 2)
"""


def pascalTriangle(numRows, res):

    if numRows == 1:
        res[0].append(1)
        return res

    pascalTriangle(numRows - 1, res)

    # previous calculated sub_array
    prev_row = res[numRows - 2]

    # In the current sub_array append 1 at the start
    res[numRows - 1] = [1]
    n = len(prev_row)

    for i in range(1, n):
        res[numRows - 1].append(prev_row[i - 1] + prev_row[i])

    # Append last value to the end of sub_array
    res[numRows - 1].append(prev_row[n - 1])

    return res

"""
****************
Better Approach 
****************
1. Generate row for till numRows and append it to the resultant array

Logic go through --> 1   4   6   4   1

1 --> 4/1 --> 4*3/1*2 --> 4*3*2/1*2*3 --> 4*3*2*1/1*2*3*4
 
Do it on a notebook, you will better explain.
"""

def generateRows(row):

    ans = 1
    ansRow = list()
    ansRow.append(1)

    for col in range(1, row):
        ans = ans * (row - col)
        ans = int(ans / (col))
        ansRow.append(ans)

    return ansRow


# Code - 01
n, r = 5, 3
print(funcnCr(n-1, r-1))

# Code - 02
arr = [[] for _ in range(numRows)]
print(pascalTriangle(numRows, arr))

# Code - 03
result = list()
for i in range(1,numRows+1):
    result.append(generateRows(i))

print(result)