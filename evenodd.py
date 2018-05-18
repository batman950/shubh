num = int(input("enter a num"))
if num % 2 == 0:
    print("even")
    if num % 4 == 0:  # check whether the num is divisible by 4 or not
        print("is divisible by 4:", num)
    else:
        print("enter a number divisible by 4  ")
else:
    print("odd")
    if num % 3 == 0:
        print("is divisible by 3:", num)
    else:
        print("enter a number divisible by 3")