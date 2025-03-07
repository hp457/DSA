"""
**************
Brute Approach
***************
1. Using three loops
2. Run first loop (i) from (0,n-2) times
2. Second loop j from (i+1) till (n-1) times
3. Third loop k from (j+1) to (n)
4. Check if arr[i],arr[j],arr[k] gives you zero, If it gives store it into the temp array
5. Sort the array, convert into tuple and insert into set data structure
6. At the end return the list of set.

TC : O(n^3 * log(no of unique triplets))
SC : O(2 * number of triplets)
"""

def threeSum(nums, n):

    res = set()

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    res.add(tuple(temp))

    return list(res)


"""
****************
Better Approach
****************
1. Declare a set data structure to store unique or numbers between i and j
2. Run a outer loop i from 0 -> n - 1
3. Set would be cleared after each new iteration of outer loop
4. Run a inner from i + 1 to n - 1
5. Calculate value of nums[k] from (nums[i]+ nums[j] + nums[k] == 0)
    which is nothing but nums[k] = -(nums[i]+ nums[j])
6. Now check the nums[k] value in set, if it is present we got the third value
7. Now sort this three values and store into the final array which is to be returned
8. Return the array

TC : O(n^2 * log(m))
SC : O(n) + (no of unique triplets)
"""


def threeSum(nums, n):

    unique_triplets = set()
    unique_num = set()

    for i in range(n):
        unique_num.clear()
        for j in range(i+1,n):
            val = -(nums[i] + nums[j])

            if val in unique_num:
                temp = [nums[i],nums[j],val]
                temp.sort()
                unique_triplets.add(tuple(temp))

            unique_num.add(nums[j])

    return list(unique_triplets)



"""
******************
Optimal Approach
******************
1. I will use three variables i,j and k
2. Sort the entire array so that we don't have to sort later on.
3. i will be initially pointing to (0) and it will be fixed
    and (j -> i + 1) and (k -> n - 1) will be moving
4. Check the sum of nums[i] + nums[j] + nums[k] until (j) crosses (k)
    - Greater than zero : reduce k
    - Less than zero : increase j
    - Equals zero : append that indices array to resultant array and
                    increase j and k. And compare the current and previous elements of j and k
                    if they are equal keep on increasing/decreasing till we found other number.
5. Once j crossed k, inner loop exit.
6. Now i will be pointing to new element which is not same as previous.
7. Repeat Steps 3-6
8. Return resultant array
                

TC : O(n log n) + O(~n^2)
SC : O(no of unique triplets) for returning
"""


def threeSum(nums, n):

    nums.sort()
    res = list()

    for i in range(n):

        # If i is pointing to the same element as it was pointing earlier
        # so we would increase i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        # Run while loop till j crosses k
        while j < k:

            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                res.append(temp)
                j += 1
                k -= 1

                # This loop is used to avoid picking the same element in next iteration
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                # This loop is used to avoid picking the same element in next iteration
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return res


# Input to Code
nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2]
n = len(nums)
print(threeSum(nums, n))
