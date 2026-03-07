# BFS using QUEUE
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
    'G': [],
    'H': ['L'],
    'I': [],
    'K': ['M'],
    'L': [],
    'M': []
}
def bfs_with_list_queue(start, goal):
    visited = []
    queue = [start]  
    while queue:
        node = queue.pop(0) 
        print("Visiting:", node)
        if node == goal:
            return visited + [node]
        visited.append(node)
        for child in graph[node]:
            if child not in visited and child not in queue:
                queue.append(child)  
    return False
start = 'A'
goal = input("Enter the goal state for BFS with list queue: ")
res = bfs_with_list_queue(start, goal)
if res:
    print("Path to goal:", res)
else:
    print("Goal not found.")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
    'G': [],
    'H': ['L'],
    'I': [],
    'K': ['M'],
    'L': [],
    'M': []
}


# BFS without using QUEUE
def bfs_without_queue(start, goal):
    visited = []
    current_level = [start]  
    while current_level:
        next_level = []
        for node in current_level:
            print("Visiting:", node)
            if node == goal:
                return visited + [node]
            visited.append(node)
            for child in graph[node]:
                if child not in visited and child not in next_level:
                    next_level.append(child)
        current_level = next_level
    return False
start = 'A'
goal = input("Enter the goal state for BFS without queue: ")
res = bfs_without_queue(start, goal)
if res:
    print("Path to goal:", res)
else:
    print("Goal not found.")