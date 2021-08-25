import random

# input feild for your choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2) # random choice for the computer

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# game images in list 
game_images = [rock, paper, scissors]

# the game logic 
if user_choice == 0 and computer_choice == 1:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You lose!")
elif user_choice == 1 and computer_choice == 0:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("You win!")
elif user_choice == computer_choice:
    print(game_images[user_choice])
    print("Computer chose:\n", game_images[computer_choice])
    print("It's a draw")
elif user_choice > 2 or user_choice < 0:
    print("you can only use these three digits 0 as rock, 1 as paper and 2 as scissors")

# The same logic or the game just shorter
# if user_choice > 2 or user_choice < 0:
#     print("you can only use these three digits 0, 1 and 2")
# elif user_choice < computer_choice:
#     print(game_images[user_choice])
#     print("Computer chose:\n", game_images[computer_choice])
#     print("You lose!")
# elif user_choice == 2 and computer_choice == 0:
#     print(game_images[user_choice])
#     print("Computer chose:\n", game_images[computer_choice])
#     print("You lose!")
# elif user_choice > computer_choice:
#     print(game_images[user_choice])
#     print("Computer chose:\n", game_images[computer_choice])
#     print("You win!")
# elif user_choice == 0 and computer_choice == 2:
#     print(game_images[user_choice])
#     print("Computer chose:\n", game_images[computer_choice])
#     print("You win!")
# elif user_choice == computer_choice:
#     print(game_images[user_choice])
#     print("Computer chose:\n", game_images[computer_choice])
#     print("It's a draw")
