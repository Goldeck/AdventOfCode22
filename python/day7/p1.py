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
				states.append(current)
				current = current['/']
			case '$', 'ls':
				continue
			case '$', 'cd', '..':
				current = states.pop()
			case 'dir', x:
				current[x] = {}
			case x , y:
				current[y] = int(x)
			case '$', 'cd', x:
				states.append(current)
				current = current[x]
	return states[0]
				

def weight(dic):
	weights = {}
	currentWeights = 0
	for key,value in dic.items():
		print(key)
		print(value)
		if isinstance(value, int):
			print("wazzza")
			weight += dic[a]
		else:
			print("oppsie")
			print(value)
			weight(value)




def SumTotalSizes(content):
	root = formatToDic(content)
	#print(root)
	sumWeight = weight(root)


SumTotalSizes(content)


