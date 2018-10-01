try :
    n = int(input("Input a number "))
    if n % 2 == 0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")
except ValueError:
    print("please start the program again")