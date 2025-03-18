from collections import Counter
"""
**************
Brute Approach
************************************************************
1. Initialize the count variable cnt to zero.
2. Form all the sub-array using two loops
3. Store the frequency of character in counter dictionary. ( Before each new iteration of
    new for loop initialize counter dictionary. )
4. In the cnt variable add the sum of max of counter value and min of counter value.
5. At the end return the cnt.

TC : O(n^3)
SC : O(1)
"""

def sumOfBeautyOfString(s):

    n = len(s)
    cnt = 0

    for i in range(n):
        counter = Counter()
        for j in range(i, n):

            counter[s[j]] += 1
            cnt += max(counter.values()) - min(counter.values())

    return cnt


#Input
s = "aabcb"
print(sumOfBeautyOfString(s))

