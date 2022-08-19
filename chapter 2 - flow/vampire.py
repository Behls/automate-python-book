#version 1

name = 'carol'
age = 3000

if name == 'Alice':
    print("hi, alice")
elif age<12:
    print("your not alice kiddo")
elif age>2000:
    print("unlike you, alice is not an undead, imortal vampire")
    # doesnt execute the bottom elif because the first returns a true boolean
    # elif statements only execute if previous code or if statements return a false boolean
elif age>100:
    print("you are not alice grannie")
