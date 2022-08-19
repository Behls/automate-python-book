import random

rando = random.randint(1,20)
guess = 0
count = 0

print('im thinking of a number take a guess')
while True:
    
    print('take a guess')
    guess = int(input())
    if guess > rando:
        print('your guess was too high')
        count += 1
    elif guess < rando:
        print('your guess was too low')
        count +=1
    elif guess == rando:
        count += 1
        print('you guessed right! you guessed my number in '+str(count)+' guesses')
        break

print('game over')