"""
**************
Approach ( Integer to Roman )
************************************************************
1. Initialize two list/arrays of numbers and their corresponding symbols as per the question.
2. Initialize two variables romanString for returning roman string and integer var times.
3. Iterate through the numbers list,
    - Check how many times the corresponding number can be fit in for that num
    - Store the number of times the symbol at that index
    - Take modulo of the num with the current value for further check.
4. Return Roman String

TC : O(1)
SC : O(log(num))

Sym	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
"""


def intToRoman(num):

    romanString = ''
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    times = 0

    for index, value in enumerate(val):
        times = num//value
        romanString += times * sym[index]
        num = num % val[index]

    return romanString


#Input
num = 3749
print(intToRoman(num))



"""
**************
Approach ( Roman to Integer )
************************************************************
1. Initialize two list/arrays of numbers and their corresponding symbols as per the question.
2. Initialize two variables romanNumber for returning number of roman string and i for 
    iterating the string initialized to 0.
3. Iterate through the roman string and do the following checks:
    - If the current_index and current_index + 1 in symbol list then add the corresponding
        index number from numbers array to romanNumber and increase counter by 2.
    - Else check current_index in symbol list then add the corresponding
        index number from numbers array to romanNumber and increase counter by 1.
4. Return Roman number.

TC : O(n)
SC : O(1)
"""

def romanToInt(s):

    romanNumber = 0
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    n = len(s)
    i = 0

    while i < n:

        if s[i:i+2] in sym:
            romanNumber += val[sym.index(s[i:i+2])]
            i += 2
        else:
            romanNumber += val[sym.index(s[i])]
            i += 1

    return romanNumber

#Input
s = "MCMXCIV"
print(romanToInt(s))