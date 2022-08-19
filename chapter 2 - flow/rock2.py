import sys, random

w = 0
l = 0
t = 0

while True:

    print('Rock, paper Scissors \n'+str(w)+' Wins, ' +str(l)+' Losses, ' +str(t)+' Ties')
    
    while True: 
         print('enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
         playerMove = input()

         if playerMove == 'q':
             sys.exit('you have exited the game')
         
         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
             break
        
         print('choose either, r, s, q, p')
    
    # better what of choosing a random computer action rather than coding multiple if statements for a computer move.
    # worth reading the documenttaiton on built in functions

    choiceList = ["r", "s", "p"]
    computerMove = random.choice(choiceList)
    print(computerMove)

    #  if you want to print a list of random choices, you can use the choices function.
    #  pass in the list, the weight(how probably it is is to repeat?, size of list. (k=10))
    print(random.choices(choiceList, weights = [10,1,1], k=10))
 
    #  creating player moves

    if playerMove == 'r':
        print('Rock Versus...')
    elif playerMove == 'p':
        print('Paper Versus...')
    elif playerMove == 's':
        print('Scissors Versus...')

    # creating random computer moves
   

    if computerMove == 'r':
        print('Rock')

    elif computerMove == 'p':
        print('Paper')

    elif computerMove == 's':
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

print(' you have left the game ')
