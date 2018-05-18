string = input("enter a string \n")

rev = string[::-1]
print(rev)
if string == rev:
    print("palindrome")
else:
    print("not")