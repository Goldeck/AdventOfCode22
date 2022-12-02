f = open("inputOne.txt", "r")
content = f.read()


#print(content)


def totalScore(content):
	mylist = contentToList(content)
	totalScore = 0
	for i in mylist:
		totalScore += score2(i)
	print(totalScore)
	return totalScore

def contentToList(content):
	mylist = content.split('\n')
	mylist = list(filter(None, mylist))
	return mylist

#rules:
# socore shape + score match result
#A=X = Rock = 1, B=Y = Paper = 2, C=Z = Scissors = 3 ||| lose = 0 , draw = 3, win = 6
#
#

def fromLigneToList2(line):
	mylist = line.split(" ")
	return mylist

def fromLigneToList(line):
	line = line.replace("X","A") #rock
	line = line.replace("Y","B") #paper
	line = line.replace("Z","C") #scissor
	mylist = line.split(" ")
	return mylist

def score(round):
	mylist = fromLigneToList(round)
	score = 0;

	if( mylist[0] == mylist[1] ):
		score += 3
	elif((mylist[0] =="A" and mylist[1] == "B") or (mylist[0] == "B" and mylist[1] == "C") or (mylist[0] == "C" and mylist[1] == "A") ):
		score += 6
	
	if(mylist[1] == "A"):
		score += 1
	elif(mylist[1] == "B"):
		score += 2
	elif(mylist[1] == "C"):
		score += 3
	return score
# X : lose / Y : draw / Z : win

def score2(round):
	mylist = fromLigneToList2(round)
	score = 0
	# draw
	if(mylist[1] == "Y"):
		match mylist[0]:
			case "A":
				score += 1
			case "B":
				score += 2
			case "C":
				score += 3
	#Win
	elif(mylist[1] == "Z"):
		match mylist[0]:
			case "A":
				score += 2
			case "B":
				score += 3
			case "C":
				score += 1
	#Lose
	elif(mylist[1] == "X"):
		match mylist[0]:
			case "A":
				score += 3
			case "B":
				score += 1
			case "C":
				score += 2

	match mylist[1]:
		case "X":
			score += 0
		case "Y":
			score += 3
		case "Z":
			score += 6
	print(score)
	return score





totalScore(content)
