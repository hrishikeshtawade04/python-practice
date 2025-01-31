def greet():
    print("Hello, World!")

greet()

def addAndSub(a, b):
    return a + b , a - b

result = addAndSub(1, 2)
summation, difference = addAndSub(1, 2)
print(summation)
print(difference)
print(result)


# Not pass by reference or pass by value
# This is immutable
def update(x):
    print(id(x)) # same id as a but still its not pass by reference
    x = 5
    print(id(x)) # different id

a = 10
print(id(a))
update(a)
print(a)

# This is mutable
def updateList(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))

lst = [10, 20, 30]
print(lst)
print(id(lst))
updateList(lst)
print(lst)

# Get even and odd list
def getEvenOdd(lst):
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

lst = [10, 20, 25, 30, 35, 40]
even, odd = getEvenOdd(lst)
print("Even List: {} and Odd : {}".format(even, odd))

