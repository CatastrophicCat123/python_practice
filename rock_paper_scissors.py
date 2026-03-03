import random

temp = {}

user_points = 0
bot_points = 0

for i in range(0, 3):
    bot_choice = random.randint(0, 2)
    user_choice = int(input("[0]: Rock\n[1]: Paper\n[2]: Scissors\n->"))
    print(bot_choice)
    if bot_choice == user_choice:
        print("\nDraw!\n\n")
    elif user_choice == 2 and bot_choice == 0:
        print("\nYou Lost This Round!\n\n")
        bot_points += 1
    elif bot_choice == 2 and user_choice == 0:
        print("\nYou Won this Round!\n\n")
        user_points += 1
    elif bot_choice < user_choice:
        print("\nYou Won This Round!\n\n")
        user_points += 1
    else:
        print("\nYou Lost this Round!\n\n")
        bot_points += 1

print("Player Wins: ", user_points)
print("Bot Wins: ", bot_points)