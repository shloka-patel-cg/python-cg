# que=1
def city():
    city_name="Pune"
    print(city_name)

city()

# que=2
school_name="ABC School"

def school():
    print(school_name)

school()    

# que=3
      
if True:
    grade = "A"

print(grade)

# que=4

for i in range(3):
    pass

print(i)

# predict the output:

# que=6
200
100

# que=7

clicks = 0
def click():
    global clicks
    clicks += 1

# que=9

def outer():
    message = "Hello from outer!"

    def inner():
        print(message)

    inner()

outer()

# que=10

def make_shopping_list():
    items = ["apples", "bread"]
    return items

my_list = make_shopping_list()
my_list.append("milk")
my_list[0] = "green apples"

print(my_list)

# que=11

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

next_count = make_counter()
print(next_count())  
print(next_count())  
print(next_count())  

# que=12
3
2
1

# que=14

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = make_greeter("Hello")
print(say_hello("Asha"))  # Hello, Asha!

# que=15

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

times_three = make_multiplier(3)
print(times_three(10))  # 30