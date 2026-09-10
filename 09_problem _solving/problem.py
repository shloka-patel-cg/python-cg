# Take input from the user
num = float(input("Enter a number: "))

# Check the sign of the number
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Take input from the user
num = int(input("Enter a number: "))

# Determine sign and parity directly
if num == 0:
    print("Zero")
elif num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")

# Take input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The larger number is: {num1}")
elif num2 > num1:
    print(f"The larger number is: {num2}")
else:
    print("Both are equal")

# Take input for three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare the numbers to find the smallest
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare num1 with num2 and num3
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("The smallest number is:", smallest)
# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare num1 with num2 and num3
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print output matching the format
if largest.is_integer():
    print(f"{int(largest)} is the largest")
else:
    print(f"{largest} is the largest")

 # Take input from the user
num = int(input("Enter a number: "))

# Check divisibility using modulo operator (%)
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
elif num % 3 == 0:
    print("Divisible only by 3")
elif num % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")
# Take marks from the user
marks = float(input("Enter marks: "))

# Check validity and pass/fail status
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
# Take input from the user
num = int(input("Enter a number: "))

# Check divisibility using modulo operator (%)
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible only by 5")
elif num % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")
# Take input from the user
num = int(input("Enter a number: "))

# Check divisibility using modulo operator (%)
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
elif num % 3 == 0:
    print("Divisible only by 3")
elif num % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")
# Take marks from the user
marks = float(input("Enter marks: "))

# Check validity and pass/fail status
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
# Take marks from the user
marks = float(input("Enter marks: "))

# Check validity and assign grade
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
# Take age from the user
age = int(input("Enter age: "))

# Check validity and voting eligibility
if age < 0:
    print("Invalid age")
elif age < 18:
    print("Cannot vote")
else:
    print("Can vote")
# Take input from the user
ch = input("Enter a character: ")

# Check validity (must be a single alphabetical character)
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
elif ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
Profit or Loss
