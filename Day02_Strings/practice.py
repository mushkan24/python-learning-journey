# Day 2 - Strings Practice

# Creating strings
s1 = "Hello"
s2 = "Python"

# Concatenation
print(s1 + " " + s2)

# Repetition
print("Hi! " * 3)

# Indexing and Slicing
text = "Programming"
print(text[0])      # P
print(text[-1])     # g
print(text[0:6])    # Progra

# String methods
msg = "   Mushkan loves Python   "
print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("Python", "Coding"))

# Splitting and joining
words = msg.strip().split(" ")
print(words)
joined = "-".join(words)
print(joined)

# f-strings
name = "Elara"
age = 22
print(f"My name is {name}, and I am {age} years old.")

# 🚀 Small Exercise
# Take a string and:
# 1. Print the reverse of the string
# 2. Count how many vowels are in it
sample = "Artificial Intelligence"
print(sample[::-1])   # reverse

vowels = "aeiouAEIOU"
count = 0
for ch in sample:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
