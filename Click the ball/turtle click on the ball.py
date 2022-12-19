import turtle
import tkinter.messagebox
import random
turtle.bgcolor("skyblue")
turtle.pencolor("white")
turtle.speed(0)
turtle.pensize(3)
turtle.write("PRESS SPACE TO START THE GAME",align="center", font=("algerian", 30))
turtle.hideturtle()
turtle.up()
turtle.goto(-400,-400)
turtle.down()


for j in range(4):
    turtle.fd(800)
    turtle.left(90)

def winner() :
    tkinter.messagebox.showinfo('you have won the game',['you have won the game'])
def draw():
    
    turtle.clearscreen()
    turtle.bgcolor("skyblue")
    turtle.pencolor("white")
    turtle.speed(0)
    turtle.pensize(3)
    turtle.up()
    turtle.goto(-500,-500)
    turtle.down()
    for j in range(4):
        turtle.fd(1000)
        turtle.left(90)


    t1 = turtle.Turtle()
    t1.speed(0)
    t1.shape('circle')
    t1.shapesize(5)
    t1.color("red")

    t2 = turtle.Turtle()
    t2.speed(0)
    t2.up()
    t2.goto(100, 0)
    t2.down()
    t2.color("blue")
    t2.shape('circle')
    t2.shapesize(5)

    t3 = turtle.Turtle()
    t3.speed(0)
    t3.up()
    t3.goto(-100, 0)
    t3.down()
    t3.color("green")
    t3.shape('circle')
    t3.shapesize(5)

    t4 = turtle.Turtle()
    t4.speed(0)
    t4.up()
    t4.goto(200, 0)
    t4.down()
    t4.color("pink")
    t4.shape('circle')
    t4.shapesize(5)

    t5 = turtle.Turtle()
    t5.speed(0)
    t5.up()
    t5.goto(-200, 0)
    t5.down()
    t5.color("yellow")
    t5.shape('circle')
    t5.shapesize(5)

    t6 = turtle.Turtle()
    t6.speed(0)
    t6.up()
    t6.goto(300, 0)
    t6.down()
    t6.color("orange")
    t6.shape('circle')
    t6.shapesize(5)

    t7 = turtle.Turtle()
    t7.speed(0)
    t7.up()
    t7.goto(-300, 0)
    t7.down()
    t7.color("purple")
    t7.shape('circle')
    t7.shapesize(5)

    t8 = turtle.Turtle()
    t8.speed(0)
    t8.up()
    t8.goto(0, 100)
    t8.down()
    t8.color("white")
    t8.shape('circle')
    t8.pensize(5)
    t8.shapesize(5)

    t9 = turtle.Turtle()
    t9.up()
    t9.speed(0)
    t9.shape('circle')
    t9.shapesize(1)
    while True:

        t1.up()
        t1.goto(random.randint(-400,400),random.randint(-400,400))
        t1.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break        
        t2.up()
        t2.goto(random.randint(-400,400),random.randint(-400,400))
        t2.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t3.up()
        t3.goto(random.randint(-400,400),random.randint(-400,400))
        t3.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t4.up()
        t4.goto(random.randint(-400,400),random.randint(-400,400))
        t4.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t5.up()
        t5.goto(random.randint(-400,400),random.randint(-400,400))
        t5.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t6.up()
        t6.goto(random.randint(-400,400),random.randint(-400,400))
        t6.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t7.up()        
        t7.goto(random.randint(-400,400),random.randint(-400,400))
        t7.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            break
        t8.up()        
        t8.goto(random.randint(-400,400),random.randint(-400,400))
        t8.down()
        if (t8.xcor()-48 <= t9.xcor() <= t8.xcor()+48 ) and (t8.ycor()-48 <= t9.ycor() <= t8.ycor()+48):
            print("you have won")
            winner()
            break
        turtle.onscreenclick(t9.goto)
turtle.onkeypress(draw, "space")
turtle.listen()

tkinter.mainloop()
