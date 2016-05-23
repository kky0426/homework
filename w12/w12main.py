#파이썬이 들어간 줄 출력

def python():
	try:
    	    myfile=open('python.txt','r')
    	    for line in myfile:
                if line.find("Python")>=0:
                    print line
            myfile.close()        
        except IOError as e:
            print e

#대문자 변환
def upper():
    myfile=open('output.txt','w')
    line1='first line\n'
    myfile.write(line1.upper())
    line2='\tsecond line\n'
    myfile.write(line2.upper())
    line3='third'
    myfile.write(line3.upper())
    myfile.close()



def lab12():
	python()
	upper()



def main():
	lab12()



if __name__=="__main__": 
     main()

