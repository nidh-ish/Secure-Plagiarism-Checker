def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def apply_discount(total, discount_percent):
    discount_amount = total * (discount_percent / 100)
    discounted_total = total - discount_amount
    return discounted_total

def main():
    cart = [
        {'name': 'item1', 'price': 10, 'quantity': 2},
        {'name': 'item2', 'price': 20, 'quantity': 1},
        {'name': 'item3', 'price': 5, 'quantity': 3}
    ]

    subtotal = calculate_total(cart)
    discounted_total = apply_discount(subtotal, 10)

    print(f"Subtotal: ${subtotal}")
    print(f"Discounted Total: ${discounted_total}")

from collections import defaultdict
import heapq

class Graph:
 
    # Constructor
    def __init__(self):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
    
    
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
    
    def shortestPath(self, src: int):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
 
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
 
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
 
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
 
        # Print shortest distances stored in dist[]
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
        
    def MinDistance(self, dist, Blackened):
        min = float("Inf")
        for v in range(len(dist)):
            if not Blackened[v] and dist[v]<min:
                min = dist[v]
                Min_index = v
        return float("Inf") if min == float("Inf") else Min_index

    def Dijkstra(self, Graph, _s, _d):
        row = len(Graph)
        col = len(Graph[0])
        dist = [float("Inf")] * row
        Blackened =[0] * row
        pathlength =[0] * row
        parent = [-1] * row
        dist[_s]= 0
        for count in range(row-1):
            u = self.MinDistance(dist, Blackened)
    
            # if MinDistance() returns INFINITY, then the graph is not
            # connected and we have traversed all of the vertices in the
            # connected component of the source vertex, so it can reduce
            # the time complexity sometimes
            # In a directed graph, it means that the source vertex
            # is not a root
            if u == float("Inf"):
                break
            else:
    
                # Mark the vertex as Blackened
                Blackened[u]= 1
            for v in range(row):
                if Blackened[v]== 0 and Graph[u][v] and dist[u]+Graph[u][v]<dist[v]:
                    parent[v]= u
                    pathlength[v]= pathlength[parent[v]]+1
                    dist[v]= dist[u]+Graph[u][v]
                elif Blackened[v]== 0 and Graph[u][v] and dist[u]+Graph[u][v]== dist[v] and pathlength[u]+1<pathlength[v]:
                    parent[v]= u
                    pathlength[v] = pathlength[u] + 1