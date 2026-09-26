text = input("Enter a string: ")


upper_case = 0
lower_case = 0
digit_count = 0
space_count = 0
special_count = 0


for char in text:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        special_count += 1


print(f"Uppercase letters: {upper_case}")
print(f"Lowercase letters: {lower_case}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Special characters: {special_count}")


counts = {
    "Uppercase Letters": upper_case ,
    "Lowercase Letters": lower_case,
    "Digits": digit_count,
    "Spaces": space_count,
    "Special Characters": special_count,
}

max_count = max(counts.values())

highest_categories = [
    category for category, count in counts.items() if count == max_count
]


if len(highest_categories) > 1:
    print("Highest Category: Tie")
else:
    print(f"Highest Category: {highest_categories[0]}")

#Q.2

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

#Q.3
sentence = input("Enter a sentence: ")

words = sentence.split()

vowels = "aeiouAEIOU"

highest_score = -1
highest_word = ""

for word in words:
    current_score = 0
    for char in word:
        if char in vowels:
            current_score += 2
        elif char.isalpha():
            current_score += 1
        elif char.isdigit():
            current_score += 3
        else:  
            current_score += 4

    if current_score > highest_score:
        highest_score = current_score
        highest_word = word

print(f"Word with highest score: '{highest_word}' (Score: {highest_score})")

#Q.4
for i in range(1, 6):
    password = input(f"Enter password for user {i}: ")

    
    length_ok = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            
            has_special = True


    score = 0
    if length_ok:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(
        f"Password {i} Strength: {strength} ({score}/5 conditions satisfied)\n"
    )

#Q.4
sentence = input("Enter a sentence: ")

words = sentence.split()

short_count = 0
medium_count = 0
long_count = 0

for word in words:
    length = len(word)

    if length <= 3:
        category = "Short"
        short_count += 1
    elif 4 <= length <= 6:
        category = "Medium"
        medium_count += 1
    else:
        category = "Long"
        long_count += 1

    print(f"Word: '{word}' | Length: {length} | Category: {category}")

print("\n--- Summary ---")
print(f"Short words (<= 3): {short_count}")
print(f"Medium words (4-6): {medium_count}")
print(f"Long words (> 6): {long_count}")

#Q.5
for i in range(1, 6):
    num_input = input(f"Enter number {i}: ")

    # Convert to string and remove negative sign if present
    num_str = str(num_input).lstrip("-")

    even_count = 0
    odd_count = 0

    # Examine every character/digit using a loop
    for char in num_str:
        if char.isdigit():
            digit = int(char)
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Compare digit counts and determine output
    print(f"\nNumber: {num_input}")
    print(f"Even digits: {even_count}, Odd digits: {odd_count}")

    if even_count > odd_count:
        print("Result: Even occurs more")
    elif odd_count > even_count:
        print("Result: Odd occurs more")
    else:
        print("Result: Equal")
    print("-" * 30)

#Q.6

text = input("Enter a string: ")

processed_chars = ""

print("\n--- Repeated Character Report ---")

for char in text:
    
    if char in processed_chars:
        continue

    occurrence_count = 0
    for c in text:
        if c == char:
            occurrence_count += 1

    processed_chars += char


    if occurrence_count > 1:
        if occurrence_count == 2:
            classification = "Duplicate"
        elif 3 <= occurrence_count <= 4:
            classification = "Repeated"
        else:  # More than 4
            classification = "Highly Repeated"

        print(
            f"Character: '{char}' | Occurrences: {occurrence_count} | Classification: {classification}"
        )

#Q.7

text = input("Enter a string: ")

# Keep track of characters we've already processed to avoid printing duplicates
processed = ""

