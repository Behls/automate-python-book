while True:
    print('enter user name')
    username = input()
    if username != 'joe':
        continue 
    # continues the code onto the next condition, you wouldnt typically do this as its not logical
    # you would code an error statment and redirect to the beginning rather than continuing code for usernames etc
    print('hi joe, what is your password? its a fish')
    password = input()
    if password =='swordfish':
        break # exists the loop
        
print('access granted')
