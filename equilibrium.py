"""Equilibrium
You are given an array A of N integers. An equilibrium position is a position where the sum of all integers on its left is equal to the sum of all integer in array A. Print the index of the equilibrium position
Note: For any given array there is only a single equilibrium position, if no equilibrium position is found then print "NOT FOUND" without quotes
The array is 1 indexed

Input Format:
The input consists of two lines:
The first line contains an integer denoting N
The second line contains N space separated integers denoting the elements of the array A

Output Format:Print the index of the equilibrium position,if no equilibrium position is found then print "NOT FOUND" without quotes

Example:
Input:
7
-7 2 4 9 -8 1 6
Output:4
"""
N = 7  
A = [-7, 2, 4, 9, -8, 1, 6]  

def find_equilibrium_position(N, A):
    total_sum = sum(A)
    left_sum = 0
    
    for i in range(N):
        # Right sum is the total sum minus the current element and left sum
        right_sum = total_sum - left_sum - A[i]
        
        if left_sum == right_sum:
            return i + 1  # Return the 1-indexed position
        
        left_sum += A[i]
    
    return "NOT FOUND"


print(find_equilibrium_position(N, A))

