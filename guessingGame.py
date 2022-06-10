import random
number = random.randint(1, 9)
chances = 0
while (chances < 5):
    guess = int(input("enter the number between 1-9: "))
    if (guess > number):
        print("try guessing a smaller number")
    elif (guess == number):
        print("Congratulation! YOU WON")
    else :
        print("try guessing a bigger number")
    chances = chances + 1
if not (chances < 5):
    print("You Lost! The number is ",number)
