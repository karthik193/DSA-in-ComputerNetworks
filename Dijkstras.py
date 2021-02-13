import math

def getMinNode(dist , vis,n):
   N =-1
   for node in range(n):
      if(vis.get(node,True)):
         if(N == -1):
            N = node
         else :
            if(dist[N] > dist[node]):
               N = node
   return N
         
def main():
   #Dijkstra's shortest path
   #given a map of networks and their costs
   graph=  [
      [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
      [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
      [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
      [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
      [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
      [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
      [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
      [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
      [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ]
      ]
   n = len(graph)
   dist = [math.inf]*(n)
   print("Enter start of route:")
   S = int(input())
   dist[S] = 0
   vis = dict()
   while(True):
      minNode = getMinNode(dist,vis,n)
      if(minNode == -1):
         break
      vis[minNode] = False
      for child in range(n):
         if(graph[minNode][child] > 0):
            dist[child] = min(dist[child] , graph[minNode][child]+dist[minNode])
   for node in range(n):
      print(node , "dist: ",dist[node])



if __name__ == "__main__":
   main()
