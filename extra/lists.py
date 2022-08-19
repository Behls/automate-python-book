number = 5;
for x in range(1,number+1):
    print('*' * x)


# star pyramid from list 

lists = [3,4,2,1,4,2,1,5]

print(lists)

for x in range(len(lists)):
    if x==x:
        print('*' * x)


#  from user input

def makePyramid(y):
    
    for x in range(1, y+1):
        print('*' * x)

number = input("enter a number loser")
converted = int(number)
makePyramid(converted)

# pyramid list
for x in range(4):
    print('*' * int(x+1))


