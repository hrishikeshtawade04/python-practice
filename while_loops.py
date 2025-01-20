# Increasing while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Decreasing while loop
i = 5
while i >=1:
    print(i)
    i -= 1

# Nested while loop
row = 1
while row <= 5:
    col = 1
    while col <= 5:
        if col < row:
            print(' ', end=' ')
        else:
            print('*', end='@')
        col += 1
    row += 1
    print()