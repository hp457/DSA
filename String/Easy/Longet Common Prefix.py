"""
**************
Approach
************************************************************
1. To find the longest common prefix, first we need to find the minimum length word because
    that number of characters/word can have maximum common prefix characters.
2. Iterate a loop till min length word
3. Initialize a variable currChar to first character of a word.
4. Now in the entire array check if the first character is matching with all the words and
    take a count of it.
5. If count equals length of array, means we got the character having common prefix, add it
    to res variable.
6. If not break the loop and return empty string.

TC : O(minWordLengthOfStringArray * N)
SC : O(1)
"""

def largestCommonPrefix(strs):

    # Get the minimum length word
    minLenWord = len(min(strs, key=lambda word:len(word)))
    n = len(strs)
    res = ''

    # Iterate through the minimum length word
    for i in range(minLenWord):
        currChar = strs[0][i] # Store the character of first word.
        cnt = 0
        # Iterate through the entire list and compare first character of each word in list
        # And check with currChar, if equals update count else break.
        for j in range(n):

            if strs[j][i] == currChar:
                cnt += 1
            else:
                break

        #If cnt equals length of array means we one common prefix, and add it to result
        if cnt == n:
            res += currChar
        else:
            break

    return res


strs = ["flower","flow","flight"]
print(largestCommonPrefix(strs))

