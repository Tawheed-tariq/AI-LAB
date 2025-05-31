#BFS
import queue
def BFS(graph, start):
    visited = []
    q = queue.Queue()
    q.put(start)
    visited.append(start)
    while not q.empty():
        node = q.get()
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.put(neighbour)
    return visited

#DFS
def DFS(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node)
            for neighbour in graph[node]:
                stack.append(neighbour)
    return visited

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS")
    print(BFS(graph, 'A'))
    # print("DFS")
    # print(DFS(graph, 'A'))