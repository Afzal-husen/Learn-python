import random

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

options = [rock, paper, scissors]

my_index = int(input('what is your choice? type 0 for rock, 1 for paper and 2 for scissors \n'))
if my_index >= len(options):
    print("Invalid choice")
else:
    my_choice = options[my_index]
    print(f"Your choice: {my_choice}")
    random_index = random.randint(0, 2)
    computer_choice = options[random_index]
    print(f"Computer\'s choice: {computer_choice}")

    if my_index > len(options) - 1:
        print("Invalid choice")
    else:
        if my_index == 0 and random_index == 2:
            print("You Won!")
        elif random_index == 0 and my_index == 2:
            print("You lost!")
        elif my_index > random_index:
            print("You Won!")
        elif my_index < random_index:
            print("You lost")
        elif my_index == random_index:
            print("It\'s a draw!")
        else:
            print("You lost!")

