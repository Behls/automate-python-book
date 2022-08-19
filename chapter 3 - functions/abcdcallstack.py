
# optional arguements
print('hello world')

print('hello', end=' ')
print('world')

print('cats','dogs','babies')
print('cats','dogs','babies', sep=',')

# sep = seperate, common sense seperates the words
# end = end of the sentence add on a string
# functions can have optional arguments that do not have to be called unless specified.


# basics of call stacks 
print('---- call stack intro ----')
print('the call stack is like a conversation, adds a stack when called and removed when returned. If a calls b then b needs to finish so a can finish')
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

