"""
**************
Brute Approach
************************************************************
1. Sort both the source and target string.
2. Compare if both are, if same return True else return False.

TC : O(N * logN)
SC : O(1)
"""

def validAnagram(s, t):

    ts = ''.join(sorted(s))
    tt = ''.join(sorted(t))

    if ts == tt:
        return True
    else:
        return False


"""
**************
Optimal Approach
************************************************************
1. Initialize an array of size 26 (Alphabets)
2. Iterate through the source string and increase the respective character index count.
3. Iterate through the target string and decrease the respective character index count.
4. Now check if the resultant array has any value greater than 0, if so return False.
5. Else return True.

TC : O(n)
SC : O(26) ~ O(1)
"""


def validAnagram(s, t):

    charCount = [0] * 26

    for char in s:
        charCount[ord(char) - ord('a')] += 1

    for char in t:
        charCount[ord(char) - ord('a')] -= 1

    # Check if all values of array are zero or not
    return all(x==0 for x in charCount)


# Input
s = "anagram"
t = "nagaram"
print(validAnagram(s, t))

