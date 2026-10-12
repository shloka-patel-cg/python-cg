# #Q-1
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print(" you selectedPizza")
#     case 2:
#         print("you selected Burger")
#     case 3:
#         print("you selected Pasta")
#     case 4:
#         print("you selected Sandwich")   
#     case _:
#         print("Invalid choice")
# #Q-2
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("you selected wi-fi")
#     case 2:
#         print("you selected Bluetooth")
#     case 3:
#         print("you selected Mobile Data")
#     case 4:
#         print("you selected Arirplane Mode")   
#     case _:
#         print("Exit")
# #Q-3
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("you selected Check Balance")
#     case 2:
#         print("you selected Withdraw Money")
#     case 3:
#         print("you selected Deposit Money")
#     case 4:
#         print("you selected Change PIN")   
#     case _:
#         print("Exit")
# #Q-4
# color=input("Enter your color: ")
# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _ :
#         print("Invalid signal")
# #Q-5
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Opening profile")
#     case 2: 
#         print("Opening Courses")  
#     case 3:
#         print("Opening Marks")
#     case 4:
#         print("Opening Attendance") 
#     case _:
#         print("logout") 
# #Q-6
# category=int(input("Enter category: "))
# match category:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("opening Clothing")
#     case 3:
#         print("opening Grocery")  
#     case 4: 
#         print("opening books")
#     case _:
#         print("Exit")    
# # Q-7
# service=int(input("Enter your service: "))  
# match service:
#     case 1:
#         print("opening Account Balance")
#     case 2:
#         print("opening mini statement")
#     case 3:
#         print("opening Fund Transfer")
#     case 4:
#         print("opening Bill Payment")
#     case _:
#         print("opening Customer Support") 
# #Q-8
# show=int(input("Enter your show: "))
# match show:
#     case 1:
#         print("Morning Show selected")
#     case 2:
#         print("Afternoon Show selected")
#     case 3:
#         print("Evening Show selected")
#     case 4:
#         print("Night Show selected")
#     case _:
#         print("Invalid show")
# #Q-9
# Weather=input("enter weather: ")
# match Weather:
#     case "sunny":
#         print("Wear sunglasses")
#     case "rainy":
#         print("Carry an umbrella") 
#     case "cloudy":
#         print("Weather may change") 
#     case "snowy":
#         print("Wear warm clothes")
#     case _:
#      print("Unknown Weather")  
# #Q-10
# method=input("enter payment method: ")
# match method:
#     case "upi":
#         print("UPI Payment Selected")
#     case "card":
#         print("card Payment Selected") 
#     case "cash":
#         print("cash Payment Selected") 
#     case "wallet":
#         print("UPI Payment Selected")
#     case _:
#      print("Unknown method")
# #Q-11
# file=input("Enter extension:")
# match file:
#     case "pdf":
#         print("Document file")
#     case "jpg":
#         print("jpg image file") 
#     case "png":
#         print("png image file") 
#     case "mp3":
#         print("Audio file")  
#     case "mp4":
#         print("Video file") 
#     case _:
#         print("Unknown File Type")
# #Q-12
# rule=input("enter the rule:")
# match rule:
#     case "admin":
#         print("Full Access")
#     case "teacher":
#         print("Teacher Dashboard")
#     case "student":
#         print("Student Dashboard")
#     case "guest":
#         print("Limited Access") 
#     case _:
#         print("Invalid Role")   
# # Q-13
# day=int(input("enter the day number:"))
# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Wekkend")
#     case _:
#         print("Invalid Day")  
# #Q-14
# property=int(input("Enter priority numbers:"))
# match property:
#     case 1|2:
#         print("Normal Priority")
#     case 3|4:
#         print("Urgent Priority") 
#     case _:
#         print("Invalid priority") 
# #Q-15
# member=int(input("Enter the membership levels:"))
# match member:
#     case 1|2:
#         print("Basic Membership")
#     case 3|4:
#         print("Premium Membership") 
#     case _:
#         print("Invalid membership") 
# #Topic-5 
# #Q-16
# select=input("user selected:")
# chioce=int(input("enter the choice:"))
# match select:
#     case "student":
#         match chioce:
#               case 1:
#                   print("View Courses")
#               case 2:
#                   print("View Marks") 
#               case 3:
#                 print("View Attendance")
#               case _:
#                 print("Invalid choice")  
#     case "teacher":
#         match chioce:
#             case 1:
#                 print("View student")
#             case 2:
#                 print("enter Marks") 
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid choice")     
#     case _:
#         print("Invalid selection") 
# #Q-17
# account=int(input("Enter the account type:"))
# opration=int(input("Enter the operation:"))
# match account:
#     case 1:
#         match opration:
#             case 1:
#                 print("View Balance selected")
#             case 2:
#                 print("Withdraw Money selected") 
#             case 3:
#                 print("Deposit Money selected")
#             case _:
#                 print("Invalid operation")  
#     case 2:
#         match opration:
#             case 1:
#                 print("View Balance")
#             case 2:
#                 print("Withdraw Money") 
#             case 3:
#                 print("Deposit Money")
#             case _:
#                 print("Invalid operation")  
#     case _:
#         print("Invalid account type")
# #Q-18
# category = int(input("Enter category: "))
# # 1 -> Electronics, 2 -> Clothing

