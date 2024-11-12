'''Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
'''

arr = [9, 55, 2, 10, 54, 3]

def second_largest(arr):
    # Remove duplicates and sort in descending order
    unique_elements = sorted(set(arr), reverse=True)
    
    # Check if there's a second largest element
    if len(unique_elements) < 2:
        return -1
    else:
        return unique_elements[1]  # Return the second largest element

print(second_largest(arr))  
