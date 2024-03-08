def depth_limited_search(graph, start, goal, depth_limit):
    if start == goal:
        return [start]

    if depth_limit == 0:
        return None

    for neighbor in graph.get(start, []):
        result = depth_limited_search(graph, neighbor, goal, depth_limit - 1)
        if result is not None:
            return [start] + result

    return None

def iterative_deepening_search(graph, start, goal):
    depth_limit = 0

    while True:
        result = depth_limited_search(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

# # Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H', 'I'],
#     'E': [],
#     'F': [],
#     'G': [],
#     'H': [],
#     'I': []
# }

# start_node = 'A'
# goal_node = 'I'

# result_path = iterative_deepening_search(graph, start_node, goal_node)

# if result_path:
#     print(f"Path from {start_node} to {goal_node}: {result_path}")
# else:
#     print(f"No path found from {start_node} to {goal_node}")
