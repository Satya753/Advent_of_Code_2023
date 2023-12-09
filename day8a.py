path = "LLRRRLLRRRLRRRLRLRLLRRLRRRLLLRLRRRLRRRLRLLRRLRRRLLRRLRRLRLRRRLRRLLRLRRLRRRLRRLLRRRLRLLLRLRRRLRRLLLLRRRLRRRLRRRLRLRRLRRLRLRRLLRLLRRRLRRLRLLRRLRRLLRLLRLRRRLRLRLRRRLRRLLLRLRRRLLRLLRRRLRLRLRRRLLRLLLLRRRLRRRLRLRRRLRRLRRLLRLRLRRRLRRRLRLRRLLLLRLRRRLRRRLRLRRRLRLRRLRLRRRR"
node_label = {}
edges = []
with open('puzzle8b.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[:-1]=='\n':
			line  = line[:-1]
		edges.append(line.split(" "))

adj = [[] for i in range(0 , 10000)]
cnt = 0
for edge in edges:
	par = edge[0]
	left_child = edge[2][1:4]
	right_child = edge[3][0:3]
	print(par , left_child , right_child , edge[2])

	if par not in node_label:
		node_label[par]=cnt
		cnt+=1
	if left_child not in node_label:
		node_label[left_child]=cnt
		cnt+=1
	if right_child not in node_label:
		node_label[right_child]=cnt
		cnt+=1

	adj[node_label[par]].append(node_label[left_child])
	adj[node_label[par]].append(node_label[right_child])


print(node_label)
root = node_label['AAA']
end = node_label['ZZZ']
n = len(path)
idx = 0
steps=0

dis = [float('inf') for i in range(0 , cnt + 3)]
vis = [0 for i in range(0 , cnt + 3)]
queue = []
queue.append([root , idx])
dis[root] = 0

while vis[end]==0:

	vis[root]=1

	if path[idx%n]=='L':
		print(adj[root] , root)
		next_node = adj[root][0]

		dis[next_node] = min(dis[next_node] , dis[root]  + 1)
		root= next_node
	else:
		next_node = adj[root][1]
		dis[next_node] = min(dis[next_node] , dis[root]  + 1)
		root= next_node
	idx+=1
	steps+=1
	idx%=n

print(steps-1)