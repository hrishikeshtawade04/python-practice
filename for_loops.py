# x = [1, 2, 3, 4, 5]

# # We don't need to initialize i and increment it as well. For loop does that for us
# for i in x:
#     print(i, end='')
# print()

# for i in range(20, 9, -5):
#     print(i)


# nums = [1, 2, 4, 5]
# for num in nums:
#     if num == 3:
#         print('Found!')
#         break # This is compulsory to print the else below.
# else:
#     print('Not Found!')

# Check if given number is prime or not
number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers are not prime")
elif number <= 1:
    print(number, " is not a prime number")
else:
    for i in range(2, number): # There is more efficient methods. Example you can go till sqrt only.
        if number % i == 0:
            print(number, " is not prime")
            break
    else:
        print(number, " is prime number")
