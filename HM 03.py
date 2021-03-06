#Q1

n = input("Enter employee's name: ")
h = int(input("Enter number of hour worked in a week: "))
r = float(input("Enter hourly pay rate: "))
ft = float(input("Enter federal tax withholding rate: "))
st = float(input("Enter state tax withholding rate: "))
gross = (h*r)
ft_2 = (ft*100)
st_2 = (st*100)
fm = ft*gross
sm = st*gross
total = fm+sm
net = gross - total
print(f"\n\nEmployee Name: {n}")
print(f"Hours Worked: {h:.1f}")
print(f"Pay Rate: {r:.2f}")
print(f"Gross Pay: {gross:.1f}")
print(f"Deductions: \n\tFederal Withholding({ft_2:.1f}%):${fm:.1f}")
print(f"\t State Withholding({st_2:.1f}%):${sm:.2f}")
print(f"\t Total Deduction: ${total:.2f}")
print(f"Net Pay: ${net:.2f}")

#Q2

print(input("Enter four-digit number: ")[::-1])


#Q3

from turtle import *
l = float(input("Enter length of the star: "))
for i in range(5):
    forward(l)
    right(144)
done()

#Q4

from turtle import *

def upper_circle(r):
    for i in range(3):
        if i == 2:
            color('red')
            circle(r)
        elif i < 2:
            if i == 1:
                color('black')
            elif i == 0:
                color('blue')
            circle(r)
            penup()
            forward((r*2)+(r/3))
            pendown()
def lower_circle(r):
    penup()
    goto(-100,0)
    forward(r+(r/4))
    right(90)
    forward((r))
    left(90)
    pendown()
    color('yellow')
    circle(r)
    penup()
    forward((r * 2) + (r / 3))
    pendown()
    color('green')
    circle(r)

r = float(input("Enter the radius: "))
speed(0)
penup()
goto(-100,0)
pendown()
pensize(r/9)
upper_circle(r)
lower_circle(r)
done()

#Q5

from turtle import *
try:
    p1 = list(map(float, input("Enter point 1: ").split()))
    p2 = list(map(float, input("Enter point 2: ").split()))
    p3 = list(map(float, input("Enter point 3: ").split()))
    if p1 == [] or p2 == [] or p3 == []:
        raise Exception
    if p1 == p2 or p2 == p3 or p1 == p3:
        raise ValueError("Error: Duplicate position!")
    else:
        area = abs(((p1[0] * (p2[1] - p3[1])) + (p2[0] * (p3[1] - p1[0]) + (p3[0] * (p1[1] - p2[1])))) / 2)
        penup()
        goto(p1[0], p1[1])
        pendown()
        goto(p2[0], p2[1])
        goto(p3[0], p3[1])
        goto(p1[0], p1[1])
        if (p1[0] <= p2[0] and p1[0] <= p3[0]) and (p1[1] <= p2[1] and p1[1] <= p3[1]):
            penup()
            goto(p1[0], p1[1])
            right(90)
            forward(20)
            left(90)
            pendown()
        elif (p2[0] <= p1[0] and p2[0] <= p3[0]) and (p2[1] <= p1[1] and p2[1] <= p3[1]):
            penup()
            goto(p2[0], p2[1])
            right(90)
            forward(20)
            left(90)
            pendown()
        elif (p3[0] <= p1[0] and p3[0] <= p2[0]) and (p3[1] <= p1[1] and p3[1] <= p2[1]):
            penup()
            goto(p3[0], p3[1])
            right(90)
            forward(20)
            left(90)
            pendown()
        write("The area is {:.2f}".format(area), font=("Arial", 16, "normal"))
        done()
except ValueError as err:
    print(err)
except Exception:
    print("Error: You did not enter a number!")
