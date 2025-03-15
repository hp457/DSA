"""
**************
Approach
************************************************************
1. Initialize two dictionaries Source -> Target and Target -> Source for Mapping.
2. Initialize a variable res for comparing the result with target string
3. Check if source and target length are not equals, return False
4. Iterate a loop in the given string, and check if current character is present in Source and
    target dictionary or not, if not then add the respective string character to dictionary.
    
    For e.g.     s = 'egg' , t = 'add'    
    s_t_dict will hold first character {'e':'a'} mapped to target first character.
    t_s_dict will hold first character of target {'a':'e'} mapped to source first character.

5. Also check if, the target is already mapped or not, if it is then return False else continue.
6. Now iterate a loop in the source string and get corresponding mapped character from 
    dictionary and add it result variable.
7. It result equals target then return True else False.

TC : O(n)
SC : O(s + t)
"""

def isomorphicString(s, t):

    s_t_dict = dict()
    t_s_dict = dict()
    soruceLength = len(s)
    targetLength = len(t)
    res = ''

    if soruceLength != targetLength:
        return False

    for i in range(soruceLength):
        if s[i] not in s_t_dict:
            if t[i] in t_s_dict:
                return False
            s_t_dict[s[i]] = t[i]
            t_s_dict[t[i]] = s[i]

    for char in s:
        res += s_t_dict[char]

    if res == t:
        return True
    else:
        return False

s = "paper"
t = "title"
print(isomorphicString(s, t))

