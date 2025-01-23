# Also called anonymous functions
#hey are typically used in situations where you need to pass a simple function as an argument, 
# especially if it’s only used once or is very short-lived.

f = lambda a : a*a
result  = f(5)
print(result)

add = lambda a,b : a+b
print(add(1,2))