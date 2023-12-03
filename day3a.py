
engine = []

dx = [1 , -1  , 1 , -1 , 1 , -1]
dy = [0 ,  0  , -1 , 1 , 1 , -1]
def checkValidPart(x ,y, n , m , cur_sum ):
	for i in range(0 , 6):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >=n or nx <0 or ny>=m or ny < 0:
			continue
		if engine[nx][ny]!='.':
			return True
	return False

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
for i in range(0 , n):
	cur_sum = 0
	validPart  = False
	for j in range(0 , m):
		if (engine[i][j]<'0' or engine[i][j]>'9'):
			if engine[i][j]!='.':
				validPart = True
			if validPart:
				print(cur_sum)
				ans = ans + cur_sum
			if engine[i][j]!='.':
				validPart = True
			else:
				validPart = False
			cur_sum = 0
		else:
			cur_sum = cur_sum*10 + (ord(engine[i][j]) - ord('0'))
			if checkValidPart(i , j , n , m , cur_sum):
				validPart = True
	if cur_sum>0 and validPart:
		ans = ans + cur_sum


print(ans)
