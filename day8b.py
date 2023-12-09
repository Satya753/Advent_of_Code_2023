#path = "LLRRRLLRRRLRRRLRLRLLRRLRRRLLLRLRRRLRRRLRLLRRLRRRLLRRLRRLRLRRRLRRLLRLRRLRRRLRRLLRRRLRLLLRLRRRLRRLLLLRRRLRRRLRRRLRLRRLRRLRLRRLLRLLRRRLRRLRLLRRLRRLLRLLRLRRRLRLRLRRRLRRLLLRLRRRLLRLLRRRLRLRLRRRLLRLLLLRRRLRRRLRLRRRLRRLRRLLRLRLRRRLRRRLRLRRLLLLRLRRRLRRRLRLRRRLRLRRLRLRRRR"
path = "LR"
node_label = {}
edges = []
def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


with open('puzzle8a.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[:-1]=='\n':
			line  = line[:-1]
		edges.append(line.split(" "))

adj = [[] for i in range(0 , 10000)]
cnt = 0
all_root=[]
all_destination =set() 
for edge in edges:
	par = edge[0]
	left_child = edge[2][1:4]
	right_child = edge[3][0:3]

	if par not in node_label:
		node_label[par]=cnt
		cnt+=1
	if left_child not in node_label:
		node_label[left_child]=cnt
		cnt+=1
	if right_child not in node_label:
		node_label[right_child]=cnt
		cnt+=1
	if par[2]=='A':
		all_root.append(node_label[par])

	if left_child[2]=='Z':
		all_destination.add(node_label[left_child])
	if right_child[2]=='Z':
		all_destination.add(node_label[right_child])
	if par[2]=='Z':
		all_destination.add(node_label[par])

	adj[node_label[par]].append(node_label[left_child])
	adj[node_label[par]].append(node_label[right_child])


n = len(path)
idx = 0
steps=0

dis = [float('inf') for i in range(0 , cnt + 3)]
vis = [set() for i in range(0 ,6)]
start_cycle = [float('inf') for i in range(0 , 8)]
paths = [[] for i in range(0 , 6)]

while steps  < 100000:

	tot_destination = 0
	next_node = all_root

	for i in range(0 , len(all_root)):
		if path[idx%n]=='L':
			next_node[i] = adj[next_node[i]][0]
		else:
			next_node[i] = adj[next_node[i]][1]
		if next_node[i] in all_destination:
			paths[i].append(steps + 1)
			tot_destination+=1
	steps+=1
	if tot_destination==len(all_root):
		break
	all_root = next_node
	idx+=1
	idx%=n

length_of_cycle = []
for path in paths:
	print(path)
	if not path:
		break
	length_of_cycle.append(path[1] - path[0])

print(length_of_cycle)
lcm = length_of_cycle[0] 
for i in range( 1, len(length_of_cycle)):
	g = getGCD(length_of_cycle[i] , lcm)
	lcm = lcm*(length_of_cycle[i])//(g)


intersections_points = {}
print(lcm)


#
#[20777, 41554, 62331, 83108]
#[19199, 38398, 57597, 76796, 95995]
#[18673, 37346, 56019, 74692, 93365]
#[16043, 32086, 48129, 64172, 80215, 96258]
#[12361, 24722, 37083, 49444, 61805, 74166, 86527, 98888]
#[15517, 31034, 46551, 62068, 77585, 93102]

#[20777, 41554, 62331, 83108]
#[19199, 38398, 57597, 76796, 95995]
#[18673, 37346, 56019, 74692, 93365]
#[16043, 32086, 48129, 64172, 80215, 96258]
#[12361, 24722, 37083, 49444, 61805, 74166, 86527, 98888]
#[15517, 31034, 46551, 62068, 77585, 93102]