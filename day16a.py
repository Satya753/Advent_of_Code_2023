import sys
sys.setrecursionlimit(150000)

mat = []
dx = [0 , -1 , 0 , 1]
dy = [1 , 0 , -1 , 0]

with open('puzzle16b.txt' , 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[-1]=='\n':
            line = line[:-1]
        mat.append(line)


n = len(mat)
m = len(mat[0])

vis =set()
energy = [[0 for i in range(0 , m)] for i in range(0 , n)]
def checkboundary( x , y , n , m ):
    if (x < 0 or y < 0 or x>=n or y>=m):
        return False
    else:
        return True



def nextDirection(coming_from , mirror , x , y):

    if mirror=='.':
        if coming_from=='W':
            return [[x , y + 1 , 'W']]
        elif coming_from=='E':
            return [[x , y - 1 , 'E']]
        elif coming_from=='N':
            return [[x + 1 , y , 'N']]
        else:
            return [[x-1 , y , 'S']]


    elif mirror=='-':
        if coming_from=='W':
            return [[x , y + 1 , 'W']]
        elif coming_from=='E':
            return [[x , y - 1 , 'E']]
        elif coming_from=='N':
            return [[x, y - 1 , 'E'] , [x , y + 1 , 'W']]
        else:
            return [[x , y - 1 ,'E'] ,[x , y + 1 , 'W']]

    elif mirror=='|':
        if coming_from=='W':
            return [[x + 1 , y , 'N'] , [x - 1 , y , 'S']]
        elif coming_from=='E':
            return [[x + 1 , y , 'N'] , [x -1 , y , 'S']]
        elif coming_from=='N':
            return [[x + 1 , y , 'N']]
        else:
            return [[x-1 , y , 'S']]

    elif mirror=='/':
        if coming_from=='W':
            return [[x -1 , y , 'S']]
        elif coming_from=='E':
            return [[x +1 , y , 'N']]
        elif coming_from=='N':
            return [[x , y - 1 , 'E']]
        else:
            return [[x , y + 1 , 'W']]
    else:
        if coming_from=='W':
            return [[x + 1 , y , 'N']]
        elif coming_from=='E':
            return [[x - 1 , y , 'S']]
        elif coming_from=='N':
            return [[x , y + 1  , 'W']]
        else:
            return [[x , y - 1 , 'E']]



def dfs(x , y , coming_from , mat):
    global vis
    energy[x][y] = 1
    vis.add(str(x) + "#" + str(y) + "#" + str(coming_from))

    next_cell = nextDirection(coming_from , mat[x][y] , x , y)
    print(next_cell , x , y , mat[x][y] , coming_from)
    for cell in next_cell:
        if checkboundary(cell[0]  , cell[1] , len(mat) , len(mat[0]))==False:
            continue
        if  str(cell[0]) + "#" + str(cell[1]) + "#" + str(cell[2]) in vis:
            continue
        dfs(cell[0] ,cell[1] , cell[2] , mat)

dfs(0 , 0  , 'W' , mat)
ans =0
for i in range(0 , n):
    print(energy[i])
    for j in range(0 , m):
        ans = ans + energy[i][j]
print(ans)

