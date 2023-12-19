import sys
import heapq
from functools import cmp_to_key

sys.setrecursionlimit(150000)

island = []
dx = [-1 , 0 , 1 , 0]
dy = [0 , 1 ,  0 , -1]
with open('puzzle17b.txt' , 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[-1]=='\n':
            line = line[:-1]

        island.append(line)


n = len(island)
m = len(island[0])


def checkboundary(x  , y , n , m):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    else:
        return True


def mycmp(a,b):

    if (a[0] == b[0]):
        if (a[1] != b[1]):
            return (a[1] - b[1])
        else:
            return (a[2] - b[2])
    return (a[0] - b[0])

def shortestPath(island):

    n = len(island)
    m = len(island[0])
    vis = {}
    dis = [[float('inf') for i in range(0 , m)] for i in range(0 , n)]

    pq = []
    heapq.heappush(pq , [0 , 0 , 0 , -1 , -1])
    dis[0][0] = 0

    ans = float('inf')
    while (len(pq) > 0):
        now = heapq.heappop(pq)
        x = now[1]
        y = now[2]
        cur_dir = now[3]
        cnt_dir = now[4]
        if (x==n-1 and y==m-1):
            ans = min(ans , now[0])
            print(now)
        if (x , y , cur_dir , cnt_dir) in vis:
            continue
        vis[(x , y, cur_dir , cnt_dir)]=now[0]
        for i in range(0 , 4):
            nx = x+ dx[i]
            ny = y +dy[i]
            if checkboundary(nx , ny , n , m)==False:
                continue
            next_dir =1
            if cur_dir==i:
                next_dir = cnt_dir + 1
            dot = dx[i]*dx[cur_dir] + dy[i]*dy[cur_dir]
            if next_dir>3 or dot==-1:
                print(next_dir , i , cur_dir , dot)
                continue
            heapq.heappush(pq ,[now[0] + int(island[nx][ny]) , nx , ny, i , next_dir])

    return ans


print(shortestPath(island))


