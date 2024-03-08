# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# making list for visited nodes and stack:
visited = set() # using set so that no duplications
stack = [] 

# function for DFS:
def DFS(graph, start_value, search_value, visited, stack):
    # base check to see if the start and search values exist in graph or not
    if start_value not in graph or search_value not in graph:
        return False
    
    stack.append(start_value)
    while stack:
        vertex = stack.pop()
        if vertex == search_value:
            return True
        if vertex not in visited:
            visited.add(vertex)  # adds single value to a list (sets doesnt have append function)
            stack.extend(graph[vertex][::-1])  # Reverse the order to mimic DFS (stack behavior)
            # stack.extend(reversed(graph[vertex]))  # Reverse the order to mimic DFS (stack behavior)

    return False

# main code:
# start_value = input("Enter the start value: ").upper()
# print(start_value)
# search_value = input("Enter the search value: ").upper()
# print(search_value)

# result = DFS(graph, start_value, search_value, visited, stack)

# if result:
#     print(f"{search_value} is found starting from {start_value}.")
# else:
#     print(f"{search_value} is not found starting from {start_value}.")
