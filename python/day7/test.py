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

etats = []
en_cours = {}
en_cours["a"] = {} # dir a
en_cours["b.txt"] = 14848514 # 14848514 b.txt
en_cours["d"] = {} # dir d

# $ cd a
etats.append(en_cours)
en_cours = en_cours["a"]

# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
en_cours["e"] = {}
en_cours["f"] = 29116

# $ cd e
etats.append(en_cours)
en_cours = en_cours["e"]


# cd ..
en_cours = etats.pop()
en_cours["autre"] = 42
print(etats[0])