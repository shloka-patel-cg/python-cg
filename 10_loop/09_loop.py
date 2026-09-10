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

count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print("Count of even numbers:", count)