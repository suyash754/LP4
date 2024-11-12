from collections import Counter

string = "abbcddffffffff"

# Count occurrences of each fruit
s_count = Counter(string)

max_s = max(s_count, key=s_count.get)
print(max_s)

max_frequency = s_count[max_s]
print(max_frequency)
