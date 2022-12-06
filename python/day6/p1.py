f = open("inputOne.txt")
content = f.read().strip()

# z = "wxyz"
# y = "zxww"
# thisset = {"apple", "banana", "cherry"}
# thisset.add("apple")
# print(thisset)
# print( z[0] in  {z[1] , z[2] , z[3]})
# print( y[0] in  {y[1] , y[2] , y[3]})


def firstMarker(message):
	#create a set and add elements to it till it lenght is 3 insead of 4
	marker = set()
	markerLenght = 4
	result = 0
	
	cpt = 0
	for lettre in message:
		marker.clear()
		marker.add(message[0 + cpt])
		marker.add(message[1 + cpt])
		marker.add(message[2 + cpt])
		marker.add(message[3 + cpt])
		if(len(marker) == 4 ):
			print(cpt + 4)
			return cpt + 4
		cpt += 1 


firstMarker(content)