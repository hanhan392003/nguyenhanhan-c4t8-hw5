import random
question_count = 0
while True :
    a = random.randint(0,10)
    b = random.randint(0,10)
    operater = ["+", "-"]
    d = random.choice(operater)

    if d == "+":
        c = a + b
    elif d == "-":
        c = a - b
    numbers = [-1, 0, 1]
    n = random.choice(numbers)
    e = c + n

    if question_count >= 5:
        a = random.randint(0,20)
        b = random.randint(0,20)
        operater = ["+", "-"]
        d = random.choice(operater)

        if d == "+":
            c = a + b
        elif d == "-":
            c = a - b
        numbers = [-1, 0, 1]
        n = random.choice(numbers)
        e = c + n
       
        if a < 10 or b < 10:
            operater = ["+", "-", "*"]
            d = random.choice(operater)
            if d == "*":
                c = a*b
            if d == "+":
                c = a + b
            elif d == "-":
                c = a - b
            numbers = [-1, 0, 1]
            n = random.choice(numbers)
            e = c + n
        

    print (a, d, b, "=", e)
    i = input("Please input True(t or T) or False(F or f) ")
    
    if e == c and i == "t" :
        question_count += 1
    elif e != c and i == "f" :
        question_count += 1
    else:
        break    
        