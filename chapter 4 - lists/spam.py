import sys

spam = ['cat', 'dog','mouse']
# indexes can only be int values nothing else.
print(spam[1])
print(f'the {spam[0]} ate the {spam[2]}')

# this is what i would do 
# def spam(index):
#     try:
#         spam = ['cat', 'dog','mouse']
#         return print(spam[index])

#     except IndexError:
#         return sys.exit('index out of bounds')

# #
# numb = int(input('enter a number'))
# spam(numb)


spam1 = [['cat', 'dog'],['baby', 'mouse']]
# first index selects the list within the list, second index selects the value stored in that last at that index
# should print dog
print(spam1[0][1]) 
# negative indexs work from the last item on the last backwards, -1 is the last, -2 is second to last etc etc
# should print mouse
print(spam1[-1][-1])
# slicing includes 2 ints and a colon. Create a slice at a starting index place and and ending index place. 
# only includes up to the last index value.
# should print first 2 items
print(spam[0:2])

# concatination of lists 
spam2 = spam + [1,2,3]
print(spam2)

# repeating list
spam2 *= 3
print(spam2)

# deleting values from lists
spam3 = [1,2,3,4,5,6]
del spam3[2]
print(spam3)

# working with lists - adding to the list
# cats=[]
# while True: 
#     print('enter in a cat name: ' +str(len(cats)+1)+ ' or enter to stop')
#     name = input()
#     if name == '':
#         break
#     else:
#         cats.append(name)
#     print('cats names are:')
#     for name in cats:
#         print(f'{name}')

# for loops and lists
for x in range(3):
    print(x)

supplies=['pen','rubber','paper','binder']
for i in range(len(supplies)):
    print('index: '+str(i)+ ' is ' +supplies[i])
    
# in and not in operators 

'howdy' in ['hello', 'hi','howdy', 'heyas']
# true
spam3 = ['hello', 'hi','howdy', 'heyas']
'cat' in spam3
# false
'howdy' not in spam3
# true
'cat' not in spam3
# false


# enumerating and lists - instead of using range(len(list)) with a for loop to loop through the values
spam4 = ['pens', 'staplers', 'flamethrowers', 'binders']
# use two iterating values - enumrate gives you the index value and the item in the list
for index,item in enumerate(spam4):
    print(f'the index is {index} and the item is: {item}')