# match category:
#     case 1:
#         print("Category: Electronics")
#         product = int(input("Enter product: "))
#         # 1 -> Mobile, 2 -> Laptop, 3 -> Headphones

#         match product:
#             case 1:
#                 print("You selected: Mobile")
#             case 2:
#                 print("You selected: Laptop")
#             case 3:
#                 print("You selected: Headphones")
#             case _:
#                 print("Invalid product selection for Electronics")
    
#     case 2:
#         print("Category: Clothing")
#         product = int(input("Enter product: "))
#         # 1 -> Shirt, 2 -> Jeans, 3 -> Shoes
        
#         match product:
#             case 1:
#                 print("You selected: Shirt")
#             case 2:
#                 print("You selected: Jeans")
#             case 3:
#                 print("You selected: Shoes")
#             case _:
#                 print("Invalid product selection for Clothing")
    
#     case _:
#         print("Invalid category")

#Q-19
# category = int(input("Enter category: "))
# food = int(input("Enter food: "))

# match category:
#     case 1: # Vegetarian
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")        
#             case 3:     
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")
#     case 2: # Non-Vegetarian
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")
#     case _:
#         print("Invalid Category")  

# Topic-6
# Q.20
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         result = num1 + num2
#         print(f"Result = {result}")
#     case "-":
#         result = num1 - num2
#         print(f"Result = {result}")
#     case "*":
#         result = num1 * num2
#         print(f"Result = {result}")
#     case "/":
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#         else:
#             result = num1 / num2
#             print(f"Result = {result}")
#     case _:
#         print("Invalid operator selected.")
# Q.21
# choice = int(input("Enter choice: "))
# temp = float(input("Enter temperature: "))

# match choice:
#     case 1:
#         # Celsius to Fahrenheit: (C * 9/5) + 32
#         converted = (temp * 9/5) + 32
#         print(f"Temperature = {converted} F")
#     case 2:
#         # Fahrenheit to Celsius: (F - 32) * 5/9
#         converted = (temp - 32) * 5/9
#         print(f"Temperature = {converted} C")
#     case _:
# print("Invalid choice selected.")
# Q.22
# choice = int(input("Enter choice: "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         result = value * 1000
#         print(f"{int(result) if result.is_integer() else result} meters")
#     case 2:
#         result = value / 1000
#         print(f"{int(result) if result.is_integer() else result} kilometers")
#     case 3:
#         result = value * 1000
#         print(f"{int(result) if result.is_integer() else result} grams")
#     case 4:
#         result = value / 1000
#         print(f"{int(result) if result.is_integer() else result} kilograms")
#     case _:
#         print("Invalid choice selected.")

# Topic-7
# Q.23
# account_type = int(input("Enter account type: "))
# amount = float(input("Enter amount: "))

# match account_type:
#     case 1:
#         print("Savings Account")
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case 2:
#         print("Current Account")
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case _:
#        print("Invalid Account Type")
# Q.24
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         age = int(input("Enter age: "))
#         if age >= 18:
#             print("You can start the exam")
#         else:
#             print("You must be at least 18 years old to start the exam.")
#     case 2:
#         print("View Result Selected")
#     case 3:
#         print("Exiting portal...")
#     case _:
#         print("Invalid choice selected.")
# Q.25
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         ticket_type = "Regular Ticket"
#     case 2:
#         ticket_type = "Premium Ticket"
#     case 3:
#         ticket_type = "VIP Ticket"
#     case _:
#         ticket_type = "Invalid Choice"

