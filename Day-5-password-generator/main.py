# MINOR
# to find average
# heights = input("please enter the heights of students \n").split()
# sum = 0
# total_count = 0
# for height in heights:
#     height = int(height)
#     sum += height
#     total_count += 1
# average = round(sum/total_count)
# print(average)

# to find high score
# highest_score = 0
# scores = input("Please enter the scores \n").split()
# for score in scores:
#     score = int(score)
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is: {highest_score}")

# SUM OF ALL EVEN NUMBERS BETWEEN 1 and 100
# even_numbers = range(0, 101, 2)
# sum = 0
# for number in even_numbers:
#     sum += number
# print(sum)

# FIZZBUZZ CHALLENGE
# if number is divisible by 3 then fizz
# if number is divisible by 5 then buzz
# if number is divisible by both 3 and 5 then fizzBuzz

# chosen_numbers = range(1, 101)
# for number in chosen_numbers:
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzBuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)

# MAJOR
# PASSWORD_GENERATOR
# prompt the user to enter number of char letters
# prompt the user to enter number of symbols
# prompt the user to enter number of numbers

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters = int(input("How many letters would you like in your password \n"))
number_of_numbers = int(input("How many numbers would you like in your password \n"))
number_of_symbols = int(input("How many symbols would you like in your password \n"))

# ORDINARY PASSWORD
password = ""
for char in range(1, number_of_letters + 1):
    password += random.choice(letters)

for char in range(1, number_of_symbols + 1):
    password += random.choice(symbols)

for char in range(1, number_of_numbers + 1):
    password += random.choice(numbers)

print(password)

# HIGHER LEVEL PASSWORD
password_list = [*password]
random.shuffle(password_list)

new_password = ""
for char in password_list:
    new_password += char

print(new_password)







