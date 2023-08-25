import random

def roll_die():
  outcome = random.randint(1,6)
  return outcome

print("--- WELCOME TO 21!---")
print("The aim of the game is to roll the die to get a score of 21")

total=0

while total<=21:
  print("Current total: " + str(total))
  if total==21:
    print("You won, you got 21!")
    break
  else:
    enter = input("Press <ENTER> to roll die...\n")
    number = roll_die()
    total += number
    print("You rolled a " + str(number))
if total > 21:
  print("You lose! You ended up with " + str(total) + " :(")
  