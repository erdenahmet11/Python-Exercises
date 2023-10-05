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

import random
rounds = int(input("How many rounds do you want to play?"))
images = [rock, paper, scissors]
user_score = 0
computer_score = 0
for i in range(1, rounds + 1):
    user_choice = int(input("What do you choose? Please type 0 for Rock, 1 for Paper, 2 for Scissors."))
    if user_choice < 0 or user_choice > 2:
        print("The number you entered is invalid. Please write one of the numbers mentioned.")
    else:
        print(f"Your choice:\n{images[user_choice]}")
        computer_choice = random.randint(0, 2)
        print(f"Computer choice:\n{images[computer_choice]}")
        if user_choice == 0 and computer_choice == 2:
            print(f"You won the {i}. round!")
            user_score += 1
        elif user_choice == 1 and computer_choice == 0:
            print(f"You won the {i}. round!")
            user_score += 1
        elif user_choice == 2 and computer_choice == 1:
            print(f"You won the {i}. round!")
            user_score += 1
        elif computer_choice == 0 and user_choice == 2:
            print(f"Computer won the {i}. round!")
            computer_score += 1
        elif computer_choice == 1 and user_choice == 0:
            print(f"Computer won the {i}. round!")
            computer_score += 1
        elif computer_choice == 2 and user_choice == 1:
            print(f"Computer won the {i}. round!")
            computer_score += 1
        else:
            print(f"{i}. round draw!!")

        print(f"{i}. Round --> Your score: {user_score} Computer score: {computer_score}")

if user_score > computer_score:
    print("CONGRATULATİONS YOU WON THE GAME!")
elif computer_score > user_score:
    print("YOU LOST THE GAME!")
else:
    print("YOU ARE İN A DRAW!")