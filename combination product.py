"""Number of combinations leading to a product

You are given an array of integers arr of length n and a positive integer m.Find and print the number of possible unique triplets(a combination of 3 numbers) having product m from array arr and print the count

Note:No element is repeated in the given array

Input Format:
The input consists of 3 lines:
the first line contains an integer,i.e.m
the second line contains an integer n,i.e.the length of arr
the third line contains n space-separated integers,i.e.the elements of arr

Output Format: the output consists of a single integer,i.e. the count of unique triplets having product m

Example:
Input:
60
7
5 3 20 10 1 4 2

Output:3"""
m = 36  
n = 5  
arr = [9,18,2,1,4]

def count_triplets_with_product_m(m, arr):
    n = len(arr)
    count = 0
    
    # Use three nested loops to find all unique triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the product of arr[i], arr[j], arr[k] equals m
                if arr[i] * arr[j] * arr[k] == m:
                    count += 1
    
    return count

print(count_triplets_with_product_m(m, arr))
