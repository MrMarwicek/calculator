while True:
    a = str(input("Do u like to use +, -, /, * or 2square"))
    if a==("+"):
        b1 = int(input("Okay what is the first number?"))
        b2 = int(input("Okay what is the second number?"))
        print (b1+b2)
    elif a==("-"):
        c1 = int(input("Okay what is the first number?"))
        c2 = int(input("Okay what is the secont number?"))
        print (c1-c2)
    elif a==("/"):
        d1 = int(input("Okay what is the first number?"))
        d2 = int(input("Okay what is the second number?"))
        print (d1/d2)
    elif a==("*"):
        e1 = int(input("Okay what is the first number?"))
        e2 = int(input("Okay what is the second number?"))
        print (e1*e2)
    elif a==("2square"):
        f = int(input("Okay what is the number you want to calculate from squares?"))
        print (f*f)
    elif a==("break"):
        break
    else:
        print("unknown command")
    p = str(input("Do you whant to countinue?"))
    if p==("yes"):
        continue
    else:
        break