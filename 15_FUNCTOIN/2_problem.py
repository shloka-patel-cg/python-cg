# 1.
# def welcome():
#     print("Welcome to Python")


# welcome()
# welcome()
# welcome()

# 2.
# def greet(name):
#     print(f"Hello, {name}!")


# greet("Alice")

# 3.
# def show_number(number):
#     print(number)


# show_number(42)

# 4.
# def add(a, b):
#     return a + b


# result = add(5, 3)
# print(result)

# 5.
# def square(number):
#     return number ** 2

# 6.
# def is_even(number):
#     return number % 2 == 0

# 7.
# def is_even(number):
#     return number % 2 == 0

# 8.
# def introduce(name, city="Pune"):
#     print(f"Hi, I am {name} from {city}.")

# introduce("Aarav", "Mumbai")

# introduce("Priya")

# 9.
# def subtract(a, b):
#     return a - b


# result1 = subtract(10, 5)
# print(f"subtract(10, 5) = {result1}")

# result2 = subtract(5, 10)
# print(f"subtract(5, 10) = {result2}")

# 10.
# def get_min_max(a, b):
#     return min(a, b), max(a, b)


# smaller, larger = get_min_max(10, 4)
# print(f"Smaller: {smaller}, Larger: {larger}")

# 11.
# def calculate(a, b):
#     return a + b, a - b, a * b, a / b


# sum_val, diff, prod, quot = calculate(10, 2)
# print(f"Sum: {sum_val}, Difference: {diff}, Product: {prod}, Quotient: {quot}")

# 12.
# def count_digits(number):
#     return len(str(number))



# print(count_digits(0))     
# print(count_digits(12345))  

# 13.
# def classify_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"


# print(classify_number(15)) 
# print(classify_number(-7))  
# print(classify_number(0))    

# 14.
# def calculate_total(price, quantity=1):
#     return price * quantity


# print(calculate_total(50))      
# print(calculate_total(50, 3))   

# 15.
# def create_email(username, domain="example.com"):
#     return f"{username}@{domain}"


# print(create_email("john.doe"))                 
# print(create_email("jane.smith", "gmail.com"))  

# 16.
# def format_name(first, last, uppercase=False):
#     full_name = f"{first} {last}"
#     if uppercase:
#         return full_name.upper()
#     return full_name


# print(format_name("Alice", "Smith"))              
# print(format_name("Alice", "Smith", uppercase=True)) 

# 17.
# def percentage(marks, total=100):
#     return (marks / total) * 100


# print(percentage(75))         
# print(percentage(45, 50))     

# 18.
# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute


# print(convert_minutes(5))       
# print(convert_minutes(5, 60))   

# 19.
# def student_details(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")


# student_details(city="Mumbai", age=20, name="Rahul")

# 20.
# def bill(item, quantity=1, price=100):
#     return quantity * price

# print("Positional:", bill("Apple", 5, 20))         

# print("Keyword:", bill(price=50, item="Orange", quantity=3))  

# print("Defaults:", bill("Mango")) 

# 21
# def analyze_number(number):
#     if number < 0:
#         abs_val = -number
#     else:
#         abs_val = number

#     is_even = (number % 2 == 0)

#     num_digits = len(str(abs_val))

#     return abs_val, is_even, num_digits

# print(analyze_number(-42))   
# print(analyze_number(7))    
# print(analyze_number(0)) 

# 22
# def calculate_stats(a, b, c):
    
#     smallest = min(a, b, c)

#     largest = max(a, b, c)

    
#     total_sum = a + b + c

#     return smallest, largest, total_sum

# smallest, largest, total = calculate_stats(15, 3, 9)
# print(
#     f"Smallest: {smallest}, Largest: {largest}, Sum: {total}"
# )  

# print(calculate_stats(-5, 0, 10))  

# 23
# def make_sentence(subject, verb, obj):
    
#     return f"{subject} {verb} {obj}."

# sentence = make_sentence(obj="a mouse", subject="The cat", verb="chased")

# print(sentence)

# 24
# def apply_discount(price, discount=0):
#     final_price = price * (1 - discount / 100)
#     return final_price

# print(apply_discount(100)) 

# print(apply_discount(100, 20))  

# print(apply_discount(250, 15.5))  

# 25
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus


# print(calculate_pay(40))  

# print(calculate_pay(40, rate=250))  

# print(calculate_pay(35, 300, 1500))  

# print(calculate_pay(hours=30, bonus=500, rate=220)) 

# print(calculate_pay(25, bonus=1000))  

# 26
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())  

# print(get_coordinates(x=5))  

# print(get_coordinates(y=10)) 

# 27
# def compare(a, b):

#     if a > b:
#         comparison = "A is greater"
#     elif b > a:
#         comparison = "B is greater"
#     else:
#         comparison = "Equal"

#     if a > b:
#         diff = a - b
#     else:
#         diff = b - a

#     return comparison, diff

# print(compare(10, 5))   
# print(compare(3, 8))   
# print(compare(7, 7))    

# 28
# def convert_temperature(value, scale="C"):
#     if scale == "C":
    
#         return (value * 9 / 5) + 32
#     else:
    
#         return (value - 32) * 5 / 9

# print(convert_temperature(25, "C")) 
# print(convert_temperature(77, "F"))  
# print(convert_temperature(100))

# #29
# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"


# print(calculate_result(40))     
# print(calculate_result(30))    
# print(calculate_result(45, 50)) 
# print(calculate_result(55, 50))    

# 30
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     total_cost = (quantity * price) + delivery_fee
#     return total_cost

# total = order_summary("Laptop", delivery_fee=60)

# print(total) 



                                                                                                                                                                                                         