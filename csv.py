import csv

c = 0
with open('data.csv', newline='')as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
        c += 1

print(c)
