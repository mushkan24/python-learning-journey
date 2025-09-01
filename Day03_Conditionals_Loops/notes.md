# Day 3 - Conditionals & Loops

## 🔹 Conditionals (if/elif/else)
- Used to execute code only if a condition is true.

x = 10

if x > 0:

    print("Positive")

elif x == 0:

    print("Zero")

else:

    print("Negative")

Conditions can use operators:

Comparison: ==, !=, <, >, <=, >=

Logical: and, or, not

## 🔹 Loops

1. While Loop

Runs as long as the condition is true.

i = 1

while i <= 5:

    print(i)

    i += 1

2. For Loop

Iterates over a sequence (list, string, range).

for i in range(5):

    print(i)  # 0 to 4

for ch in "Python":

    print(ch)

## 🔹 Loop Control Statements

break → exits loop immediately

continue → skips current iteration

pass → placeholder (does nothing)

for i in range(5):

    if i == 3:

        break   # loop ends at 3

    print(i)

for i in range(5):

    if i == 2:

        continue   # skip 2

    print(i)

# ✅ Key Takeaways

Use if/elif/else for decisions.

Use while when you don’t know iterations in advance.

Use for when you know the sequence/range.

Loop control (break, continue, pass) helps handle flow.