import math
x=37.575754
y=126.973554
Locations=tuple()
Locations=[(37.571594, 126.976626),(37.576478, 126.985408),(37.570165, 126.983010),(37.574511, 126.957740)]
sel=list()
for i in Locations:
    sel.append(math.sqrt((x-i[0])**2+(y-i[1])**2))
print min(sel)         

wn.exitonclick()