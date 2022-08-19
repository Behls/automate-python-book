
myPets=['zophie', 'pooka','fat-tail']
petName = input('enter a pets name')
if petName not in myPets:
    print('no pet here with name: ' +petName)
else:
    print(petName+ ' is my pet')


# tuple unpacking - assigning multiple variables to values in a list
# this is a long winded approach to assigning variables 
cat=['fat', 'gray', 'loud']
size=cat[0]
color=cat[1]
disposition=cat[2]

# you can condense it into one line as follows:
cat=['fat', 'gray', 'loud']
size,color,disposition=cat
# only works if the amount of values = length of elements otherwise a value error is thrown

# if wanted to use try and catch then you could do
try: 
    cat=['fat', 'gray', 'loud']
    size,color,disposition=cat
    print('variables are assigned')
except ValueError:
    
    print('error')


# using the random module 
# choice - will randomly choose a value in a list
# it will shuffle the whole list rearranging the order of the list randomly.
import random
random.choice(myPets)
random.shuffle(myPets)

# augmented operators + - = / *
# you usually use operators to add values to variables
spamNo = 40 
spamNo = spamNo + 1
# could be written as 
spamNo +=1
#could also apply to lists or other stuff
alist =  ['fat', 'gray', 'loud']
# adding a value to the list
alist += ['hello'] 
# repeating the list 
alist *=2
# many more can be applied
print(f'{alist}')





