# there are local scopes and global scopes
# global are initialised outside functions where as local variables are initialised temporarly inside functions
# when a program is terminated the values stored in the global scope are terminated
# when a function returns a value(finishes) the local scope is destroyed
x = 0
print(str(x)+ ' is a global variable') 

def num(k):
    k +=1
    return print(str(k) + ' is a local variable')

num(10)


# code in the global scope cannot use variables stored in the local scope
# code in local scopes can use global variables.
# functions cannot use other variables in local scopes

# you can name variables the same inside different functions 
# not ideal though for reading code.

# local variables/scope example
def egg():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    eggs =0

egg()

# because the egg function calls the bacon function, eggs in bacon is destroyed once it rreturns a value
# hence why egg returns a value of 99 when calling the egg function.

def breakfast():
    print(meat)

meat = 42
breakfast()
print(meat)