import sys
sys.setrecursionlimit(20000000)
maze = []
connect = {'|' : [[-1 , 0] , [1 ,0]] , '-':[[0 , 1] , [0 , -1]] , 'L' : [[-1 , 0] , [0 , 1]] , 'J': [[-1 , 0] , [0 , -1]] , '7':[[0 , -1] , [1 , 0]] , 'F':[[0, 1] , [1 , 0]]}
opposite ={'|':['|' ,'L','J' 'S'] , '-':['-','7','J' ,'S'] , 'L':['J','-','|' , '7' , 'S'] , 'J':['L' , '|' ,'F', '-','S'] , 'F':['7','J' ,'-' ,'|' , 'S'] , '7':['F', 'L', '|' , 'S']}
with open('puzzle10b.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			line = line[:-1]
		maze.append(line)



mx_length  = 0
m = len(maze[0])
n = len(maze)
vis = [0 for i  in range(0 , n*m  + m + n +19999)]
dis = [-1 for i in range(0 , n*m + m + n + 199999)]
cycles = [[0 for i in range(0 , m)] for i in range(0 , n )]



edges = [[] for i in range(0 , n*m + m + n + 19999)]
start = 0
for i in range(0  ,  n):
	for j in range(0 , len(maze[i])):
		if maze[i][j]=='S':
			start = i*m + j
			continue
		if maze[i][j] not in connect:
			continue

		for [dx , dy] in connect[maze[i][j]]:
			nx = i + dx
			ny = j + dy
			if nx<0 or ny<0 or nx>=n or ny>=m:
				continue

			edges[i*m + j].append(nx*m + ny)
			if maze[nx][ny] in opposite[maze[i][j]]:
				edges[nx*m + ny].append(i*m + j)

#dfs(start , -1 , edges , start , n , m)
print(edges[start] , start , m)

q = [[start , 0]]
dis[start] = 0
cnt = 0
while len(q)>0:
	now = q.pop(0)
	if vis[now[0]]==1:
		continue
	vis[now[0]]=1
	mx_length = max(mx_length , now[1])

	cycles[now[0]//m][now[0]%m]=now[1]
	for node in edges[now[0]]:
		dis[node] = dis[now[0]] + 1
		q.append([node , dis[node]])
#print(cycles)
#for i in range(0 , len(cycles)):
#	print(" ".join([str(d) for d in cycles[i]]))
print(mx_length)
