def aLeapyear():
    sel=raw_input("input year:")
    if float(sel)%4==0 and (float(sel)%100!=0 or float(sel)%400==0):
        print "a leap year"
    else:
        print "No"



def sumList(aList):
    x=list()
    sum=0
    for i in range(0,aList):
        if(i%4==0 and i%5):
            x.append(i)
    for i in range(0,len(x)):
        sum+=x[i]
    return sum




def lab6-2():
	sumList(2000)



def lab6-1():
	aLeapyear()
def main():
	lab6-1()    
	lab6-2()


if __name__=="__main__":
    main()