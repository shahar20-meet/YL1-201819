import turtle

numb1 = 14
print(numb1)
numb2 = numb1/2
print(numb2)

mylist=[4,6,8]
sum = 0
for i in range(3):
    print(mylist[i]*2)
    print(mylist[i])
    sum = sum + mylist[i]
    print(sum)
    
turtle.pensize(9)
turtle.color("green")
turtle.circle(70)
turtle.color('yellow')
turtle.penup()
turtle.goto(-120, 0)
turtle.pendown()
turtle.circle(70)
turtle.color('red')
turtle.penup()
turtle.goto(60,80)
turtle.pendown()
turtle.circle(70)
turtle.color('black')
turtle.penup()
turtle.goto(-60, 80)
turtle.pendown()
turtle.circle(70)
turtle.color('blue')
turtle.penup()
turtle.goto(-180, 80)
turtle.pendown()
turtle.circle(70)
 
