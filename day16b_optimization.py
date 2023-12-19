import sys
sys.setrecursionlimit(150000)

mat = []
dx = [0 , -1 , 0 , 1]
dy = [1 , 0 , -1 , 0]

with open('puzzle16a.txt' , 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[-1]=='\n':
            line = line[:-1]
        mat.append(line)


n = len(mat)
m = len(mat[0])

vis = {}
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
    if str(str(x) + "#" + str(y) + "#" + str(coming_from)) in vis:
        return vis[str(x)  + "#"  + str(y) + "#" + str(coming_from)]

    print(x , y , coming_from , mat[x][y])
    energy[x][y]+=1
    total_cells =0
    if energy[x][y]<=1:
        total_cells+=1
    vis[str(x)  + "#"  + str(y) + "#" + str(coming_from)]=1
    next_cell = nextDirection(coming_from , mat[x][y] , x , y)
    for cell in next_cell:
        if checkboundary(cell[0]  , cell[1] , len(mat) , len(mat[0]))==False:
            continue
        total_cells = total_cells + dfs(cell[0] ,cell[1] , cell[2] , mat)

    vis[str(x)  + "#"  + str(y) + "#" + str(coming_from)]  = total_cells
    return total_cells


ans =0
#Starting from top row and bottom rows
for i in range(1 , m-1):
    ans = max(ans , dfs(0 , i , 'N', mat))
    ans = max(ans , dfs(n-1,i ,'S', mat))

#Starting from left and right column

for i in range(0 , n):
    ans = max(ans , dfs(i , 0 , 'W', mat))
    ans = max(ans , dfs(i, m-1 , 'E', mat))

print(ans)

