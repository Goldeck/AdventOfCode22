# f = open("inputOne.txt")
f = open("exemple.txt")
content = [l.strip() for l in f.readlines() ]
#print(content)



def formatToDic(content):
	states = []
	current = {}
	for cmd in content:
		match cmd.split():
			case '$', 'cd', '/':
				current['/'] = {}
				current = current['/']
				states.append(current)
			case '$', 'cd', '..':
				current = states.pop()
			case 'dir', x:
				current[x] = {}
			case x , y:
				current[y] = x
			case '$', 'cd', x:
				states.append(current)
				current = current[x]
	print(states)
	print(current) 
				




def SumTotalSizes(content):
	root = formatToDic(content)
	#sumWeight = weight(listDir)


SumTotalSizes(content)