# if ticket_type != "Invalid Choice":
#     age = int(input("Enter age: "))
#     if age < 5:
#         print("Free Entry")
#     else:
#         print(ticket_type)
# else:
#     print("Invalid ticket choice selected.")

# Topic-8
# Q.26
# device = int(input("Enter device: "))

# match device:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid Device Selection")
# Q.28
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Book Ticket Selected")
#     case 2:
#         print("Cancel Ticket Selected")
#     case 3:
#         print("Check PNR Selected")
#     case 4:
#         print("Train Schedule Selected")
#     case 5:
#         print("Exiting Railway System...")
#     case _:
#         print("Invalid Choice")
# Q.29
# Take choice input from the user
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Search Book Selected")
#     case 2:
#         print("Issue Book Selected")
#     case 3:
#         print("Return Book Selected")
#     case 4:
#         print("View Issued Books Selected")
#     case 5:
#         print("Exiting Library Management System...")
#     case _:
#         print("Invalid Choice")
#         print("Invalid Choice")
# Q.30
# status = input("Enter status: ").strip().lower()

# match status:
#     case "placed":
#         print("Output: Your order has been placed successfully.")
#     case "confirmed":
#         print("Output: Your order has been confirmed by the restaurant.")
#     case "preparing":
#         print("Output: Your food is being prepared.")
#     case "out_for_delivery":
#         print("Output: Your order is on the way")
#     case "delivered":
#         print("Output: Your order has been delivered. Enjoy your meal!")
#     case "cancelled":
#         print("Output: Your order has been cancelled.")
#     case _:
#         print("Output: Invalid status entered.")

# Topic-9
# Q.31
# banking_type = int(input("Enter banking type: "))
# option = int(input("Enter option: "))

# match banking_type:
#     case 1:  
#         match option:
#             case 1:
#                 print("Personal Balance Selected")
#             case 2:
#                 print("Personal Transfer Selected")
#             case 3:
#                 print("Personal Loan Selected")
#             case _:
#                 print("Invalid Option")
#     case 2:  
#         match option:
#             case 1:
#                 print("Business Balance Selected")
#             case 2:
#                 print("Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid Banking Type")
# Q.32
# role = int(input("Enter role (1: Student, 2: Teacher, 3: Parent): "))
# option = int(input("Enter option: "))

# match role:
#     case 1:  
#         match option:
#             case 1:
#                 print("Student Marks Selected")
#             case 2:
#                 print("Student Attendance Selected")
#             case 3:
#                 print("Student Homework Selected")
#             case _:
#                 print("Invalid Student Option")
#     case 2:  
#         match option:
#             case 1:
#                 print("Enter Marks Selected")
#             case 2:
#                 print("Teacher Attendance Selected")
#             case 3:
#                 print("Assign Homework Selected")
#             case _:
#                 print("Invalid Teacher Option")
#     case 3:  
#         match option:
#             case 1:
#                 print("Child Marks Selected")
#             case 2:
#                 print("Child Attendance Selected")
#             case 3:
#                 print("Contact Teacher Selected")
#             case _:
#                 print("Invalid Parent Option")
#     case _:
#         print("Invalid Role Selected")
# Q.33
# transport = int(input("Enter transport (1: Flight, 2: Train, 3: Bus): "))
# option = int(input("Enter option: "))

# match transport:
#     case 1:  
#         match option:
#             case 1:
#                 print("Economy Flight Selected")
#             case 2:
#                 print("Business Flight Selected")
#             case _:
#                 print("Invalid Flight Option")
#     case 2:  
#         match option:
#             case 1:
#                 print("Sleeper Train Selected")
#             case 2:
#                 print("AC Train Selected")
#             case _:
#                 print("Invalid Train Option")
#     case 3:  
#         match option:
#             case 1:
#                 print("Ordinary Bus Selected")
#             case 2:
#                 print("Volvo Bus Selected")
#             case _:
#                 print("Invalid Bus Option")
#     case _:
#         print("Invalid Transport Selection")
# Q.34
# choice = int(input("Enter choice (1: Start, 2: Load, 3: Settings, 4: Exit): "))

