import sys

graph = {}
city1=sys.argv[2]
city2=sys.argv[3]
f=open(sys.argv[1], 'r')
data=f.read()
holder=data.split()
a=0
b=1
while b < (len(holder)-3):
    graph.setdefault(holder[a], []).append(holder[b])
    graph.setdefault(holder[b], []).append(holder[a])
    a=a+3
    b=b+3

# to obtain the shortest path between 2 nodes of graph using BFS
def bfs(graph, start, goal):
    # keep trail of examined nodes
    examined = []
    # keep trail of all the paths to be examined
    que = [[start]]
 
    # for start node equal to goal node
    if start == goal:
        print "Start = goal"
 
    # for examining all possible trails
    while que:
        # pop the first trail from the queue
        trail = que.pop(0)
        # obtain the last node from the trail
        node = trail[-1]
        if node not in examined:
            neighbours = graph[node]
            # parse through each neighbouring node, create a new trail and
            # push it into the queue
            for neighbour in neighbours:
                new_trail = list(trail)
                new_trail.append(neighbour)
                que.append(new_trail)
                # return trail if neighbouring node is goal node
                if neighbour == goal:
                    return new_trail
 
            # mark node as examined
            examined.append(node)
            
 
 
path = bfs(graph, city1, city2)
length=(len(holder)-3)
q=0
if path != None:
    q=(len(path)-1)
    print "route :"
d=0
e=1
f=2
distance=0
for b in range(0,q,1):
    if city1 == city2:
        break
    for a in range(0,length,1):
        if path[b] == holder[d] and path[b+1] == holder[e]:
            print holder[d],"to",holder[e],",",holder[f],"km"
            distance = distance + int(holder[f])
        elif path[b] == holder[e] and path[b+1] == holder[d]:
            print holder[e],"to",holder[d],",",holder[f],"km"
            distance = distance + int(holder[f])
        d=d+3
        e=e+3
        f=f+3
        if f > length:
            break
    d=0
    e=1
    f=2
if distance == 0:
    print "distance : infinity"
    print "route :\nnone"
else :
    print "distance :",distance,"km"
