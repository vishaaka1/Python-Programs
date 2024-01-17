import random
from art import art1
computer_number = random.randint(0,100)
print(computer_number)

def game(number):
  global computer_number
  print(f"You have {number} Chances to guess the number")
  for _ in range(number):
    user_number = int(input("Guess the number: "))
    if user_number > computer_number:
      print("Your Number is Too High")
    elif user_number < computer_number:
      print("Your number is too Low")
    elif user_number == computer_number:
      print(f"{user_number} is the correct answer....You Win!!!  :)")
      return
  print("You have no more chances YOU LOSE!!! :(")
    
    

print(art1)
print("Welcome to Number Guessing Game!!")
print("I'm Thinking a Number between 1 to 100")
difficulty = input("Choose your difficulty level 'Easy' 'Medium' 'Hard': ").lower()
if difficulty == "easy":
  print("Easy Mode Selected")
  game(number = 15)
elif difficulty == "medium":
  print("Medium Mode Selected")
  game(number = 10)
elif difficulty == "hard":
  print("Hard Mode Selected")
  game(number = 5)