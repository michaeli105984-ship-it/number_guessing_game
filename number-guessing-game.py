"""
Filename: <>
Author: <Fontaine, Michael>
Created: <1/21/2026>
Instructor: Holtslander
"""
from random import randint

# num = randint(1, 100)
num = 10

guess = int(input("Guess a number between 1 and 100\n"))

if num== guess:
    print("Correct!")
elif num < guess:
    print("too low!")
elif num > guess:
    print ("Tpp high!")
