import turtle

turtle.speed(1)

def нарисовать_символ():

    turtle.fillcolor("black")
    turtle.begin_fill()

    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(-80)
    turtle.rt(90)
    turtle.fd(-60)
    turtle.rt(90)
    turtle.fd(-20)
    turtle.rt(90)
    turtle.fd(-40)
    turtle.rt(90)
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(-100)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(-80)
    turtle.rt(90)
    turtle.fd(-20)
    turtle.rt(90)
    turtle.fd(-40)
    turtle.rt(90)
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(-100)
    turtle.rt(90)
    turtle.fd(100)

    turtle.end_fill()

turtle.penup()
turtle.goto(-300, 100)
turtle.pendown()

for i in range(4):
    нарисовать_символ()
    
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(150)
    turtle.pendown()

turtle.done()
