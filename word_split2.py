space = " "

sample = open("sec.txt", "r+")

rawtext = sample.read()

rawtext = rawtext.replace(',', '')

rawlist = rawtext.split("\n")

for i in range(len(rawlist) - 1):

	temp = rawlist[i].split()
		
	temp2 = space.join(temp[1::])

	print('"' + str(temp2) + '"' + ',')





