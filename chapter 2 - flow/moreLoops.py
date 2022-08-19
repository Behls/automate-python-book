for i in range(5):
    print('my name is jimmiy ('+str(i+1)+')')

# adding all the numbers from 0-100 to total using a for loop
total=0
for x in range(100):
    total += x
    print(total)

# while loops  may need iterators embedded in the clause to help determine the evaluation at the start
print('my name is :')
i=0
while (i<5):
    print('my name is jimmy ('+str(i+1)+')')
    i += 1

# range function can accept 3 integers are paramters => start, stop, stepping.
# range(0,10, 2)
# starts at 0
# stops at 10 (doesnt include the stop number(10))
# steps at 2 intervals, 2,4,6,8
# example:

print('counting up')
for i in range(0,10,2):
    print(i)

print('counting down')
# 
for i in range(5,-1, -1):
    print(i)