# example of using the same name variable in different scopes
# avoid this at all times! too much confusion.

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

# if you want python to modify a global variable you can use the global keyboard
# so python knows not to create a new local variable inside a function 
# example as below

eggs = 42
def eggs():
    global eggs
    eggs = 10
    print(eggs)

eggs()
