# 1. what are the two values pf the boolean Data Type? How do you write them.
# True and False

print(True)
print(False)

# 2. what are the thre boolean operators? 
# And, Or, Not
print('\n')
print(''' ----- boolean operators -----
 or   |  one of conditions is true
 and  |  both conditions are true
 not  |  flips to opposite boolean value
''')

# 3 write out the truth tables of each boolean operator. 

# not
print('\n')
print('flips the boolean value ie True => False')
print('------ not truth table ------')
print('not true       | ' +str(not True))
print('not false      | ' +str(not False))
print('not not true   | ' +str(not not True))
print('not not false  | ' +str(not not False))

# and
print('\n')
print('both values must be / return true')
print('------ and truth table ------')
print('true and true        | ' +str(True and True))
print('false and false      | ' +str(False and False))
print('true and false       | ' +str(True and False))
print('false and true       | ' +str(False and True))

print('\n')
print('one of the values must be true')
print('------ or truth table ------')
print('true or true        | ' +str(True or True))
print('false or false      | ' +str(False or False))
print('true or false       | ' +str(True or False))
print('false or true       | ' +str(False or True))

print('\n')
print('operators can also be combined!')
print('------ example ------')
print('not(true and true)    | ' +str(True and True))


# 4. what dp the following expressions evaluate to? 

print((5>4) and (3==5)) 
print('answer is false')

print(not (5>4))
print('answer is false')

print((5>4) or (3==5))
print('answer is true')

print(not ((5>4) or (3 ==5)))
print('answer is false')

print((True and True) and (True == False))
print('answer is false')

print((not False) or (not True))
print('answer is True\n')



#  5. what are the 5 comparision operators? 
print(''' ----- comparison operators -----
 ==   |  equal to
 !=   |  not equal to
 >=   |  greater than or equal to 
 <=   |  less than or equal to 
 >    |  greater than
 <    |  less than
''')

# 6. what is the difference between the equal operator and the assignment operator
print(''' \n 
The assigment operator essentially assigns a value to a 
variable where as equal operator evaluates an exrepession
down to a single boolean value true.
''')

# 7. explain what a condition is where you would use one.
print(''' \n 
A condition is typically used in flow statements, typically for loops or switches, 
where a block of code will execute if a condition is true.
''')

# 8. identify 3 blocks in this code: 
print(''' \n 

spam = 0
if spam == 10: 
    print('eggs') <---- 1. 
    if spam > 5:
        print('bacon') <---- 2.
    else: 
        print('ham') <---- 3.
    print('spam')

print('spam')
''')

# 9. write code that prints hello if 1 is stored in spam, prints howdy if 2 
# is stored in spam, greetings if anything else is stored in spam

spam  = input()
if spam ==1:
    print('hello')
elif spam ==2:
    print('howdy')
else:
    print('greetings')



# 10. what keys can you you use if your program gets stuck in an infinite loop
print(''' \n 
control + c
''')

# 11. what is the different between break and continue
print(''' \n 
break exists the loop completely, however if there are multiple loops
it will exit the direct parent loop, where as continue goes back to the start
of the loop where the condition is evaluated. 
''')
# 12. what is the difference between range(10), range(0,10) and range(0,10,1)
print(''' \n 
range(10) => range of ints from 0 (ints start at 0) to 9. 
range(0, 10) => range of ints starting at 0 and ending at 10.
range(0,10,1) => range of ints starting at 0, ending at 10 and incrementing by 1.
''')

# 13. write a short program that prints numbers 1 to 10 using a for loop. then the same using a while loop

for x in range(10):
    print(x+1)

x = 0
while x <= 10:
    print(x)
    x += 1


# 14. if you had a function named bacon() inside a module named spam how would you call it after importing spam?
print(''' \n 
spam.bacon() OR variable = spam.bacon()
''')



