# Session 4 Exercisess

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
# items = ['Apples', 'Cherries', 'Pears', 'Pineapple', 'Peaches', 'Mango']
# print(items)

# 2. Add "Grapes" to the list and print the list.
# items.append("Grapes")
# print(items)

# 3. Change "Pears" to "Strawberries" and print the list.
# items[2]="Strawberries"
# print(items)

# 4. Remove "Apples" from the list and print the list.
# del items[0]
# print(items)

# 5. Print out the current length of the list.
# print(len(items))

# 6. Order the list alphabetically.
# items.sort()

# 7. Print out the list again.
# print(items)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
# for fruit in items:
#   print(fruit)

# 2. Print the numbers 1 to 100 (including the number 100).
# for num in range (0,101):
#   print(num)

# 3. Print all odd numbers from 1 to 100.
# for odd_num in range(1,101, 2):
#   print(odd_num)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
# for olympic_year in range(1916, 2024, 4):
#   print(olympic_year)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
# random_numbers=[3,44,53,63,3,75,24,86,242,763]
# even_numbers=0
# odd_numbers=0

# for num in random_numbers:
#   if num%2==0:
#     even_numbers+=1
#   else:
#     odd_numbers+=1

# print("Even numbers: " + str(even_numbers))
# print("Odd numbers: " + str(odd_numbers))

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
# names = ["Sophia", "Darren", "Jim", "Eliza", "Yeli"]
# for name in names:
#   print("Hello " + name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
# string="supercalifragilisticexpialidocious"
# for i in range (0, len(string)):
#   print(string[i])

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#   numbers.append(num**2)
# print(names)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
# names = ["Sophia", "Darren", "Jim", "Eliza", "Yeli"]
# new_list =[]
# for name in names:
#   new_list.append("Dr. "+name)
# print(new_list)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz".
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

# for i in range(1,101):
#   if i%3==0:
#     if i%5==0:
#       print("FizzBuzz")
#     else:
#       print("Fizz")
#   elif i%5==0:
#     print("Buzz")
#   else:
#     print(i)
