
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





import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def saveTracks():
    tracks=list()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks

def replayTracks(Tracks):
    for t in Tracks:
        print t
    for i in range(0,len(Tracks)):
        t1.goto(Tracks[i])












def lab7-1():
    drawSquareAtSave(100,(100,100))
def lab7-2():
    mytracks=saveTracks()
    replayTracks(mytracks)


def main():
    lab7-1()	
    lab7-2()


wn.exitonclick()

if __name__=="__main__":
    main()