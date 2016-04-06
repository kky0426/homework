def aLeapyear():
    sel=raw_input("input year:")
    if float(sel)%4==0 and (float(sel)%100!=0 or float(sel)%400==0):
        print "a leap year"
    else:
        print "No"

def lab6():
	aLeapyear()
def main():
	lab6()    



if __name__=="__main__":
    main()