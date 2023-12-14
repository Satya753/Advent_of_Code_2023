
onsens = []
with open('puzzle12b.txt' , 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			line = line[:-1]
		onsens.append(line)


res = 0
mx = 0
for onsen in onsens:
	row = list(onsen.split(" ")[0])
	grp = onsen.split(" ")[1].split(',')
	unknown = []

	for i in range(0 , len(row)):
		if row[i]=='?':
			unknown.append(i)

	mx = max(mx , len(unknown))
	mask = (1<<(len(unknown)))
	ans =0
	for m in range(0 , mask):
		temp = row
		for i in range(0 , len(unknown)):
			if (m &(1<<i)):
				temp[unknown[i]]='#'
			else:
				temp[unknown[i]]='.'

		cgrps = []
		cnt =0
		for i in range(0 , len(temp)):
			if temp[i]=='#':
				cnt+=1
			else:
				if cnt>0:
					cgrps.append(cnt)
				cnt=0
		if cnt>0:
			cgrps.append(cnt)
		found  = True
		if len(grp)!=len(cgrps):
			found = False
		else:
			for i in range(0 , len(cgrps)):
				if cgrps[i]!=int(grp[i]):
					found = False
		if found:
			ans+=1
	res = res + ans
print(res)
print(mx)