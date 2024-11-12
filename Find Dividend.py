'''                 Find Dividend

You are given array A, having some dividends. Further, you are given 3 numbers D, Q and R. A dividend can be found using a rule that states:
          Dividend = Divisor * Quotient + Remainder
your task is to find and return an integer value representing the index of the dividend if present in array. If dividend not found return -1.

Input Specification:
input1:An integer array A, containing dividends
input2:An integer D, representing divisor
input2:An integer Q, representing quotient
input2:An integer R, representing remainder
input2:An integer N, representing length of array A
Input:
A=[12,24,35,9]
D=8
Q=3
R=0
N=4
Output:1'''
A = [12, 24, 35, 9]
D = 8
Q = 3
R = 0
N = 4

def find_dividend_index(A, D, Q, R, N):
    # Calculate the expected dividend
    dividend = D * Q + R
    
    # Search for the dividend in the array
    for i in range(0,len(A)):
        if A[i] == dividend:
            return i  # Return the index if found

    return -1  # Return -1 if not found

print(find_dividend_index(A, D, Q, R, N))  
