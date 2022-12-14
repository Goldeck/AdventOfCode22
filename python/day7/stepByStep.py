xx = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

if __name__ == '__main__':
	state = []
	current = {}
	print(state)
	print(current)
	print("-----")
	# $ cd /
	current['/'] = {} 
	state.append(current)
	current = current['/']
	print(current)
	print(state)
	print("-----")
	# $ ls
	# dir a
	current["a"] = {}
	print(current)
	print(state)
	print("-----")
	# 14848514 b.txt
	current['b.txt'] = 14848514
	print(current)
	print(state)
	print("-----")
	# 8504156 c.dat
	current['c.dat'] = 8504156
	print(current)
	print(state)
	print("-----")
	# dir d
	current["d"] = {}
	print(current)
	print(state)
	print("-----")
	# $ cd a


{'/': 
	{'a': 
		{'e': 
			{'i': '584'}, 
		'f': '29116',
		'g': '2557',
		'h.lst': '62596'},
	 'b.txt': '14848514',
	 'c.dat': '8504156',
	 'd': 
	 	{'j': '4060174',
	 	 'd.log': '8033020',
	 	 'd.ext': '5626152',
	 	 'k': '7214296'
	 	 }
	}
}
print("---------------------------------")
weights = {}
print(weights)
print("------")
weights['/'] = 0
print(weights)