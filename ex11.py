month = int(input("Input the month "))

thirtyone_days = [1,3,5,7,8,10,12]
thirty_days = [4,6,9,11]
if month == 2:
    print("This mon has 28 or 29 days")
if month in thirtyone_days :
    print("This month has 31 days")
if month in thirty_days:
    print("This month has 30 days")