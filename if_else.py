# If will have to follow indentation. Generally 4 spaces or 1 tab.
if True:
    print("True")

x = 4
y = x % 2
if y == 0: # evaluating a condition
    print("Even")
    if x > 5:
        print("Greater than 5")
    elif x > 3:
        print("Greater than 3")
    else:
        print("Less than 3")
else:
    print("Odd")

