# DFS using Stack 
def dfs_stack(graph, start):
    visited = set()      
    stack = [start]      
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=" ")  
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}
print("DFS using stack:")
dfs_stack(graph, '0')