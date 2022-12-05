import string
from itertools import islice

file = open("inputOne.txt")
content = file.read()
#print(content)

# list 
# trouvez l'intru
# scorer total
def evenOrOdd(string):
  if len(string) % 2 == 0:
     return "Even"
  else:
     return "Odd"

def findWrongItem(runSack):
	Leng = len(runSack)
	halfLeng = Leng//2

	compOne = runSack[:halfLeng]
	compTwo = runSack[halfLeng:]
	commonElemSet = set(compOne).intersection(set(compTwo))

	return list(commonElemSet)[0]

#create dic with lettre -> value
def score(elem):
	numList = list(range(1,53))
	lettreList = list(string.ascii_lowercase) + list(string.ascii_uppercase)
	res = {}
	for key in lettreList:
	    for value in numList:
	        res[key] = value
	        numList.remove(value)
	        break
	return res[elem]

def prioritiesSum(content):
	runSackList = list(filter(None,content.split("\n")))
	wrongItem = []
	for elem in runSackList:
		wrongItem.append(findWrongItem(elem))
	totalScore = 0
	for elem in wrongItem:
		totalScore += score(elem)
	print(totalScore)

def listOfGroups(content):
	runSackList = list(filter(None,content.split("\n")))
	groups= []
	start = 0
	end = len(runSackList)
	step = 3
	for i in range(start, end, step):
	    x = i
	    groups.append(list(runSackList[x:x+step]))
	return groups

def findCommonItem(group):
	commonElemSet = set(group[0]) & set(group[1]) & set(group[2])
	print(list(commonElemSet)[0])
	return list(commonElemSet)[0]


def badgeSum(content):
	groups = listOfGroups(content);
	totalScore = 0
	for group in groups:
		item = findCommonItem(group)
		totalScore += score(item)

	return totalScore


x = badgeSum(content)
print(x)
#prioritiesSum(content)

