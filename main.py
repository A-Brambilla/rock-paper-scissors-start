rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

choices = [rock, paper, scissors]
print(choices[player_choice])

cpu_choice = random.randint(0,2)
print(choices[cpu_choice])

if player_choice == 0 and cpu_choice == 1:
  print("You lose!")
elif player_choice == 0 and cpu_choice == 2:
  print("You win!")
elif player_choice == 0 and cpu_choice == 0:
  print("You draw!")
elif player_choice == 1 and cpu_choice == 0:
  print("You win!")
elif player_choice == 1 and cpu_choice == 1:
  print("You draw!")
elif player_choice == 1 and cpu_choice == 2:
  print("You lose!")
elif player_choice == 2 and cpu_choice == 0:
  print("You lose!")
elif player_choice == 2 and cpu_choice == 1:
  print("You win!")
elif player_choice == 2 and cpu_choice == 2:
  print("You draw!")
else:
  print("invalid choice I guess")