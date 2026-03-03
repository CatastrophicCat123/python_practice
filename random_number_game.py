import random

randomNumber = random.randint(1, 10)
userInput = None

while userInput != randomNumber:
    userInput = int(input("Im thinking of a number 1 - 10, what is it? "))
    if userInput > randomNumber:
        print("Too High")
    elif userInput < randomNumber:
        print("Too Low")

print("CONGRATS!!!!!")