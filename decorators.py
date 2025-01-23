def div(a, b):
    return a / b

div(2, 4)  # 2.0
print(div(2, 4))  # 2.0

# Using decorators you can add some additional functionality to the function
# without changing the function itself.
# Decorators are functions that wrap another function and add some additional
# functionality to it.

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b= b,a
        return func(a,b)
    return inner

div = smart_div(div)

print(div(2, 4))  # 2.0