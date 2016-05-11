import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def keyup():
     t1.fd(50)
     if (50<x<150 and y==50):
	   t1.write("you trapped")	


def keyback():
     t1.backward(50)
     if (50<x<150 and y==50):
	  t1.write("you trapped")	
def keyright():
     t1.right(90)

def keyleft():
     t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)	
    if (50<x<150 and y==50):
		t1.write("you trapped")


def quit():
    wn.bye()


def line():
	t1.penup()
	t1.goto(50,50)
	t1.pendown()
	t1.fd(100)
	t1.penup()
	t1.home()


def addKeys():	
    wn.onkey(keyup,"Up")
    wn.onkey(keyback,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
 

def addMouse():
    wn.onclick(mousegoto)

def addQuit():
    wn.onkey(quit,"q")


def lab11():
     line()	
     addQuit()
     addMouse()
     addKeys()
     wn.listen()
     turtle.mainloop()

lab11()

