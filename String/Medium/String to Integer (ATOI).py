"""
**************
Approach
************************************************************
1. Initialize three variables i to zero, empty string res, sign equals one.
2. First Check : Do not consider leading spaces.
3. Second Check : Handle Sign, if you encounter '-' sign, update it else not.
4. Third Check : If it is a digit add it to resultant string.
5. If the string contains characters ignore it, we need to do a check for it. If you do not
    check, resultant string would be ' ' or some numbers.
6. If Empty return 0.
7. Convert the result into integer and multiply it with the sign. ( If we encounter a '-' sign
    in our string )
8. Initialize two variables INT_MIN --> -2**31 and INT_MAX --> 2**31 - 1.
9. Compare the result, if it is lesser than INT_MIN, return INT_MIN
    - If it is greater than INT_MAX, return INT_MAX
    - Else return result

TC : O(n)
SC : O(1)
"""


def stringToIntegerATOI(s):

    n = len(s)
    i = 0
    res = ''
    sign = 1

    # Leading Spaces
    while i < n and s[i] == ' ':
        i += 1

    # Handle Optional Sign
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    # Build the Number
    while i < n and s[i].isdigit():
        res += s[i]
        i += 1

    if not res:
        return 0

    result = sign * int(res)

    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    else:
        return result

#Input
s = "1337c0d3"
print(stringToIntegerATOI(s))

