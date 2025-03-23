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

def longestPalindromicSubstring(s):

    longestSubstring = s[0]
    longestLength = 1
    n = len(s)

    for i in range(n):
        res = ''
        for j in range(i, n):
            # Add the character to res and get the length
            res += s[j]
            lengthOfSubString = len(res)

            # If res and reversible of res is equal and length of that string is greater
            # than longest length
            if res == res[::-1] and lengthOfSubString > longestLength:
                longestSubstring = res
                longestLength = lengthOfSubString

    return longestSubstring

#Input
s = "babad"
print(longestPalindromicSubstring(s))

