"""
**************
Brute Approach
**********************************************
1. To check all the possible pages from max(arr) to sum(arr) + 1
2. The moment m > n, return -1 because books cannot be more than students
3. Iterate through the range max(arr) -> sum(arr) + 1, and for each pages check if we can
    distribute books among exact m students
4. Create a function checkPages which will perform this operation:
    - Initialize s = 1, totalStudentPages = 0
    - Iterate through the pages array and check if totalStudentPages and page exceeds limit or not
        If not then assign book to the same student else another student
    - Once iteration is done check if noOfStudent == m, then return True else False
5. If the func return true, then return the pages.

TC : O(sum(arr) - max(arr) + O(n)
SC : O(1)
**********************************************
"""

def bookAllocation(arr, n, m):

    if m > n:
        return -1

    maximumPages = max(arr)
    totalPages = sum(arr)

    # Function to check if the pages can fulfill all the students
    def checkPages(arr, pages, m):

        totalStudentPages = 0
        s = 1

        # Iterate through each page in pages array
        for page in arr:
            if page + totalStudentPages <= pages:
                totalStudentPages += page
            else:
                s += 1
                totalStudentPages = page

        # If the student are equal return True
        if s == m:
            return True
        else:
            return False

    for pages in range(maximumPages, totalPages + 1):

        if checkPages(arr, pages, m):
            return pages


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = max(arr) and high = sum(arr) of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Now using a function, calculate if we can the mid/pages can be fulfilled by the 
    students we have
    - The same function used in brute approach.
    - Iterate through the array using the mid/pages and count students
    - If they exceeds m return false else true
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(maxEleOfArray))
SC : O(1)
**********************************************
"""

def bookAllocation(arr, n, m):

    low = max(arr)
    high = sum(arr)

    # Function to calculate if the student can be fit in with all the books/pages.
    def checkPages(arr, pages, m):

        totalStudentPages = 0
        s = 1

        # Iterate through each page in pages array
        for page in arr:
            if page + totalStudentPages <= pages:
                totalStudentPages += page
            else:
                s += 1
                totalStudentPages = page

        if s == m:
            return True
        else:
            return False

    # Perform BS on the range
    while low <= high:

        mid = (low + high) // 2

        # Calculate if the pages/books can be distributed to all students
        if checkPages(arr, mid, m):
            high = mid - 1

        # Else on right side
        else:
            low = mid + 1

    return low

# Input
arr = [12, 34, 67, 90]
n = len(arr)
m = 2
print(bookAllocation(arr, n, m))