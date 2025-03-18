"""
**************
Approach
************************************************************
1. Initialize a dictionary and a resultant string.
2. Iterate through the string and count the frequency of characters.
3. Sort the dictionary in reverse order on the basis of count
4. Iterate through the new sorted dict, and add the number of character count in res
5. Return the res string.

TC : O(N + NlogN)
SC : O(N)
"""


def sortFrequency(s):

    charFrequencyCount =  dict()
    res = ''

    for char in s:
        if char not in charFrequencyCount:
            charFrequencyCount[char] = 1
        else:
            charFrequencyCount[char] += 1

    charFrequencyCountSortedDesc = dict(sorted(charFrequencyCount.items(), key=lambda x:x[1], reverse=True))

    for char, count in charFrequencyCountSortedDesc.items():
        while count > 0:
            res += char
            count -= 1

    return res

#Input
s = "tree"
print(sortFrequency(s))

