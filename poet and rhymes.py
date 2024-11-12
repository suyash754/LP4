'''Poet and Rhymes
A poet has asked you for assistance in writing poems. He has given you a string S and a dictionary D and he asks you to find, from the dictionary, a word which rhymes best with S.Words are said to rhyme when the last syllables of the words are the same, like "cave" and "gave", or "typical" and "critical". the words will be deemed to rhyme best if the last few characters of the words match the most.

Your tassk is to find and return a string value denoting the word which rhymes best with S, from the dictionary D. If no such word is found, return the string "No Word".

Input Specification:
input1: A string value S, representing a single word
input2: A string array D, representing the dictionary
input3: An integer value, representing the length of array D

Output Specification:Return a string value denoting the word which rhymes best with S from the dictionary D. If no such word is found return the string "No word"

Example:
input1:thunder
input2:(puzzle,thunder,powder,blender,under)
input3:5

output:under'''
def best_rhyme(S, D):
    best_match = "No Word"
    max_suffix_length = 0

    for word in D:
        # Start from the end of the word and check for matching suffix length
        suffix_length = 0
        # Iterate backward and compare suffixes
        while suffix_length < len(S) and suffix_length < len(word) and S[-(suffix_length + 1)] == word[-(suffix_length + 1)]:
            suffix_length += 1

        # Update best match if a longer matching suffix is found
        if suffix_length > max_suffix_length:
            max_suffix_length = suffix_length
            best_match = word

    return best_match

print(best_rhyme("thunder", ["puzzle", "powder", "blender", "under"]))  # Expected output: "under"
print(best_rhyme("pole", ["kilo", "super", "cake"]))  # Expected output: "cake"
