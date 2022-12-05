file = open("inputOne.txt")
content = file.read()

def toPairList(content):
	return list(filter(None,content.split('\n')))

def checkIfContained(pair):
	pairList = pair.split(',')
	listOne = pairList[0]
	listOneFElem = int(listOne.split('-')[0])
	listOneLElem = int(int(listOne.split('-')[1]))
	listTwo = pairList[1]
	listTwoFElem = int(listTwo.split('-')[0])
	listTwoLElem = int(int(listTwo.split('-')[1]))

	setOne = set(range(listOneFElem,listOneLElem + 1))
	setTwo = set(range(listTwoFElem,listTwoLElem + 1))
	return (setOne.issubset(setTwo) or setTwo.issubset(setOne))

def containedCount(content):
	listOfPairs = toPairList(content)
	totalPairsContained = 0
	for pair in listOfPairs:
		if(checkIfContained(pair) == True):
			totalPairsContained += 1
	return totalPairsContained

def checkIfPairsOverlap(pair):
	pairList = pair.split(',')
	listOne = pairList[0]
	listOneFElem = int(listOne.split('-')[0])
	listOneLElem = int(int(listOne.split('-')[1]))
	listTwo = pairList[1]
	listTwoFElem = int(listTwo.split('-')[0])
	listTwoLElem = int(int(listTwo.split('-')[1]))

	setOne = set(range(listOneFElem,listOneLElem + 1))
	setTwo = set(range(listTwoFElem,listTwoLElem + 1))
	if(set(setOne) & set(setTwo)):
		return True
	else:
	    return False


def overLapingCount(content):
	listOfPairs = toPairList(content)
	totalOverlapingPairs = 0
	for pair in listOfPairs:
		if(checkIfPairsOverlap(pair) == True):
			totalOverlapingPairs += 1
	return totalOverlapingPairs

x = containedCount(content)
y = overLapingCount(content)
print(y)