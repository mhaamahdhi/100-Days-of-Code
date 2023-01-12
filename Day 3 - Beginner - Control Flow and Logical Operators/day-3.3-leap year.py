year = int(input("Which year do you want to check : "))

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print("Leap Year 2")
        else:
            print("Not Leap year 1")
    else:
        print("Leap year 1")
else:
    print("Not Leap Year 2")