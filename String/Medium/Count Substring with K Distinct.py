"""
**************
Brute Approach
************************************************************
1. Initialize two variables longestSubstring to s[0], considering string of single char and
    longestLength equals one.
2. Using two loops generate all the possible substrings.
3. During each value in outer loop, initialize res variable to store all the substrings.
4. Now check if res is reversible of res and length of res is greater than longestLength then
    - Update longestLength and longestSubstring.

    Alternatively you can use a recursive function at Step 4 to check the palindrome.

5. At the end return, longestSubstring.

TC : O(n^3)
SC : O(n) -- Storing String
"""

def countSubstring(s, k):

    n = len(s)
    mapp = dict()
    l, r = 0, 0
    cnt = 0

    pass



#Input
s = "abaaca"
k = 1
print(countSubstring(s,k))

