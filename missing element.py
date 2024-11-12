'''You are required to implement the following function:
int MissingNumber(int arr[], int n);

The function accepts an integer array 'arr' and its length 'n' as arguments.Array 'arr' contains n integers inthe range of 1 to (n+1) where one of the integers is missing. Implement the function to find and return that missing integer.

Assumption:All elements of array are distinct
Note:Return 0 if array length is 0

input:
Array: 3 2 1 7 5 4
output:6
'''

def MissingNumber(arr, n):
    # If array length is 0, return 0
    if n == 0:
        return 0
    
    # Calculate the expected sum of numbers from 1 to n+1
    total_sum = int((n + 1) * (n + 2) / 2)
    
    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected and actual sum
    missing_number = total_sum - actual_sum
    
    return missing_number

arr = [3, 2, 1, 7, 5, 4]
print(MissingNumber(arr, len(arr)))  

