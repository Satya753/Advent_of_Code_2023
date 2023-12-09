
histories = []
with open('puzzle9b.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			line=line[:-1]
		histories.append(line.split(" "))




def extrapolateHistory(history):
	n = len(history)
	mat = [[-1  for i in range(0 , n + 2)] for  i in range(0 , n + 2)]
	idx = 0

	for i in range(0 , n ):
		mat[0][i] = history[i]

	for i in range(1 , n):
		for j in range(0 , n - i):
			mat[i][j] = mat[i-1][j + 1] - mat[i-1][j]
		zeros = 0
		for j in range(0 , n -i):
			if mat[i][j]==0:
				zeros+=1
		if (zeros==n-i):
			idx = i
			break
	ans = 0
	print(idx)
	mat[idx][n-idx]=0

	for i in range(idx-1 , -1 , -1):
		mat[i][n-i]  = mat[i + 1][n-i - 1] + mat[i][n-i-1]

	return mat[0][n]

ans = 0
for history in histories:
	h = [int(d) for d in history] 
	extrapolate = extrapolateHistory(h)
	ans =ans+ extrapolate
	print(extrapolate)
print(ans)
