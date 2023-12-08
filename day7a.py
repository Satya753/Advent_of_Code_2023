from collections import Counter
import functools

# Get your file input
cards = []
labelranks = {'A':13, 'K':12, 'Q':11, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1 , 'J':0}

def compare(a , b):
	if a[2] < b[2]:
		return 1
	elif a[2]==b[2]:
		for i in range(0 , len(a[0])):
			if labelranks[a[0][i]]>labelranks[b[0][i]]:
				return -1
			if labelranks[a[0][i]]<labelranks[b[0][i]]:
				return 1
			else:
				continue
	else:
		return -1
with open('puzzle7a.txt' , 'r') as f:
	while True:
		line  = f.readline()
		if not line:
			break
		if line[-1]=='\n':
			line = line[:-1]
		cards.append(line.split(" "))

print(cards)
print(labelranks['A'])
cardrank = []
for card in cards:
	print(card[0])
	res = dict(Counter(card[0]))
	freqi = dict(Counter(res.values()))
	ones , two , three , four , five =0 , 0 , 0 , 0 , 0
	if 2 in freqi.keys():
		two = freqi[2]
	if 1 in freqi.keys():
		ones = freqi[1]
	if 5 in res.values():
		cardrank.append([card[0] , card[1] , 7])
	elif 4 in res.values() and 1 in res.values():
		cardrank.append([card[0] , card[1] , 6])
	elif 3 in res.values() and 2 in res.values():
		cardrank.append([card[0] , card[1] , 5])
	elif 3 in res.values() and 1 in res.values():
		cardrank.append([card[0] , card[1] , 4])
	elif two==2:
		cardrank.append([card[0] , card[1] , 3])
	elif ones==5: 
		cardrank.append([card[0] , card[1] , 1])
	else:
		cardrank.append([card[0] , card[1] , 2])
cardrank = sorted(cardrank ,key=functools.cmp_to_key(compare) ,reverse = True)
ans = 0
print(cardrank)
for i in range(0 , len(cardrank)):
	ans  = ans + (i + 1)*(int(cardrank[i][1]))
print(ans)




#249355116


