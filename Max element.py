'''You are given a function, void MaxInArray(int arr[], int length); The function accepts an integer array 'arr' of size 'length' as its argument. Implement the function to find the maximum element of the array and print the maximum element and its index to the standard output.
the maximum element and its index should be printed in separate lines
Note:
Array index starts with 0
Maximum element and its index should be separated by a line in the output
Assume there is only 1 maximum element in the array
'''

arr = [23, 45, 90, 27, 66, 12, 78, 13, 71, 86]

def MaxInArray(arr):
    max_element = arr[0]
    max_index = 0

    for i in range(0, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i

    print(max_element)
    print(max_index)

MaxInArray(arr)
