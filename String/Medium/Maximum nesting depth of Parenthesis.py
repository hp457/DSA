"""
**************
Approach
************************************************************
1. Initialize two variables cnt and maxCnt with zero
2. Iterate a loop in the string
3. Check if char is equals to open bracket, if it is increase cnt
         if char is equals to close bracket, then decrease cnt
4. Calculate maxCnt through the loop, and return it.

TC : O(n)
SC : O(1)
"""


def nestingDepth(s):

    cnt = 0
    maxCnt = 0

    for char in s:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1

        maxCnt = max(cnt, maxCnt)

    return maxCnt

#Input
s = "(1+(2*3)+((8)/4))+1"
print(nestingDepth(s))

