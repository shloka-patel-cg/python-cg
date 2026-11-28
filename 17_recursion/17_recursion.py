# # que 1
# def show(n):
#     if n == 0:
#         print("Stop")
#         return
#     print(n)
#     show(n - 1)
#     print(n)
# show(2)
# output =  2
#           1
#         Stop
#           1
#          2
# 
# # que 2
# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)
# base-case = if n==0:
#              return 0

# # que 3
# def count(n):
#     if n == 0:
#         return
#     count(n + 1)
# bug = we are not calling the function.
#  ans def count(n):
#     if n <= 0:
#         return
#     count(n - 1)

# que 4
# def answer(n):
#     if n == 0:
#         return 0
#     n + answer(n - 1)
# print(answer(3))
#  on 36th line return i will write

# # que 5
# def countdown(n):
#     if n ==0:
#         return "Done!"
#     print(n)
#     return countdown(n-1)
# print(countdown(3))

# count = 0
# def fun(n,count):
#     if n == count:
#         return 
#     count += 1
#     print(count)
#     fun(n,count)

# fun(4,count)  **

# #Q-6
# def count_up(n):
#     if n==0:
#         return 
#     count_up(n-1)
#     print(n)
# count_up(4)
# #Q-7
# def sum_to(n):
#     if n==0:
#         return 0
#     return n +sum_to(n-1)
# print(sum_to(5))
# print(sum_to(0))
# #Q-8
# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(4))
# print(factorial(0))
# #Q-9
# def digit_sum(n):
#     if n < 10:
#         return n
#     return n % 10 + digit_sum(n // 10)
# print(digit_sum(583)) 
# print(digit_sum(7))    
# print(digit_sum(0))    

# #Q-10 
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)
# print(power(2, 5))
# Q-11
# def count_digits(n):
#     if n<10:
#         return 1
#     return 1 +count_digits(n//10)
# print(count_digits(555))
# #Q-12

# #Q-13
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))
# #Q-14
# #Q-15
# #Section D — Edge Cases and Debugging (10 marks)
# #16. Fix the factorial (3 marks)
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(0))
# ##Q-17
# def stop_at_zero(n):
#     if n == 0:
#         return

#     stop_at_zero(n)
# print(stop_at_zero(0))

# Q.12
# def reverse_text(text):
#     if text == "":          
#         return ""

#     return reverse_text(text[1:]) + text[0] 


# print(reverse_text("cat"))
# print(reverse_text("a"))
# print(reverse_text(""))

# Q.14
# def max_digit(n):
#     if n < 10:                 # Base case
#         return n

#     last_digit = n % 10
#     remaining_max = max_digit(n // 10)

#     if last_digit > remaining_max:
#         return last_digit
#     else:
#         return remaining_max


# print(max_digit(4729))
# print(max_digit(555))
# print(max_digit(0))



