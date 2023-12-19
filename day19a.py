import re
parts = []

rules = []
startparts = False
adj = {}
acceptedParts  =set()
vis = set()
indegree ={}
# sample -  qqz ,  s>2770:qs,m<1801:hdj,R

with open('puzzle19b.txt' , 'r') as f:
    while  True:
        line = f.readline()
        if not line:
            break
        if len(line)==1:
            startparts = True
        if line[-1]=='\n':
            line = line[:-1]
        filtered = re.split(r'[{}]' , line)
        if startparts:
            parts.append(list(filter(None , filtered)))
        else:
            rules.append(list(filter(None , filtered)))




def validateExpression(part , exp):
    for p in part:
        if p[0]==exp[0]:
            cur_val = int(p[2 : len(p)])
            req_val = int(exp[2:len(exp)])
            if (exp[1]=='>'):
                return cur_val > req_val
            else:
                return cur_val < req_val
    return False


def buildAdjacencyGraph(rules):

    for rule in rules:
        nextnodes = rule[1].split(',')
        if rule[0] not in indegree:
            indegree[rule[0]]=0
        if rule[0] not in adj:
            adj[rule[0]]=[]

        for i in range(0 , len(nextnodes) - 1):
            edge = nextnodes[i].split(':')[0]
            v = nextnodes[i].split(':')[1]
            adj[rule[0]].append([v , edge])
            if v not in indegree:
                indegree[v]=0
            indegree[v]+=1
        if nextnodes[-1] not in indegree:
            indegree[nextnodes[-1]]=0
        indegree[nextnodes[-1]]+=1
        adj[rule[0]].append([nextnodes[-1] , '#'])


def dfs(part , root , adj):
    #print(root , part)
    if root=='A':
        acceptedParts.add(tuple(part))
        return
    elif root=='R':
        return

    vis.add(root)
    match = False

    for i in range(0 , len(adj[root])-1):
        if adj[root][i][0] in vis:
            continue
        if validateExpression(part , adj[root][i][1])==True:
            match= True
            dfs(part , adj[root][i][0] , adj)
            #break immediately after finding a match otherwise others condition will be evaluate
            break

    if match==False:
        dfs(part , adj[root][-1][0] , adj)
    return

buildAdjacencyGraph(rules)
root = None
for node in indegree:
    if indegree[node]==0:
        print(node)
        root = node
for part in parts:
    if not part:
        continue
    d = part[0].split(',')
    vis.clear()
    dfs(d , root , adj)
ans  = 0
for part in acceptedParts:
    for p in part:
        ans = ans + int(p[2:len(p)])
print(acceptedParts)
print(ans)

