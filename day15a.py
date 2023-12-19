
sequence = []

with open('puzzle15a.txt' , 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[-1]=='\n':
            line = line[:-1]
        sequence=line.split(',')


ans = 0
for s in sequence:
    cnt = 0
    for i in range(0 , len(s)):
        cnt = (cnt%256 + ord(s[i]))*17
        cnt = cnt%256
    print(cnt)
    ans = ans + cnt
print(ans)


