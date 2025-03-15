"""
**************
Brute Approach
************************************************************
1. Initially take out the length of s and goal, return False if not same else continue.
2. Now to rotate the string, iterate a loop till strLen, that will be number of rotations.
3. Initialize a res variable for storing the string for that rotation
4. Run inner loop that will run from r -> r + strLen
5. Add the character to the temporary res string
6. Check if res equals goal, if so return True, else continue above steps.

TC : O(n^2)
SC : O(n) --> For storing result in res string
"""


def rotateString(s, goal):

    stringLen = len(s)
    goalLen = len(goal)

    if stringLen != goalLen:
        return False
    # Iterate through the length of string i.e. no of rotations
    for r in range(stringLen):
        res = ''
        # Loop runs till rotation to rotation plus length of string
        for i in range(r, r + goalLen):
            # If string length exceeds, it will go back to initial index -> 0.
            res += s[i % stringLen]

        #If result equals goal return True
        if res == goal:
            return True

    return False

"""
**************
Optimal Approach (Trick)
************************************************************
Trick : If you concatenate any string with itself, then it will have all the iteration
        of the that string.
        
        Example : s = 'abc', If I concatenate, it will become --> 'abcabc'
        Now if you see, you can get all rotation of abc i.e. 'abc', 'bca', 'cab'
        
1. Check the goal in concatenation of input string

TC : O(n) --> in Operation
SC : O(n) --> Concatenation of S
"""

def rotateString(s, goal):

    if len(s) != len(goal):
        return False

    if goal in s + s:
        return True

    return False


#Input
s = "abc"
goal = "bca"
print(rotateString(s, goal))

