
num = int(input("give me a number to check: "))
check = int(input("give me a number to divide: "))
if num % 4 == 0:
    print(num, "is multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if num % check == 0:
    print("success")
else:
    print("failure")

2