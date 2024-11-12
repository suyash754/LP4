from collections import Counter

# Sample input
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Count occurrences of each fruit
fruit_count = Counter(fruits)

max_fruit = max(fruit_count, key=fruit_count.get)
print(max_fruit)

max_frequency = fruit_count[max_fruit]
print(max_frequency)
