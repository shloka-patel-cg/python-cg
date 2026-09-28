# text = input("Enter a string: ")


# upper_case = 0
# lower_case = 0
# digit_count = 0
# space_count = 0
# special_count = 0


# for char in text:
#     if char.isupper():
#         upper_case += 1
#     elif char.islower():
#         lower_case += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif char.isspace():
#         space_count += 1
#     else:
#         special_count += 1


# print(f"Uppercase letters: {upper_case}")
# print(f"Lowercase letters: {lower_case}")
# print(f"Digits: {digit_count}")
# print(f"Spaces: {space_count}")
# print(f"Special characters: {special_count}")


# counts = {
#     "Uppercase Letters": upper_case ,
#     "Lowercase Letters": lower_case,
#     "Digits": digit_count,
#     "Spaces": space_count,
#     "Special Characters": special_count,
# }

# max_count = max(counts.values())

# highest_categories = [
#     category for category, count in counts.items() if count == max_count
# ]


# if len(highest_categories) > 1:
#     print("Highest Category: Tie")
# else:
#     print(f"Highest Category: {highest_categories[0]}")

# #Q.2
# for marks in range(1,11):
#     marks=float(input("enter your marks:"))
#     if marks >=75:
#         print("excellent")
#     elif marks>=50:
#         print("good")
#     elif marks>=35:
#         print("pass")
#     elif marks<35:
#         print("fail")

# #Q.3
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# vowels = "aeiouAEIOU"

# highest_score = -1
# highest_word = ""

# for word in words:
#     current_score = 0
#     for char in word:
#         if char in vowels:
#             current_score += 2
#         elif char.isalpha():
#             current_score += 1
#         elif char.isdigit():
#             current_score += 3
#         else:  
#             current_score += 4

#     if current_score > highest_score:
#         highest_score = current_score
#         highest_word = word

# print(f"Word with highest score: '{highest_word}' (Score: {highest_score})")

# #Q.4
# for i in range(1, 6):
#     password = input(f"Enter password for user {i}: ")

    
#     length_ok = len(password) >= 8
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False

    
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         else:
            
#             has_special = True


#     score = 0
#     if length_ok:
#         score += 1
#     if has_upper:
#         score += 1
#     if has_lower:
#         score += 1
#     if has_digit:
#         score += 1
#     if has_special:
#         score += 1

    
#     if score == 5:
#         strength = "Strong"
#     elif score >= 3:
#         strength = "Medium"
#     else:
#         strength = "Weak"

#     print(
#         f"Password {i} Strength: {strength} ({score}/5 conditions satisfied)\n"
#     )

# #Q.4
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# short_count = 0
# medium_count = 0
# long_count = 0

# for word in words:
#     length = len(word)

#     if length <= 3:
#         category = "Short"
#         short_count += 1
#     elif 4 <= length <= 6:
#         category = "Medium"
#         medium_count += 1
#     else:
#         category = "Long"
#         long_count += 1

#     print(f"Word: '{word}' | Length: {length} | Category: {category}")

# print("\n--- Summary ---")
# print(f"Short words (<= 3): {short_count}")
# print(f"Medium words (4-6): {medium_count}")
# print(f"Long words (> 6): {long_count}")

for marks in range(1,11):
     marks=float(input("enter your marks:"))
     if marks >=75:
        print("excellent")
     elif marks>=50:
         print("good")
     elif marks>=35:
         print("pass")
     elif marks<35:
         print("fail")

