f = open("inputOne.txt")
content = f.read().strip()

def firstMarker(message):
	marker = set()	
	markerLenght = 14
	cpt = 0
	for lettre in message:
		temp = markerLenght
		marker.clear()
		while(temp > 0):
			marker.add(message[cpt + temp])
			temp -= 1
		cpt += 1
		if(len(marker) == markerLenght ):
			return cpt + markerLenght
	

x = firstMarker(content)
print(x)