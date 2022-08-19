import sys

def divideBy(x):
    return 42 / x

print(divideBy(6))
print(divideBy(20))
# print(divideBy(0)) 
# dividing by zero returns an error. and exception would deal with this well
print(divideBy(4))


# it would be amended to: 
# Try catch statements are great for error handling, ideally want to use them frequently. 
def divideBy(x):
    # try a block of code. 
    try:
        return 42 / x
    # except and error of a type and print or execute a peaice of code if code runs into that error
    except ZeroDivisionError:
        sys.exit("cannot divide by zero try another number")

print(divideBy(6))
print(divideBy(20))
print(divideBy(0)) 
# will return a false value for that data type 
print(divideBy(4))

