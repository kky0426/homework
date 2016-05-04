def charCount():
    word=raw_input("input word:")
    d=dict() 
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d 
    
    matplotlib inline
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values())
    plt.xticks(range(len(d)),list(d.keys()))    
    plt.show()




def countDigitsLetter():
    word=raw_input("input word:")
    d=dict()
    d={"number":0, "word":0}
    for i in word:
        if i.isdigit()==True:
            d["number"]=d["number"]+1
        elif i.isdigit()==False:
            d["word"]=d["word"]+1
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()





def lab9-1():
	charCount()
	countDigitsLetter()

def main():
	lab9-1()


wn.exitonclick()


if __name__=="__main__":
    main()