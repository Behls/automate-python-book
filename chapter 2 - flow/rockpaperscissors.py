import sys
import random

w = 0
l = 0
t = 0

#  game logic loop
while True:

    print('Rock, paper Scissors \n'+str(w)+' Wins, ' +str(l)+' Losses, ' +str(t)+' Ties')

    #  user input loop
    while True: 
         print('enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
         playerMove = input()

         if playerMove == 'q':
             sys.exit('you have exited the game')
         
         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
             break
        
         print('choose either, r, s, q, p')
    
    #  creating player moves

    if playerMove == 'r':
        print('Rock Versus...')
    elif playerMove == 'p':
        print('Paper Versus...')
    elif playerMove == 's':
        print('Scissors Versus...')

    # creating random computer moves
   
    randomNumber = random.randint(1,3)
    print(randomNumber)

    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')

    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')

    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    # dealing with ties

    if playerMove == 'r' and computerMove == 'r':
        print('you have tied')
        t += 1

    elif playerMove == 's' and computerMove == 's':
        print('you have tied')
        t += 1

    elif playerMove == 'p' and computerMove == 'p':
        print('you have tied')
        t += 1
    
    #  dealing with the losses 

    elif playerMove == 'p' and computerMove == 's':
        print('you have lossed')
        l += 1
    
    elif playerMove == 'r' and computerMove == 'p':
        print('you have lossed')
        l += 1
    
    elif playerMove == 's' and computerMove == 'r':
        print('you have lossed')
        l += 1

    # dealing with the winnings

    elif playerMove == 's' and computerMove == 'p':
        print('you have won')
        w += 1
    
    elif playerMove == 's' and computerMove == 'p':
        print('you have won')
        w += 1
    
    elif playerMove == 'p' and computerMove == 'r':
        print('you have won')
        w += 1

    print ('do you wish to continue? y/n')
    choices = str(input())

    if choices == 'y':
        continue
    elif choices =='n':
        break

print('you have quit the game')

