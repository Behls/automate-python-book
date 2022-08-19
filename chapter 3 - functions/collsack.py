import sys

# recursive function, calls itself if number is higher than 1.

def collatz(number):
    if number == 1:
        print("sequence finished")
    elif number % 2 == 0:
        print(int(number / 2 ))
        collatz(number / 2)
    else: 
        print(int(number * 3 + 1))
        collatz(number * 3 + 1) 
try:
    collatz(int(input("enter an integer")))
except ValueError:
    print("you need to enter an integer")

