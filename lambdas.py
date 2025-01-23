# Also called anonymous functions
#hey are typically used in situations where you need to pass a simple function as an argument, 
# especially if it’s only used once or is very short-lived.

from functools import reduce

f = lambda a : a*a
result  = f(5)
print(result)

add = lambda a,b : a+b
print(add(1,2))

nums = [1, 2, 3]
evens = list(filter(lambda a: a % 2 == 0, nums))
print(evens)

doubles = list(map(lambda a: a * 2, nums))
print(doubles)

sum = reduce(lambda a, b: a + b, nums)
print(sum)