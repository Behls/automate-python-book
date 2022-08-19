import random

def getAnswer(answer): # <--- define a function with a paramater
    if answer == 1:
        return 'it is certain'
    elif answer == 2:
        return 'it is decidely so'
    elif answer == 3:
        return 'yes'
    elif answer == 4:
        return 'reply hazy try again'
    elif answer == 5:
        return 'ask again later'
    elif answer == 6:
        return 'concentrate and ask again'
    elif answer == 7:
        return 'my reply is no'
    elif answer == 8:
        return 'outlook not so good'
    elif answer == 9:
        return 'very doubtful' # <--- return a value based 

r = random.randint(1,9)
fortune = getAnswer(r) # <--- calling that function with arguments
print(fortune) 

# or can do the same in one line as opposed to 3 lines
print(getAnswer(random.randint(1,9)))