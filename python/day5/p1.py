file = open("inputOne.txt")
content = file.read()

def reverse_lst_2(a_lst):
   return a_lst[::-1]

def fromContentToCratesPositions(content):
	cratesParts = content.split('\n\n')
	cratesPos = cratesParts[0].replace('    ',' [0]')
	cratesPos = cratesPos.split('\n')
	numberOfCol = int(cratesPos[-1].strip()[-1])
	topToBottom = cratesPos[0:numberOfCol -1]
	bottomToTop = reverse_lst_2(topToBottom)

	listOfStacks = []
	stack = list()
	rangeOfStacks = range(1,numberOfCol + 1 )
	for i in rangeOfStacks:
		listOfStacks.append(list())
	# boucle sur cahaque niveau
	for line in bottomToTop:
		purifiedLine = line.replace('[', '').replace(']', '').replace(' ', '')
		cpt = 0
		# boucle sur conteneur d'une ligne
		for i in purifiedLine:
			if(i != '0'):
				listOfStacks[cpt].append(i)
			cpt += 1
	return listOfStacks

def moveCrate(initialCratesPosition,move):
	finalCratesPositions = initialCratesPosition
	NumberToMove = int(move[0])
	fromColone = int(move[1]) - 1
	toColone = int(move[2]) - 1
	#print( 'move ' + str(NumberToMove) + ' fromColone ' + str(fromColone) + ' to ' + str(toColone))
	elmsToMove = reverse_lst_2(initialCratesPosition[fromColone][-NumberToMove:])
	finalCratesPositions[toColone].extend(elmsToMove)
	
	while NumberToMove > 0:
		finalCratesPositions[fromColone].pop()
		NumberToMove -= 1
	print(finalCratesPositions)
	return finalCratesPositions

def moveCrate2(initialCratesPosition,move):
	finalCratesPositions = initialCratesPosition
	NumberToMove = int(move[0])
	fromColone = int(move[1]) - 1
	toColone = int(move[2]) - 1
	#print( 'move ' + str(NumberToMove) + ' fromColone ' + str(fromColone) + ' to ' + str(toColone))
	elmsToMove = initialCratesPosition[fromColone][-NumberToMove:]
	finalCratesPositions[toColone].extend(elmsToMove)
	
	while NumberToMove > 0:
		finalCratesPositions[fromColone].pop()
		NumberToMove -= 1
	print(finalCratesPositions)
	return finalCratesPositions


def moveCrates(initialCratesPosition, moves):
	for move in moves:
		newCratesPos = moveCrate2(initialCratesPosition,move)
	return newCratesPos


def contentToMoves(content):
	cratesParts = content.split('\n\n')
	moves = cratesParts[1].strip().split('\n')
	finalMoves = []
	for move in moves:
		moveList = move.split(' ')
		finalMoves.append((moveList[1],moveList[3], moveList[-1]))
	return finalMoves

def finalTopCrates(content):
	# ListOfStacks
	initialCratesPosition = fromContentToCratesPositions(content)
	moves = contentToMoves(content)
	finalCrates = moveCrates(initialCratesPosition, moves)
	return finalCrates



def finalTopCratesString(content):
	finalCratesPositions = finalTopCrates(content)
	topCrateMessage = ''
	for stack in finalCratesPositions:
		topCrateMessage += stack[-1]
	return topCrateMessage

x = finalTopCratesString(content)
print(x)