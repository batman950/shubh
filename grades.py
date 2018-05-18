students = {"a": 70, "b": 90, "c": 65, "d": 45}
for i in students:
    if students[i] > 80:
        print("A", i, str(students[i]))
    elif students[i] > 60 & students[i] < 80:
        print("B", i, str(students[i]))
    elif students[i] > 50 & students[i] > 60:
        print("C", i, str(students[i]))
    else:
        print("fail", i, str(students[i]))
