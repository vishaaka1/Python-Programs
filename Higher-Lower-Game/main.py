import random

game_dict = {
100: 'neymar, is a footballer, from brazil',
200: 'shakira, is a musician, from colombia',
1000: 'Ronaldo, is a footballer, from portugese',
2000: 'Messi, is a footballer, from aregentina',
300: 'Rajini, is a actor, from tamilnadu',
500: 'Dhoni, is a cricketer, from india',
800: 'Mike tyson, is a boxer, from USA',
1500: 'Putin , is the president, for Russia',
1200: 'Drake, is a singer, from Canada',
}

def game():
  game_dict1 = {
  100: 'neymar, is a footballer, from brazil',
  200: 'shakira, is a musician, from colombia',
  1000: 'Ronaldo, is a footballer, from portugese',
  2000: 'Messi, is a footballer, from aregentina',
  300: 'Rajini, is a actor, from tamilnadu',
  500: 'Dhoni, is a cricketer, from india',
  800: 'Mike tyson, is a boxer, from USA',
  1500: 'Putin , is the president, for Russia',
  1200: 'Drake, is a singer, from Canada',
  }
  points = 0
  name_c = 0
  a = True
  b = True
  c = True
  d = True
  while c is True:
    if a == True:
      name_a = random.choice(list(game_dict))
      game_dict.pop(name_a)
    if b == True:
      name_b = random.choice(list(game_dict))
      game_dict.pop(name_b)
    if d == True:
      print(f"Compare A: {game_dict1[name_a]}")
      print(f"Against B: {game_dict1[name_b]}")
    else:
      print(f"Compare A: {game_dict1[name_b]}")
      print(f"Against B: {game_dict1[name_a]}")
      name_c = name_b
      name_b = name_a
      name_a = name_c

    user_choice = input("Who has more followers--> Type 'A' or 'B': ").lower()
    if user_choice == 'a':
      if name_a > name_b:
        a = False
        b = True
        d = True
        points += 1
      if points == (len(game_dict1))-1:
        print(f"Your Points = {points} You WIN!!!")
        return
      elif name_a < name_b:     
        print(f"Your Points = {points} Game Over!!!")
        return
    elif user_choice == 'b':
      if name_b > name_a:
        d = False
        a = True
        b = False
        points += 1
        if points == (len(game_dict1))-1:
          print(f"Your Points = {points} You WIN!!!")
          return
        
      elif name_b < name_a:
        print(f"Your Points = {points} Game Over!!!")
        return
    else:
      print("invalid entry")
game()