'''lan has been given an array A of length N and he wants to find the sum of even positions after reversing the array your task is to help him find and return an integer value representing sum of the array elements at he even positions of the reversed array.

Input Specification:
input1:A reversed integer array A
input2:An integer N, representing length of the array

Output Specification:Return an integer value representing sum of the array elements present at the even positions of the array

Example:
input1:[10,20,30,40,50,60]
input2:6
Output:120'''
arr = [10, 20, 30, 40, 50, 60]

def sum_(arr):
    
    arr = arr[::-1]     # Reverse the array
    
    # Sum elements at even positions in the reversed array
    return sum(arr[i] for i in range(0, len(arr), 2))

print(sum_(arr))  
