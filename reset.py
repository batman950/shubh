def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 - i]

    print(x)

word = input("enter")
rev = reverse(word)
