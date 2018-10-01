username = input("Please input your username ")


loop1 = True

while True:
    email = input("Please input your email ")
    if "@" in list(email) and "." in list(email) and " " not in list(email):
        break

while loop1:
    digit_count = 0
    letter_count = 0
    password = input("please input your password ")
    for i in list(password):
        if i.isdigit():
            digit_count += 1
        if i.isalpha():
            letter_count += 1
    if digit_count > 0 and letter_count > 0:
        if len(list(password)) >= 8:
            print("You have successfully signed in")
            loop1 = False