for i in range(len(text)):
    char = text[i]

    # Skip if character has already been processed
    already_seen = False
    for p in processed:
        if p == char:
            already_seen = True
            break

    if already_seen:
        continue

    # Count occurrences of char manually without using .count()
    occurrences = 0
    for j in range(len(text)):
        if text[j] == char:
            occurrences += 1

    # Mark character as processed
    processed += char

    # Filter and classify characters appearing more than once
    if occurrences > 1:
        if occurrences == 2:
            classification = "Duplicate"
        elif 3 <= occurrences <= 4:
            classification = "Repeated"
        else:  # occurrences > 4
            classification = "Highly Repeated"

        print(f"'{char}': {occurrences} occurrences → {classification}")

#Q.8
prices = []

# Take prices of 8 products from the user
for i in range(1, 9):
    price = float(input(f"Enter price for product {i}: "))
    prices.append(price)

# Counters for each category
budget_count = 0
regular_count = 0
premium_count = 0
luxury_count = 0

total_amount = 0

# Process and classify each price
for price in prices:
    total_amount += price

    if price < 500:
        category = "Budget"
        budget_count += 1
    elif 500 <= price <= 1999:
        category = "Regular"
        regular_count += 1
    elif 2000 <= price <= 4999:
        category = "Premium"
        premium_count += 1
    else:  # price >= 5000
        category = "Luxury"
        luxury_count += 1

    print(f"Price: ₹{price:.2f} → {category}")

# Calculate average price
average_price = total_amount / len(prices)

# Print Summary Report
print("\n--- Summary Report ---")
print(f"Total Amount: ₹{total_amount:.2f}")
print(f"Average Product Price: ₹{average_price:.2f}")
print("Product Counts by Category:")
print(f"  - Budget (< 500): {budget_count}")
print(f"  - Regular (500–1999): {regular_count}")
print(f"  - Premium (2000–4999): {premium_count}")
print(f"  - Luxury (5000+): {luxury_count}")

text = input("Enter a string: ")

# Category counters
vowels_count = 0
consonants_count = 0
digits_count = 0
special_count = 0

vowels = "aeiouAEIOU"

print("\n--- Character Analysis ---")
for index in range(len(text)):
    char = text[index]
    position = index + 1  # 1-based index position

    # Determine index position parity (even or odd)
    pos_parity = "Even" if position % 2 == 0 else "Odd"

    # Classify character type
    if char.isalpha():
        if char in vowels:
            category = "Vowel"
            vowels_count += 1
        else:
            category = "Consonant"
            consonants_count += 1
    elif char.isdigit():
        category = "Digit"
        digits_count += 1
    else:
        category = "Special Character"
        special_count += 1

    print(
        f"Pos {position} ({pos_parity}): '{char}' → {category}"
    )

# Print Summary Report
print("\n--- Summary Report ---")
print(f"Total Vowels: {vowels_count}")
print(f"Total Consonants: {consonants_count}")
print(f"Total Digits: {digits_count}")
print(f"Total Special Characters: {special_count}")

#Q.9
text = input("Enter a string: ")

# Category counters
vowels_count = 0
consonants_count = 0
digits_count = 0
special_count = 0

vowels = "aeiouAEIOU"

print("\n--- Character Analysis ---")
for index in range(len(text)):
    char = text[index]
    position = index + 1  # 1-based index position

    # Determine index position parity (even or odd)
    pos_parity = "Even" if position % 2 == 0 else "Odd"

    # Classify character type
    if char.isalpha():
        if char in vowels:
            category = "Vowel"
            vowels_count += 1
        else:
            category = "Consonant"
            consonants_count += 1
    elif char.isdigit():
        category = "Digit"
        digits_count += 1
    else:
        category = "Special Character"
        special_count += 1

    print(
        f"Pos {position} ({pos_parity}): '{char}' → {category}"
    )

# Print Summary Report
print("\n--- Summary Report ---")
print(f"Total Vowels: {vowels_count}")
print(f"Total Consonants: {consonants_count}")
print(f"Total Digits: {digits_count}")
print(f"Total Special Characters: {special_count}")
 

