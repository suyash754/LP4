'''convert the decimal into binary and add it's bits

Input:10
output:2

Explanation:
10->1010->1+0+1+0->2'''
n = 7

def sum_of_binary_bits(n):
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Count and sum the '1' bits
    sum = binary_representation.count('1')
    
    return sum

print(sum_of_binary_bits(n)) 
