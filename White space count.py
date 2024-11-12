'''                 White Space Difference
You are given 2 strings A and B. Your task is to find and return a string saying 'Even' if the value representing the absolute difference between the number of whitespaces in both the strings is divisible by 2 else 'Odd' if the value representing the absolute differences between the number of whitespaces in both the string the whitespace is not divisible by 2 along with the difference value

Input Specification:
input1:A string A
input2:A string B

Output: even'''

def whitespace_difference(A, B):
    # Count whitespaces in both strings
    count_A = A.count(' ')
    count_B = B.count(' ')

    # Calculate the absolute difference
    difference = abs(count_A - count_B)

    # Check if the difference is even or odd
    if difference % 2 == 0:
        return "Even"
    else:
        return f"Odd {difference}"

A = "Hello World"
B = "Hi therefolks"
print(whitespace_difference(A, B))  # Output could be "Odd 2" or "Even" depending on whitespace difference

A="Suyash Chavan"
B="Suyash Surendra Chavan"
print(whitespace_difference(A, B))