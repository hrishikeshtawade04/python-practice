# Break

# av = 10
# i = int(input("Enter the number of candies you want: "))

# while av > 0 and i > 0:
#     if i > av:
#         print("Won't be able to dispense the amout requested")
#         break
#     av -= 1
#     i -= 1
#     print("Candy")


def dont_know_implementation():
    pass # This is a placeholder for the implementation of the function

# Continue
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        continue
    if i % 2 == 0:
        pass
    else:
        print(i)