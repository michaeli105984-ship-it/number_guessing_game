"""
Filename: <>
Author: <Fontaine, Michael>
Created: <1/23/2026>
Instructor: Holtslander
"""
from random import randint
playing = "y"
while playing == "y":
    num = randint(1, 100)
    guess = 0
    while guess != num:
        print("Guess a number between 1 and 100.")
        guess = input()
        guess = int(guess)
        if guess < num:
            print("Too low! Try again.")
        elif guess > num:
            print("Too high! Try again.")
        else:
            print(f"You got it! The number was {num}.")
    playing = input("Play again? (y/N)\n").lower()
print("Thanks for playing!")
# number should be random and code needs to repeat




