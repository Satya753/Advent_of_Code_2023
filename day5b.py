# Get your file input
seeds = []
cnt = 0
interval = [[] for i in range(0 , 7)]
with open('puzzle5d.txt' , 'r') as f:
	while True:
		line  = f.readline()
		if cnt==0:
			seeds=line[:-1].split(": ")[1].split(" ")
			cnt = 1
		else:
			for i in range(0 , 7):
				line = f.readline()
				while True:
					if not line.strip():
						break
					line = line[:-1]
					interval[i].append(line.split(" "))
					line = f.readline()
			break




location = [[]]
for s in range(0 , len(seeds) , 2):
	reachable =[[int(seeds[s]) , int(seeds[s]) + int(seeds[s + 1]) - 1]]
	print(reachable)
	for i in range(0 , len(interval)):
		nextreachable = []
		for r in reachable:
			found = False
			dt = []
			# Find overlapping intervals with this seed
			for k in range(1 , len(interval[i])):
				source = int(interval[i][k][1])
				destination = int(interval[i][k][1])+int(interval[i][k][2])-1
				mxd = int(interval[i][k][0])-source
				if min(destination , r[1]) - max(source , r[0])>=0:
					found = True
					dt.append([max(source , r[0]) , min(destination , r[1]) , mxd])
			st = r[0]
			dt.sort()
			nextreachable.sort()
			# Find remaining seeds which couldn't be found
			for n in dt:
				nextreachable.append([n[0] + n[2] , n[1] + n[2]])
				if st < n[0]:
					nextreachable.append([st , n[0] - 1])
				st = n[1] + 1
			if nextreachable and st < r[1]:
				nextreachable.append([st , r[1]])

			if not found:
				nextreachable.append(r)
		reachable = list(nextreachable)
	location = location  + reachable
ans = float('inf')
print(location)
for l in location:
	if not l:
		continue
	ans = min(ans , l[0])
print(ans)

