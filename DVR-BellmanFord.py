#Distance vector routing (Bellman Ford)

def shortestPaths(source_map, s):
    n = len(source_map)
    d_from_s = source_map[s]
    for i in range(n):
        if(i!=s and d_from_s[i]==0):
            d_from_s[i] = 20000000
    def newD(node):
        for i in range(n):
            if(i != node and source_map[i][node]!=0):
                if(d_from_s[i] + source_map[i][node] < d_from_s[node]):
                    d_from_s[node] = d_from_s[i] + source_map[i][node]

    for i in range(n-1):
        for j in range(n):
            if(s != j):
                newD(j)
        
    return d_from_s

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
				[4, 0, 8, 0, 0, 0, 0, 11, 0], 
				[0, 8, 0, 7, 0, 4, 0, 0, 2], 
				[0, 0, 7, 0, 9, 14, 0, 0, 0], 
				[0, 0, 0, 9, 0, 10, 0, 0, 0], 
				[0, 0, 4, 14, 10, 0, 2, 0, 0], 
				[0, 0, 0, 0, 0, 2, 0, 1, 6], 
				[8, 11, 0, 0, 0, 0, 1, 0, 7], 
				[0, 0, 2, 0, 0, 0, 6, 7, 0] ]; 
paths = shortestPaths(graph,0)
print("Shortest Paths from '0' to all vertices:")
for i in range(len(graph)):
				print("0->",i,"  =  ",paths[i],sep="")
