totCubes = {"green":13 , "blue":14 , "red":12}

def checkPossibility(cubes):
	for cube in cubes:
		if totCubes[cube[1]]<cube[0]:
			return False

	return True
Games = []

with open('puzzle2.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			Games.append(line[:-1])
		else:
			Games.append(line)


tot = 0
for game in Games:
	gameId = game.split(": ")[0].split(" ")
	pickCubes = game.split(": ")[1].split("; ")
	print(gameId[1])
	print(pickCubes)
	Possible = True
	for eachPick in pickCubes:
		possibleCubes = []
		for pick in eachPick.split(", "):
			possibleCubes.append([int(pick.split(" ")[0]),pick.split(" ")[1]])
		if checkPossibility(possibleCubes)==False:
			Possible =False
			break
	if Possible==True:
		tot = tot + int(gameId[1])


print(tot)