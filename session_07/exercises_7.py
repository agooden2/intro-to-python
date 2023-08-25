# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
# def print_name():
#   print("Adina")

# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
# def print_name(name):
#   print("Hello, " + name)

# print_name("Adina")

# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
# list = ["Alice", "Bob", "Charlie"]
# for name in list:
#   print_name(name)


# 4. Write a function that prints the area of two passed in parameters.
# def calculate_area(width, height):
#   area = width * height
#   print(area)


# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
# def print_list(list):
#   for item in list:
#     print(item)


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

# def school(age):
#   if age < 11:
#     if age==0: 
#       print("You're not born yet!")
#     else:
#       print("You're too young to go to this school")
#   elif age >11 and age<16:
#     print("You can can come to this school")
#   else:
#     print("You're too old for school")


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
# def is_odd(int):
#   if int % 2 ==0:
#     return False
#   else:
#     return True


# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
# def flip_word(word):
#   print(word[::-1])

# flip_word("hello")

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
# def stars(num):
#   star = ""
#   for y in range(0, num):
#     star = star + "*"
#   print(star)
#   if num > 1:
#     stars(num-1)

# stars(4)


# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
# def padlock(guess):

#     pin = 3394
#     if pin == guess:
#         print("Unlock")
#     else:
#         print("Locked")


# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
# def multiples_of_3_and_5(limit):

#     total = 0
    
#     for i in range (0, limit+1):
#         if limit < 0:
#             print("Limit must be greater than 0")
#         if i % 3 == 0:
#             total += i
#         elif i % 5 == 0:
#             total += i
    
#     print(total)



# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.
# def is_prime(num):
#   for i in range(2, num):
#       if(num % i == 0):
#           count = count + 1
#           break

#   if (count == 0 and num != 1):
#       print(str(num) + " is a prime Number")
#       return True
#   else:
#       print(str(num) +" is not a prime Number")
#       return False



# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
# def is_pallindrome(string):
#   backwards = string[::1]
#   if backwards == string:
#     return True
#   else:
#     return False

# print(is_pallindrome("Hannah"))


# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
# def is_pallindrome_sentence(string):
#   backwards = string[::1].lowercase()
#   if backwards == string.lowercase():
#     return True
#   else:
#     return False
