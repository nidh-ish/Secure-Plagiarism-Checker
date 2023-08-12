def calculate_final_amount(products):
    total_amount = 0
    for product in products:
        total_amount += product['price'] * product['quantity']
    return total_amount

def apply_special_discount(amount, discount_percentage):
    discount = amount * (discount_percentage / 100)
    final_amount = amount - discount
    return final_amount

def main():
    items = [
        {'name': 'product1', 'price': 12, 'quantity': 3},
        {'name': 'product2', 'price': 18, 'quantity': 2},
        {'name': 'product3', 'price': 8, 'quantity': 4}
    ]

    total_amount = calculate_final_amount(items)
    final_amount = apply_special_discount(total_amount, 15)

    print(f"Total Amount: ${total_amount}")
    print(f"Final Amount after Discount: ${final_amount}")

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self, start):
        visited = [False] * self.V
        queue = []
        queue.append(start)
        visited[start] = True
        
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)
                
    def dfs(self, start):
        visited = [False] * self.V
        self.dfs_util(start, visited)
        
    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
                
        stack.insert(0, vertex)
        
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
                
        print(stack)
        
    def dijkstra(self, start):
        distance = [float("inf")] * self.V
        distance[start] = 0
        visited = [False] * self.V
        
        for _ in range(self.V):
            u = self.min_distance(distance, visited)
            visited[u] = True
            
            for v, weight in self.graph[u]:
                if not visited[v] and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
        
        print("Vertex\tDistance from Source")
        for i in range(self.V):
            print(f"{i}\t{distance[i]}")
            
    def min_distance(self, distance, visited):
        min_dist = float("inf")
        min_index = -1
        
        for v in range(self.V):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v
        
        return min_index
        


# Example usage
from collections import defaultdict

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(4, 5)

print("Breadth-First Search:")
g.bfs(0)
print("\nDepth-First Search:")
g.dfs(0)
print("\nTopological Sort:")
g.topological_sort()

# Dijkstra's shortest path algorithm
g = Graph(5)
g.add_edge(0, [(1, 9), (2, 6)])
g.add_edge(1, [(3, 3)])
g.add_edge(2, [(1, 2), (3, 5)])
g.add_edge(3, [(4, 2)])
g.add_edge(4, [])

print("\nDijkstra's Shortest Path Algorithm:")
g.dijkstra(0)