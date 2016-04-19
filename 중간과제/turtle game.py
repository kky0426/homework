import turtle
import sys
wn=turtle.Screen()
wn.bgpic("bg.gif")
t1=turtle.Turtle()
t1.shape("turtle")
ta=turtle.Turtle()
ts=turtle.Turtle()
td=turtle.Turtle()
tf=turtle.Turtle()
tg=turtle.Turtle()
th=turtle.Turtle()

t1.penup()
ta.penup()
ts.penup()
td.penup()
tf.penup()
tg.penup()
th.penup()

t1.shapesize(5)
ta.shapesize(2)
ts.shapesize(2)
td.shapesize(2)
tf.shapesize(2)
tg.shapesize(2)
th.shapesize(2)

ta.color("blue")
ts.color("blue")
td.color("blue")
tf.color("blue")
tg.color("blue")
th.color("blue")

ta.right(180)
ts.left(135)
td.left(90)
tf.right(90)
tg.left(45)

t1.setpos(-200,-200)
ta.setpos(15,200)
ts.setpos(80,210)
td.setpos(165,210)
tf.setpos(240,190)
tg.setpos(315,210)
th.setpos(385,200)

oldhead=t1.heading()
def h1():
    t1.setheading(oldhead)
    t1.right(180)
def h2():
    t1.setheading(oldhead)
    t1.left(135)
def h3():
    t1.setheading(oldhead)
    t1.left(90)
def h4():
    t1.setheading(oldhead)
    t1.right(90)
def h5():
    t1.setheading(oldhead)
    t1.left(45)
def h6():
    t1.setheading(oldhead)


oldhead=t1.heading()
def h1():
    t1.setheading(oldhead)
    t1.right(180)
def h2():
    t1.setheading(oldhead)
    t1.left(135)
def h3():
    t1.setheading(oldhead)
    t1.left(90)
def h4():
    t1.setheading(oldhead)
    t1.right(90)
def h5():
    t1.setheading(oldhead)
    t1.left(45)
def h6():
    t1.setheading(oldhead)


def moveA():
    ta.color("green")
    ta.speed(1)
    ta.setpos(15,-220)
    if not (t1.heading()==ta.heading()):
        sys.exit()
    ta.speed(100)
    ta.color("blue")
    ta.setpos(15,200)
def moveS():
    ts.color("green")
    ts.speed(1)
    ts.setpos(80,-210)
    if not (t1.heading()==ts.heading()):
        sys.exit()
    ts.speed(100)
    ts.color("blue")
    ts.setpos(80,210)     
def moveD():
    td.color("green")
    td.speed(1)
    td.setpos(165,-210)
    if not (t1.heading()==td.heading()):
        sys.exit()
    td.speed(100)
    td.color("blue")
    td.setpos(165,210)
def moveF():
    tf.color("green")
    tf.speed(1)
    tf.setpos(240,-230)
    if not (t1.heading()==tf.heading()):
        sys.exit()
    tf.speed(100)
    tf.color("blue")
    tf.setpos(240,190)
def moveG():
    tg.color("green")
    tg.speed(1)
    tg.setpos(315,-210)
    if not (t1.heading()==tg.heading()):
        sys.exit()
    tg.speed(100)
    tg.color("blue")
    tg.setpos(315,210)
def moveH():
    th.color("green")
    th.speed(1)
    th.setpos(385,-220)
    if not (t1.heading()==th.heading()):
        sys.exit()
    th.speed(100)
    th.color("blue")
    th.setpos(385,200)

t2=turtle.Turtle()
t2.penup()
t2.setpos(-380,200)
t2.write("'a''s''d''f''g''h'를 이용해 화살표 방향에 맞게 거북이의 방향을 조절하세요")
t2.setpos(-380,180)
t2.write("시작하려면 y를 누르세요")


def gameStart():
    import random
    for i in range(1,20):
        x=random.randint(1,6)
        if (x==1):
            moveA()
        elif (x==2):
            moveS()
        elif (x==3):
            moveD
        elif (x==4):
            moveF()
        elif (x==5):
            moveG()
        elif (x==6):
            moveH()


wn.onkey(h1,"a")
wn.onkey(h2,"s")
wn.onkey(h3,"d")
wn.onkey(h4,"f")
wn.onkey(h5,"g")
wn.onkey(h6,"h")
wn.onkey(gameStart,"y")
wn.listen()
wn.exitonclick()