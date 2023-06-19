from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
visited1 = set()

def bfs_iterative(start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited1:
            print(node, end= ' ')
            visited1.add(node)
            queue.extend(graph[node])

def dfs_iterative(start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))


snode = 'A'
dfs_iterative(snode)
print('\n-----------')
bfs_iterative(snode)