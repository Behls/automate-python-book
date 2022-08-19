name = 'carol'
age = 3000

if name == 'Alice':
    print("hi, alice")
elif age<12:
    print("your not alice kiddo")
elif age>100:
    print("you are not alice grannie")
    # this elif is skipped as previous one returns true. only works if it returns false
elif age>2000:
    print("unlike you, alice is not an undead, imortal vampire")

