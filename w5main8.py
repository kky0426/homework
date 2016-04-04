import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def computeBMI():
    sel1=raw_input("input your weight:")
    sel2=raw_input("input your height:")

    bmi=float(sel1)/(float(sel2)*float(sel2))

    if bmi>=18.5 and bmi<25.0:
      print "nomal weight"
    elif bmi>=25.0 and bmi<=29.9:
      print "over weight"
    else:
       print "error"
computeBMI()
def lab5():
    computeBMI()
def main():
    lab5()
wn.exitonclick()
if __name__=="__main__":
    main()	