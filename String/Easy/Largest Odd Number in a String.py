"""
**************
Approach
************************************************************
1. Iterate in the string number in the reverse order
2. The moment at that index you find odd number, return the number from the starting index
    to the current index else return space

TC : O(n)
SC : O(1)
"""

def largestOddNumber(num):

    n = len(num)

    for i in range(n - 1, -1, -1):

        if int(num[i]) % 2 != 0:
            return num[:i + 1]

    return ''

s = '52'
print(largestOddNumber(s))

