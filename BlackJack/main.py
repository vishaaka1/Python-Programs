
import random
dealer_score = []
user_score = []

def hit():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return(random.choice(cards))

def computer_jack(human_final, computer_final):
  if sum(computer_final)<17:
    computer_final.append(hit())
    computer_jack(human_final=human_final, computer_final=computer_final)
  elif sum(computer_final)>21:
    print(f"You Win {sum(human_final)}!!! Dealer Lost {sum(computer_final)}")
  else:
    compare(human_compare=human_final,computer_compare = computer_final)

def compare(human_compare,computer_compare):
  if sum(human_compare) > sum(computer_compare):
    print(f"You Won!!!!computer_score is {sum(computer_compare)} and human_score is {sum(human_compare)}")
  elif sum(human_compare) < sum(computer_compare):
    print(f"You Lose!!!!computer_score is {sum(computer_compare)} and human_score is {sum(human_compare)}")
  else:
    print(f"It's a Draw!!!!computer_score is {sum(computer_compare)} and human_score is {sum(human_compare)}")

def blackjack(human,computer):
  print(f"computer_score is {sum(computer)} and human_score is {sum(human)}")
  if sum(human) == 21:
    print("BlackJack!!! You Win!!!")
  elif sum(computer) == 21:
    print("You Lose!!! Dealer Won!!!")
  elif sum(human) > 21:
    if 11 in human:
      human.remove(11)
      human.append(1)
      if sum(human) > 21:
        print("Bust!! You Lose!!")
      else:
        decision = input("Enter y to 'Hit' or n to 'stand'")
        if decision == 'y':
          human.append(hit())
          blackjack(human=human,computer=computer)
          #print(f"human: {sum(human)} and computer: {sum(computer)}")
        else:
          computer_jack(human_final=human,computer_final=computer)
          #print(f"human: {sum(human)} and computer: {sum(computer)}")
    else:
      print("Bust!! You Lose!!")
  else:
    decision = input("Enter y to 'Hit' or n to 'stand'")
    if decision == 'y':
      human.append(hit())
      blackjack(human=human,computer=computer)
      #print(f"human: {sum(human)} and computer: {sum(computer)}")
    else:
      computer_jack(human_final=human,computer_final=computer)


for i in range(0,2):
  user_score.append(hit())
  dealer_score.append(hit())
blackjack(human=user_score,computer=dealer_score)