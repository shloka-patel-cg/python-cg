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
ch = input("Enter a character: ")

if "A" <= ch <= "Z":
    print("Uppercase alphabet")
elif "a" <= ch <= "z":
    print("Lowercase alphabet")
elif "0" <= ch <= "9":
    print("Digit")
else:
    print("Special character")
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
char = input("Enter a single character: ")

if 'A' <= char <= 'Z':
    print("Uppercase alphabet")
elif 'a' <= char <= 'z':
    print("Lowercase alphabet")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special character")
char = input("Enter a single character: ")

# Check if the character is an alphabet letter
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    # Convert to lowercase to simplify vowel checking
    lower_char = char.lower()
    
    if lower_char in ('a', 'e', 'i', 'o', 'u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit = {profit}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss = {loss}")
else:
    print("No profit and no loss")
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if cost_price <= 0:
    print("Invalid cost price. Cost price must be greater than 0.")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print(f"Profit Percentage = {profit_percentage:.2f}%")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print(f"Loss Percentage = {loss_percentage:.2f}%")
else:
    print("No profit, no loss (0%)")
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units entered.")
elif units <= 100:
    bill = units * 5
    print(f"Total Electricity Bill = ₹{bill}")
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print(f"Total Electricity Bill = ₹{bill}")
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print(f"Total Electricity Bill = ₹{bill}") 
    num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ").strip()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ").strip()

if operator == '+':
    result = num1 + num2
    print(f"Result: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {result}")
else:
    print("Invalid operator entered.")
num = float(input("Enter a number: "))

if num < 0:
    print("Negative")
elif num <= 10:
    print("Number is between 0 and 10")
elif num <= 50:
    print("Number is between 11 and 50")
elif num <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")
a = float(input("Enter first side length: "))
b = float(input("Enter second side length: "))
c = float(input("Enter third side length: "))

# Check for positive side lengths and triangle inequality rule
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Valid triangle")
    else:
        print("Invalid triangle")
else:
    print("Invalid side lengths (must be greater than 0)")
a = float(input("Enter first side length: "))
b = float(input("Enter second side length: "))
c = float(input("Enter third side length: "))

# Step 1: Check triangle validity
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    # Step 2: Determine triangle type
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")
balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Withdrawal amount must be greater than 0.")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100.")
elif withdrawal > balance:
    print("Insufficient funds (amount exceeds account balance).")
elif balance - withdrawal < 500:
    print("Transaction rejected: At least ₹500 must remain in the account.")
else:
    remaining_balance = balance - withdrawal
    print("Withdrawal successful")
    print(f"Remaining balance: {remaining_balance:.2f}")
username = input("Enter username: ")
password = input("Enter password: ")

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"

if username != VALID_USERNAME:
    print("User not found")
elif password != VALID_PASSWORD:
    print("Wrong password")
else:
    print("Login successful")
amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount entered.")
else:
    if amount < 500:
        discount_percent = 0
    elif amount <= 999:
        discount_percent = 5
    elif amount <= 1999:
        discount_percent = 10
    elif amount <= 4999:
        discount_percent = 15
    else:
        discount_percent = 20

    discount_amount = (amount * discount_percent) / 100
    final_amount = amount - discount_amount

    print(f"Original amount: ₹{amount:.2f}")
    print(f"Discount percentage: {discount_percent}%")
    print(f"Discount amount: ₹{discount_amount:.2f}")
    print(f"Final amount: ₹{final_amount:.2f}")
    day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Check if year and month are in basic valid ranges
if year <= 0 or month < 1 or month > 12:
    print("Invalid")
else:
    # Determine if the year is a leap year
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    # Determine maximum days allowed in the given month
    if month == 2:
        if is_leap:
            max_days = 29
        else:
            max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31

    # Validate day range
    if 1 <= day <= max_days:
        print("Valid")
    else:
        print("Invalid")
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if (0 <= hours <= 23) and (0 <= minutes <= 59) and (0 <= seconds <= 59):
    print("Valid time")
else:
    print("Invalid time")
name1 = input("Enter name 1: ")
age1 = int(input("Enter age 1: "))

name2 = input("Enter name 2: ")
age2 = int(input("Enter age 2: "))

name3 = input("Enter name 3: ")
age3 = int(input("Enter age 3: "))

# Check for equal age cases
if age1 == age2 == age3:
    print(f"All three ({name1}, {name2}, and {name3}) are of the same age.")
elif age1 == age2 and age1 < age3:
    print(f"{name1} and {name2} are the youngest.")
elif age1 == age3 and age1 < age2:
    print(f"{name1} and {name3} are the youngest.")
elif age2 == age3 and age2 < age1:
    print(f"{name2} and {name3} are the youngest.")

# Check for single youngest person
elif age1 < age2 and age1 < age3:
    print(f"{name1} is the youngest")
elif age2 < age1 and age2 < age3:
    print(f"{name2} is the youngest")
else:
    print(f"{name3} is the youngest")

 age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

is_eligible = True

# Check each requirement individually
if not (18 <= age <= 25):
    print("Reason: Age must be between 18 and 25.")
    is_eligible = False

if marks < 85:
    print("Reason: Marks must be 85 or above.")
    is_eligible = False

if attendance < 75:
    print("Reason: Attendance must be 75% or above.")
    is_eligible = False

if income > 300000:
    print("Reason: Family income must be ₹300,000 or below.")
    is_eligible = False

if is_eligible:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")