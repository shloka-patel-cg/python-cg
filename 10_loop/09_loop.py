for _ in range(5):
    print("Hello")
for i in range(10):
    print(i, end=" ")
for i in range(1, 11):
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in range(5, 51, 5):
    print(i)
for i in range(2, 21, 2):
    print(i)
for i in range(1, 20, 2):
    print(i)
for i in range(3, 19, 3):
    print(i, end=" ")
for i in range(20, 1, -2):
    print(i)
n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    print(i)
n = int(input("Enter a positive integer n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
n = int(input("Enter a positive integer n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
n = int(input("Enter a positive integer n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
n = int(input("Enter a positive integer n: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
n = int(input("Enter a positive integer n: "))

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print("Count of even numbers:", count)

n = int(input("Enter a number: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print("Sum:", total_sum)

n = int(input("Enter a number: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print("Sum:", total_sum)

n = int(input("Enter a number: "))
even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i

print("Sum of even numbers:", even_sum)

n = int(input("Enter a number: "))
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i

print("Sum of odd numbers:", odd_sum)

text = input("Enter a string: ")

for char in text:
    print(char)

text = input("Enter a string: ")

text = input("Enter a string: ")
count = 0

for char in text:
    count += 1

print("Total characters:", count)

text = input("Enter a string: ")
count = 0

for char in text:
    if char == "a":
        count += 1

print("Occurrences of 'a':", count)

text = input("Enter a string: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0

for char in text:
    if char in uppercase_letters:
        count += 1

print("Uppercase characters count:", count)

for i in range(3):  # Outer loop for 3 rows
    for j in range(4):  # Inner loop for 4 stars per row
        print("*", end="")
    print()  # Move to the next line after completing a row

for i in range(1, 6):  # Rows: 1 to 5
    for j in range(1, 6):  # Columns: 1 to 5
        print(i * j, end="\t")  # Print product followed by a tab space
    print()  # Move to the next row


