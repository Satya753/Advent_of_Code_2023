
sequence = []

with open('puzzle15b.txt' , 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[-1]=='\n':
            line = line[:-1]
        sequence=line.split(',')




ans = 0
boxes = [[] for i in range(0 , 256)]
for s in sequence:
    label = ''
    remove =False
    focal_lens = 0
    if s[-1]=='-':
        label = s[:-1]
        remove = True
    else:
        label = s.split('=')[0]
        focal_lens  = s.split('=')[1]

    box = 0
    for i in range(0 , len(label)):
        box = (box%256 + ord(label[i]))*17
        box = box%256
    if remove:
        for i in range(0 , len(boxes[box])):
            if boxes[box][i][0]==label:
                boxes[box].pop(i)
                break
    else:
        replace = False
        for i in range(0  , len(boxes[box])):
            if boxes[box][i][0]==label:
                boxes[box].pop(i)
                boxes[box].insert(i , [label , int(focal_lens)])
                replace = True
                break

        if replace==False:
            boxes[box].append([label , int(focal_lens)])

focussing_power =0
for i in range(0 , 256):
    for j in range(0 , len(boxes[i])):
        ans = ans + (i + 1)*(j + 1)*(boxes[i][j][1])
print(ans)


