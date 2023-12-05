
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


for d in interval:
	print(d)

print(seeds)

location = []
for seed in seeds:
	startpoint = int(seed)
	for i in range(0 , len(interval)):
		for k in range(1 , len(interval[i])):
			source = int(interval[i][k][1])
			destination = int(interval[i][k][1]) + int(interval[i][k][2])
			if startpoint>=source and startpoint<=destination:
				print(source ,destination, startpoint)
				startpoint = int(interval[i][k][0]) + (startpoint - source)
				break
	location.append(startpoint)
print(min(location))



