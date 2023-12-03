
engine = []
ty = []

dx = [1 , -1  , 1 , -1 , 1 , -1 ,0 , 0]
dy = [0 ,  0  , -1 , 1 , 1 , -1 ,1 ,-1]
def updateGears(x , y , n , m ):
	possibleNeighbours = []
	for i in range(0 , 8):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >=n or nx < 0 or ny>=m or ny < 0:
			continue
		possibleNeighbours.append([nx , ny])
	return possibleNeighbours

with open('puzzle3.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			engine.append([x for x in line[:-1]])
		else:
			engine.append([x for x in line])


ans = 0
n = len(engine)
m = len(engine[0])
ty= [[] for i in range(0 , n*m + 90)]
for i in range(0 , n):
	cur_sum = 0
	neighbours = []
	for j in range(0 , m):
		if engine[i][j]>='0' and engine[i][j]<='9':
			cur_sum = cur_sum*10 + ord(engine[i][j])-ord('0')
			thisCellneighbours = updateGears(i , j , n , m)
			neighbours+=thisCellneighbours
		else:
			uniqueneighbours  = set()
			for [x ,y] in neighbours:
				if x*m + y in uniqueneighbours:
					continue
				uniqueneighbours.add(x*m +y)
				ty[x*m + y].append(cur_sum)
			cur_sum = 0
			neighbours = []
	if cur_sum>0:
		uniqueneighbours = set()
		for [x , y] in neighbours:
			if x*m + y in uniqueneighbours:
				continue
			uniqueneighbours.add(x*m + y)
			ty[x*m +y].append(cur_sum)
		cur_sum = 0


ans = 0
for i in range(0 , n):
	for j in range(0 , m):
		if engine[i][j]=='*' and len(ty[i*m + j])==2:
			ans = ans + ty[i*m + j][0]*ty[i*m + j][1]


print(ans)