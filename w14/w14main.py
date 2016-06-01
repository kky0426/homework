

class Dog(object):   
    def talk(self):
        print "mung mung"

class ShihTzuDog(object):
    def talk(self):
        print "si si"
        
class Maltese(object):
    def talk(self):
        print "mal mal"

def DogTalk():
	mydog1=Dog()
	mydog1.talk()
	mydog2=Maltese()
	mydog2.talk()
	mydog3=ShihTzuDog()
	mydog3.talk()



def lab14():
	DogTalk()


def main():
	lab14()


if __name__=="__main__": 
     main()
