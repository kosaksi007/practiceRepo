# DFS algorithm in Python
import timeit


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
# def dfs(graph, root, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(root)
#     for next in set(graph[root]) - visited:
#         dfs(graph, next, visited)
#     return visited


graph = {'0': ['1', '2'],
         '1': ['0', '3', '4']}
         #
         # '2': set(['0']),
         # '3': set(['1']),
         # '4': set(['2', '3'])}

# print(timeit.timeit(dfs(graph, '0')))
n = timeit.timeit(dfs(graph,0))
print(n)