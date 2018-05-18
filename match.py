score = {}


def userdata():
    name = input("Enter player's name:")
    run = int(input("Enter run"))
    return name, run


def addrun(run, score):
    global b


    if run == 4:

        t = 'fours' in score[name]
        b = 'balls' in score[name]
        if t :
            f = score[name]['fours']
            print(f)
            f += 1
            score[name]['fours'] = f
            r = score[name]['runs']
            r += run
            score[name]['runs'] = r

        else:
            score[name]['fours'] = 1
            score[name]['six'] = 0
            score[name]['runs'] = run
            score[name]['balls'] = 1

            return b
    elif run == 6:
        t = 'six' in score[name]
        b = 'balls' in score[name]
        if t:
            f = score[name]['six']
            print(f)
            f += 1
            score[name]['six'] = f
            r = score[name]['runs']
            r += run
            score[name]['runs'] = r

        else:
            score[name]['six'] = 1
            score[name]['fours'] = 0
            score[name]['runs'] = run
            score[name]['balls'] = 1
            return b
    elif run != 4 or run != 6:
        t = 'runs' in score[name]
        b = 'balls' in score[name]
        if t:
            r = score[name]['runs']
            r +=run
            score[name]['runs'] = r


        else:
            score[name]['fours'] = 0
            score[name]['six'] = 0
            score[name]['balls'] = 1
            score[name]['runs'] = run
            return b


    return b
while True:
    name, run = userdata()
    if name in score:
        pass
    else:
        score[name] = {}
    b = addrun(run, score)

    if b:
        b1 = score[name]['balls']
        b1 += 1
        score[name]['balls'] = b1
        r = score[name]['runs']
        r += run
        score[name]['runs'] = r-run

    print(score)

