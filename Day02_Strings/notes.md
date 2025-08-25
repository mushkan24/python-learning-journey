# Day 2 - Strings in Python

## 🔹 What are Strings?
- A string is a sequence of characters inside single quotes `' '`, double quotes `" "`, or triple quotes `''' '''`.
- Strings are **immutable** → once created, they cannot be changed (but you can create new ones).

s1 = 'hello'

s2 = "world"

s3 = '''multi-line
string'''

## 🔹 String Operations
Concatenation

a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
Repetition

print("Hi! " * 3)   # Hi! Hi! Hi!
Indexing & Slicing

s = "Python"
print(s[0])     # P
print(s[-1])    # n
print(s[0:4])   # Pyth

## 🔹 String Methods
Some commonly used:

upper(), lower(), title()

strip() → remove whitespace

replace("a", "b")

find("sub") / count("x")

split(" ") → breaks into list

join(list) → joins list into string

msg = "  hello python  "
print(msg.upper())     # HELLO PYTHON
print(msg.strip())     # hello python
print(msg.replace("python", "world"))  # hello world

## 🔹 f-Strings (Formatted Strings)

name = "Mushkan"
age = 22
print(f"My name is {name}, I am {age} years old.")

## ✅ Key Takeaways

Strings are immutable sequences of characters.

Use slicing to extract parts of strings.

String methods simplify text manipulation.

Use f-strings for readable formatting.

