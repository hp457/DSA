"""
**************
Brute Approach
************************************************************
1. Convert the string into list of words.
2. Then reverse the words of the list.
3. At the end, join the words list and return it.

TC : O(n)
SC : O(n) --> string length
"""

def reverseWordInString(s):

    words = s.split()
    n = len(words)
    l, r = 0, n - 1

    while l < r:
        temp = words[l]
        words[l] = words[r]
        words[r] = temp

        l += 1
        r -= 1

    return ' '.join(words)


#Input
s = "the sky is blue"
print(reverseWordInString(s))