# match choice:
#     case 1:
#         print("Start Game Selected")
#     case 2:
#         print("Load Game Selected")
#     case 3:
#         setting_option = int(input("Enter settings option (1: Sound, 2: Graphics, 3: Controls): "))
#         match setting_option:
#             case 1:
#                 print("Sound Settings Selected")
#             case 2:
#                 print("Graphics Settings Selected")
#             case 3:
#                 print("Controls Settings Selected")
#             case _:
#                 print("Invalid Settings Option")
#     case 4:
#         print("Exiting Gaming Console...")
#     case _:
#         print("Invalid Choice")
# Topic-10
# Q.35
# category = int(input("Enter category (1: Starters, 2: Main Course, 3: Desserts, 4: Drinks): "))
# item = int(input("Enter item choice: "))

# match category:
#     case 1: 
#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid Starter Option")
#     case 2:  
#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid Main Course Option")
#     case 3:  
#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid Dessert Option")
#     case 4:  
#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid Drink Option")
#     case _:
#                 print("Invalid Category Selection")
# Q.36
# category = int(input("Enter category (1: Starters, 2: Main Course, 3: Desserts, 4: Drinks): "))
# item = int(input("Enter item choice: "))

# match category:
#     case 1:  
#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid Starter Option")
#     case 2:  
#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid Main Course Option")
#     case 3:  
#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid Dessert Option")
#     case 4:  
#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid Drink Option")
#     case _:
#                 print("Invalid Category Selection")
# Q.37
# category = int(input("Enter category (1: Programming, 2: Mathematics, 3: Communication): "))
# option = int(input("Enter option: "))

# match category:
#     case 1:  
#         match option:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid Programming Option")
#     case 2:  
#         match option:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid Mathematics Option")
#     case 3:  
#         match option:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid Communication Option")
#     case _:
#         print("Invalid Category Selection")
# Q.38
# main_option = int(input("Enter main option (1: Engine, 2: Lights, 3: Music, 4: Navigation): "))
# sub_option = int(input("Enter sub-option: "))

# match main_option:
#     case 1:  
#         match sub_option:
#             case 1:
#                 print("Engine Start Selected")
#             case 2:
#                 print("Engine Stop Selected")
#             case _:
#                 print("Invalid Engine Option")
#     case 2:  
#         match sub_option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid Lights Option")
#     case 3:  
#         match sub_option:
#             case 1:
#                 print("Play Music Selected")
#             case 2:
#                 print("Pause Music Selected")
#             case 3:
#                 print("Next Track Selected")
#             case 4:
#                 print("Previous Track Selected")
#             case _:
#                 print("Invalid Music Option")
#     case 4:  
#         match sub_option:
#             case 1:
#                 print("Start Navigation Selected")
#             case 2:
#                 print("Stop Navigation Selected")
#             case _:
#                 print("Invalid Navigation Option")
#     case _:
#         print("Invalid Main Option Selection")
# Topic-11
# Q.39
# main_menu = int(input("Enter main menu (1: Employee, 2: Manager): "))
# option = int(input("Enter option: "))

# match main_menu:
#     case 1:  
#         match option:
#             case 1:
#                 print("View Profile Selected")
#             case 2:
#                 leave_days = int(input("Enter number of leave days: "))
#                 if leave_days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")
#             case 3:
#                 print("View Salary Selected")
#             case _:
#                 print("Invalid Employee Option")
#     case 2: 
#         match option:
#             case 1:
#                 print("View Team Selected")
#             case 2:
#                 print("Approve Leave Selected")
#             case 3:
#                 print("View Reports Selected")
#             case _:
#                 print("Invalid Manager Option")
#     case _:
#         print("Invalid Main Menu Selection")
# Q.40
# role = int(input("Enter role: "))
# option = int(input("Enter option: "))

# match role:
#     case 1:  
#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case 4:
#                 print("Opening Student Courses")
#             case _:
#                 print("Invalid Student Option")
#     case 2:  
#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Opening Enter Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case 4:
#                 print("Opening Teacher Courses")
#             case _:
#                 print("Invalid Teacher Option")
#     case 3: 
#         match option:
#             case 1:
#                 print("Opening Administration Fees")
#             case 2:
#                 print("Opening Administration Admissions")
#             case 3:
#                 print("Opening Administration Notices")
#             case 4:
#                 print("Opening Administration Departments")
#             case _:
#                 print("Invalid Administration Option")
#     case _:
#         print("Invalid Role Selected")
































































































































































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    