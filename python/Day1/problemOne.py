f = open("inputOne.txt", "r")
info = f.read()

def maxCalories(info):
	# transform info to list of total calories per elf
	totalCaloriesPerElfList = fromInputToTotalsList(info)
	return max(totalCaloriesPerElfList)


def fromInputToTotalsList(info):
	mylist = info.split('\n\n')
	res = []
	sumRes = []
	for i in mylist:
		res.append(i.split('\n'))

	for i in res:
		#remove empty string in list
		i = list(filter(None, i))
		#get sum and convert list of string to list of int
		sumRes.append(sum([int(j) for j in i]))
	return sumRes

result = maxCalories(info)
sortedResult = sorted(fromInputToTotalsList(info))

print(result)
print(sum(sortedResult[-3:]))