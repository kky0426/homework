def coffee():
	allData=[
	["Coffee","Water","Milk","Icecream"],
	["Espresso","No","No","No"],
	["Long Black","Yes","No","No"],
	["Flat White","No","Yes","No"],
	["Cappuccino","No","Yes","No"],
	["Affogato","No","No","Yes"]
	]
	data=allData[1:]

	sum=0
	sum=float()
	for i in data:
    		if i[2].upper()=='YES':
        	sum=sum+1
		per=sum/len(data)*100
	print per,"%"





def lyrics():
	lyrics=dict()
	lyrics=["When I find myself in times of trouble","Mother Mary comes to me""Speaking words of wisdom let it be",
	"And in my hour of darkness",
	"She is standing right in front of me",
	"Speaking words of wisdom let it be",

	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",

	"And when the broken-hearted people",
	"Living in the world agree",
	"There will be an answer let it be",
	"For though they may be parted",
	"There is still a chance that they will see",
	"There will be an answer let it be",
	
	"Let it be let it be",
	"Let it be let it be",
	"Yeah there will be an answer let it be",
	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",

	"Let it be let it be",
	"Ah let it be yeah let it be",
	"Whisper words of wisdom let it be",

	"And when the night is cloudy",
	"There is still a light that shines on me",
	"Shine on until tomorrow let it be",
	"I wake up to the sound of music",
	"Mother Mary comes to me",
	"Speaking words of wisdom let it be",

	"Let it be let it be",
	"Let it be yeah let it be",
	"Oh there will be an answer let it be",
	"Let it be let it be",
	"Let it be yeah let it be",
	"Whisper words of wisdom let it be"]



	d=dict()
	doc=lyrics
	for l in doc:
   	     words=l.split()
   	     for word in words:
       	 	   if word not in d:
         	       d[word]=1
        	   else:
            	       d[word]=d[word]+1
	print d            

	for i in d:
            	if(d[i]>=20):
                	print  i, d[i]


def lab10():
	coffee()
	lyrics()



def main():
	lab10()



wn.exitonclick()



if __name__=="__main__":
    main()


