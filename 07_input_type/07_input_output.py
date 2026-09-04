name= input("Enter your name: ")
city= input("Enter your city: ")
print(f"My name is {name} and I live in {city}.")
#string type of value does input() return by default
print(type(name))
Frint_name = input("Enter your first name: ")
Last_name = input("Enter your last name: ")
print(f"Hello, {Frint_name} {Last_name}!")
name = input("Enter your name: ")
city = input("Enter your city: ")
collage = input("Enter your college name: ")
name,age = input("Enter your name and age: ").split()
print(f"My name is {name}, I am {age} years old.")
a,b = input("Enter two numbers separated by space: ").split()
print(f"The two numbers are {a} and {b}.")

a,b,c = map(int, input("Enter three value: ").split())
print(a)
print(b)
print(c)

Age = int(input("Enter your age: "))
Height = float(input("Enter your height: "))
Weight = int(input("Enter your weight: "))
print(type(Height))
print(f"Age: {Age}, Height: {Height}, Weight: {Weight}")
a = input()
b = input()

print(a + b)
a = input("Enter First  number: ")
b = input("Enter Second number: ")
print(a + b)

name = "Rahul"
Age = 25

print(f"My name is {name} and I am {Age} years old.")

a = 18
b = 20
c = a + b
print(c)

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"username {user_name}, age{age} .")

product_name = input("Enter your product name: ")
price = float(input("Enter your product price: "))
quantity = int(input("Enter your product quantity: "))

total_cost = price * quantity
print(f"Product: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))    
maark = float(input("Enter your mark: "))
print(f"Name: {name}, Age: {age}, Mark: {maark}")

#student_information
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_height = float(input("Enter your height: "))
student_city = input("Enter your city: ")
print(f"Name: {student_name}, Age: {student_age}, Height: {student_height}, City: {student_city}")
