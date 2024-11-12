'''Quest for the Hidden case

Given two strings S1 and S2, there a secret coded encoded in their character. Your task is to find and return this secret code. The secret code is the sum of the ascii values of the characters in the longest common substring between S1 and S2.

Output Specification:
Return an integer value representing the encoded secret of the strings by finding the sum of the ascii values of the characters in the longest common substring between these two strings.

Example 1:
input1:adventure
input2:future

Output:448

Explanation:
Here the string S1 is "adventure" and S2 is "future". the longest common substring between S1 and S2 is "ture" with their ASCII values summing up to 448(116+117+101). Therefore 448 is returned as the output

'''
def longest_common_substring_ascii_sum(s1, s2):
    max_length = 0
    ascii_sum = 0
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            # Determine the longest common substring starting at s1[i] and s2[j]
            k = 0
            while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
                k += 1

            # Update max_length and ascii_sum if we found a longer common substring
            if k > max_length:
                max_length = k
                ascii_sum = sum(ord(char) for char in s1[i:i + k])
    
    return ascii_sum

s1 = "adventure"
s2 = "future"
print(longest_common_substring_ascii_sum(s1, s2))  # Output: 448
