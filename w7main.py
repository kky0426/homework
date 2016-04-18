
def drawSquareAtSave(size, pos):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        tracks.append(i)
    for i in range(0,4):
        x[i]=t1.pos()
        t1.forward(size)
        t1.right(90)
    print tracks






def lab7():
    drawSquareAtSave(100,(100,100))



def main():
    lab7()	



wn.exitonclick()

if __name__=="__main__":
    main()