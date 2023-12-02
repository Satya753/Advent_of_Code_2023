totCubes = {"green":13 , "blue":14 , "red":12}


def findFewerCubes(cubes):
	fewCubes = {"green":0 , "blue":0 , "red":0}
	for cube in cubes:
		fewCubes[cube[1]]=max(fewCubes[cube[1]] , cube[0])
	power = 1
	print(fewCubes)
	for cube in fewCubes.values():
		power = power*cube
	return power

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


ans = 0
for game in Games:
	gameId = game.split(": ")[0].split(" ")
	pickCubes = game.split(": ")[1].split("; ")
	possibleCubes = []
	Possible = True
	for eachPick in pickCubes:
		for pick in eachPick.split(", "):
			possibleCubes.append([int(pick.split(" ")[0]),pick.split(" ")[1]])
	ans = ans + findFewerCubes(possibleCubes)


print(ans)
