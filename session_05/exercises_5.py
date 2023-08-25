# Session 5 Exercises
import random 

## Section A
# 1. Print 10 random numbers.

# for number in range(10):
#     print(random.randint(1, 10))


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
# number = 0
# while number !=7:
#   number = int(input("Enter a number: "))

# print("Wow lucky number 7")



# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
# height = int(input("Enter height in cm: "))
# width = int(input("Enter width in cm: "))
# print(str(height) + "cm x " + str(width) + "cm = " + str(height*width) + "cm2")



# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
# attempts = 0
# while attempts <3:
#   password = input("Enter password: ")
#   if password == "qwert123":
#     print("You have successfully logged in")
#     break
#   else:
#     print("Password failure")
#     attempts+=1
# if attempts==3:
#   print("System locked!")


# 5. Add up all the numbers from 1 to 500 and print the answer.
# total=0
# for num in range (1,501):
#   total +=num
# print(total)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
# list=[]
# print("Please enter 10 numbers, one being 99")
# for i in range (1,11):
#   num = int(input("Enter number " + str(i) + ": "))
#   list.append(num)

# found = False
# index = 0
# while found!= True:
#   if list[index] == 99:
#     found=True
#     print(index)
#   else:
#     index+=1


# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
# for i in range (1,13):
#   print(str(i) + " x 18 = " + str(i*18))


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
# pointer = 1
# while pointer <=100:
#   print(pointer)
#   pointer+=1



# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

# lesson = ""

# print("REPORT CARD:")

# while lesson != "":
#     lesson = input("Input your lesson:\n")
#     mark = int(input("Input your mark:\n"))
#     if mark > 80:
#         print(lesson + " - A grade")
#     elif mark <= 80 and mark > 60:
#         print(lesson + " - B grade")
#     elif mark <= 60 and mark > 50:
#         print(lesson + " - C grade")
#     elif mark <= 50 and mark> 45:
#         print(lesson + " - D grade")
#     elif mark <= 45 and mark > 25:
#         print(lesson + " - E grade")
#     elif mark < 25:
#         print(lesson + " - F grade")
#     else:
#         print("Go to see your teacher")


# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# names = []
# another = "Y"
# while another =="Y":
#   name = input("Enter name: ")
#   names.append(name)
#   another = input ("Add another name to the draw? (Y/N) ")
# index = random.randint(0, len(names)-1)
# print("The winner is... " + names[index])



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

# print("------ WELCOME TO ROCK, PAPER, SCISSORS! ------")
# print("The rules of the game:")
# print("Select either:")
# print("R for Rock, \nP for Paper or \nS for Scissors")
# print("\nLET'S PLAY")

# player_wins = 0
# computer_wins = 0
# options=["R", "P", "S"]
# for game in range (1,4):
#   print("\n --- GAME "+ str(game) + " ---")
#   selection = input("Enter R, P or S: ")
#   computer_selection = random.choice(options)
#   if computer_selection== "R" & selection=="S":
#     computer_wins++1
#   elif computer_selection== "R" & selection=="S":
#     computer_wins++1
#   # print(computer_selection)
  
  