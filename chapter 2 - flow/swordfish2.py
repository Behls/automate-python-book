import flow as bd

while True: 
    print('who are you')
    name = input()
    if name!='joe':
        continue
    password = input('hello joe what is the password. (Its a fish btw) \n')
    if password =='swordfish':
        print('that password was correct, welcome joe')
        break

print('access granted')