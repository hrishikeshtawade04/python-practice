# Global variable
a = 10

def f1():
    # Local variable
    a = 20 # this creates a new local variable
    print(a) # preference to local variable

def f2():
    print(a) # preference to global variable

def f3():
    global a # this will specify that we are using global variable
    a = 30

def f4():
    a = 40 # this creates a new local variable
    x = globals()['a'] # this will access the global variable
    # x = 1010 # this will create a new local variable
    globals()['a'] = 1010 # this will change the global variable
    print(a)
    
f1()
print(a)
f2()
f3()
print(a)
f4()
print(a)
