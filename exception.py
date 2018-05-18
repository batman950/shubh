while 1:
    try:
        num=int(input("enter number\n"))
        print(18/num)
        print("\n")
        break
    except ValueError:
        print("enter numeric value\n")
    except ZeroDivisionError:
        print("enter other value other then 0\n")
    finally:
        print("you got it\n")