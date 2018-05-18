def drop(grades):
    first, *mid, last = grades
    avg = sum(mid)/len(mid)
    print(first)
    print(last)
    print(*mid)
    print("now the outcome is:")
    print("the average is", avg)
drop([13, 667.6567, 54, 5, 87, 8])