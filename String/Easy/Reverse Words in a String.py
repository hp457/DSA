"""
**************
Approach
************************************************************
1. Splitting the string on space to get the list of it.
2. Initialize two variables l = 0 and r = n - 1
3. Swap the list
4. Return the concatenated string of the list

TC : O(n)
SC : O(noOfWords)
"""

def reverseWords(s):

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


s = 'the sky is blue'
print(reverseWords(s))

