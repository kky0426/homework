def outputUpper():
	import time
	editor='kjy'
	timeEdited=time.strftime('%Y-%m-%d %H:%M:%S')

	myfile=open('output.txt','w')
	line1='first line\n'
	myfile.write(line1)
	line2='\tsecond line\n'
	myfile.write(line2)
	line3='third'
	myfile.write(line3)
	myfile.close()
        
	fin=open('output.txt','r')
	fout=open('outputUpper.txt','w')
	for line in fin:
	    if 'line' in line:
	        fout.write("[{0} edited {1}]".format(editor,timeEdited)+line.replace('line', 'line'.upper()))
	    else: 
	        fout.write(line)        
	    fout.write('\n')    
	fin.close()
	fout.close()


def outputNumber():
	data=[1,2,3,4,5,6,7,8,9,10]
	fout=open('outputNumber.txt','w')
	for i in data:
	    toPrint="{0}\t".format(i)
	    fout.write(toPrint,)
	    if i%2==0:
	        fout.write('\n')
	fout.close()
	


def addFile():
	try:
	    fin1=open('python.txt','a')
	    fin2=open('outputNumber.txt','r')
	    for line in fin2:
	        fin1.write(line)
	    fin1.close()
	    fin2.close()
	except IOError as e:
	    print e
    



def lab13():
	outputUpper()
	outputNumber()
	addFile()


def main():
	lab13()



if __name__=='__main__' :
	main()



