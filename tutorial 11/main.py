# Project 2 - Guess the number
import random
low=0
high=100
print(f"This game is guess the number.In this game you have to guess a number chosen by the computer.That number must be between {low} to {high}")
while True:
    random_num=random.randint(low,high)
    done=False
    attempts=0
    while not done:
        guessed_num=int(input("Enter the number:"))
        if guessed_num==random_num:
            print("You are right.Attempts taken - "+str(attempts))
        elif guessed_num<random_num:
            print("It's low")
            attempts+=1
        elif guessed_num>random_num:
            print("It's high")
            attempts+=1