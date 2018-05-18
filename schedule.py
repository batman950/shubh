# construct A program such that can show the days u are doing ur classes
for k in range(1, 5):
    print("week:", k, "\n")
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    for i in range(7):
        if i % 3 == 0 & i % 7 == 0:
            print("no classes")
        else:
            print("the day for classes:", days[i])
    print("\n")

