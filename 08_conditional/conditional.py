num = int(input("Enter a number: "))
if num > 10:
    print("Greater than 10")
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Not positive")
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
day = int(input("Enter day number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Other")
marks = int(input("Enter marks: "))

if marks >= 75:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
num = int(input("Enter a number: "))

if num == 1:
    print("1")
elif num == 2:
    print("2")
elif num == 3:
    print("3")
else:
    print("Other")
age = int(input("Enter age: "))

if age >= 18:
    if age <= 60:
        print("Between 18 and 60")
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")
age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")
else:
    print("Minor")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
age = int(input("Enter age: "))
has_id = True

if age >= 18 and has_id is True:
    print("Allowed")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > 10 and second > 10:
    print("Both are greater than 10")
num = int(input("Enter a number: "))

if num < 0 or num > 100:
    print("Special")
is_closed = False

if not is_closed:
    print("Open")
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Between 10 and 50")
num = int(input("Enter a number: "))

if num < 10 or num > 50:
    print("Outside the range")
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

has_id = input("Do you have ID? (True/False): ")

if age >= 18 and marks >= 40 and has_id == "True":
    print("Eligible")
else:
    print("Not eligible")



    has_id = input("enter the value in (true or false): ").strip().lower()
    true=True
    false=False
    if has_id == "true":
        print("Welcome")
    elif has_id == "false":
        print("please bring your id!")
    else:
        print("enter the vaild value.")
