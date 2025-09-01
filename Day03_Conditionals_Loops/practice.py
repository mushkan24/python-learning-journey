# Day 3 - Conditionals & Loops Practice

# --- Conditionals ---
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# --- While Loop ---
print("\nCounting 1 to 5 using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# --- For Loop ---
print("\nIterating over a string:")
for ch in "Mushkan":
    print(ch)

print("\nRange example:")
for i in range(1, 6):
    print(i)

# --- Loop Control ---
print("\nUsing break:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\nUsing continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# --- 🚀 Small Exercises ---
# 1. Print all even numbers from 1 to 20
print("\nEven numbers 1-20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

# 2. Calculate the sum of numbers from 1 to 100
print("\n\nSum of 1 to 100:")
total = 0
for i in range(1, 101):
    total += i
print(total)
