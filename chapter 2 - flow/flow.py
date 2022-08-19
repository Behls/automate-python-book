
class testBoolean():
    # constructor with variables
    def __init__(self, number):
        self.number = number
    # self is a binder so i dont need to pass variables in and can pass down variables
    def test(self):
        if(self.number>=12):
            print("this number is larger than 12")
        else:
            print("this number is not larger than 12 ")

test1 = testBoolean(11)
test1.test()


# boolean operators - and not or
# binary operators - two values in the expresssion - and or
# binary operators are a combination of operators(+,-,!) and operands(the expressional values on the left and right), usually only 2 values
# They are grouped by logical, arthimatic, relational and assignments


true = True
false = False

print("and - returns true when both values are true, otherwise false")
if (true and false): # condition evaluates, if true executes code underneath
    print("false")

elif (false and false):
    print("false")

elif (false and true):
    print("false")

elif (true and true):
    print("true")

print("or - prints true when one of the values is true otherwise false")
if (true or false):
    print("true")

elif (false or false):
    print("false")

elif (false or true):
    print("true")

elif (true or true):
    print("true")


print("not - only takes one boolean value, evaluates to the opposite boolean value")
if (not false):
    print("true")

if (not true):
    print("false")

print("you can compare different values and combine boolean operators such as and not")
#boolean operators are like the math ones, the have pesidence, after any cmoparison or math operations the order is:
#not>and>or
if((4<5) and not (4==5)):
    print("4 is lesser than 5 but not equal to it")

# the order of elif statements matters, as when its condition means true the following expressions wont be executed.

# some values can be considered as true and false: 
#true conditions typically used if using loops and conditions. if trueInt: or while not falseInt etc.
trueInt = 1 # >=1
trueFloat=0.1 #>=0.1
trueString='this is a true string' # not ''

# default false conditions handy for conditional coding(must be this to be false)
falseInt = 0
falseFloat=0.0
falseString=''

