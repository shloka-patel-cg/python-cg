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

            










 










































































































































































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    