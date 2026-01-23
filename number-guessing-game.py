"""
Filename: <>
Author: <Fontaine, Michael>
Created: <1/23/2026>
Instructor: Holtslander
"""
from random import randint

# num = randint(1, 100)
num = 4

guess = int(input("Guess a number between 1 and 100\n"))

if num== guess:
    print("Correct!")
elif num < guess:
    print("Too low!")
elif num > guess:
    print ("Too high!")


