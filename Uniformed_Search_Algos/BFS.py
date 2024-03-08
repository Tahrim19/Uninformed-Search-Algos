# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# making list for visited nodes and queue:
visited = set() # using sets so that no duplication 
queue = []

# function for BFS:
def BFS(graph , start_value , search_value , visited , queue):
    # base check to see if the start and search values exist in graph or not
    if start_value not in graph or search_value not in graph:
        return False
    
    queue.append(start_value)
    while queue:
        vertex = queue.pop(0)
        if vertex == search_value:
            return True
        if vertex not in visited:
            visited.add(vertex) # adds single value to a list (sets doesnt have append function)
            queue.extend(graph[vertex]) # extend adds more than one iterable value to a list
    return False
            
    

# main code: 
# start_value = input("Enter the start value: ").upper()
# print(start_value)
# search_value = input("Enter the search value: ").upper()
# print(search_value)

# result = BFS(graph, start_value, search_value, visited, queue)

# if result:
#     print(f"{search_value} is found starting from {start_value}.")
# else:
#     print(f"{search_value} is not found starting from {start_value}.")