import random

def roll_dice():
    print("Welcome to the Dice Rolling Game!")
    print("Press 'Enter' to roll the dice. Press 'Q' to quit.")

    while True:
        user_input = input()
        if user_input.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            break

        dice_value = random.randint(1, 6)
        print(f"You rolled a {dice_value}!")

roll_dice()
