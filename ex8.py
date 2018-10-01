from turtle import *

shape("turtle")
color("green")

n = int(input("Input the side of the polygon "))
if n > 0:
    for i in range (n):
        forward(50)
        left(180-(180*(n-2)/n)) #viết lại dc thành 360/n

mainloop()