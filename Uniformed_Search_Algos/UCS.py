def UCS(graph, start, goal):
    visited = set() # set to keep track of visited nodes
    priority_queue = [(0, start, [])]  # (cumulative cost, current node, path)
    
    while priority_queue:
        priority_queue.sort()  # Sort the priority queue based on cumulative cost
        cost, current, path = priority_queue.pop(0)
        
        if current in visited:
            continue
        
        visited.add(current)
        path = path + [(current, cost)]
        
        if current == goal:
            return path
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            if neighbor not in visited:
                priority_queue.append((cost + edge_cost, neighbor, path))
    
    return None  # No path found


    
# Example graph
# graph = {
#     'A': {'B': 6, 'C': 3},
#     'B': {'C': 1, 'D': 2},
#     'C': {'B': 4, 'D': 8 , 'E':2},
#     'D': {'E': 9},
#     'E': {'D': 7}
# }

# # Example usage
# start_node = input("Enter the start value: ").upper()
# print(start_node)
# goal_node = input("Enter the search value: ").upper()
# print(goal_node)


# result = uniform_cost_search(graph, start_node, goal_node)

# will print the optimum total cost
# if result:
#     path_nodes = [node for node, cost in result]
#     total_cost = result[-1][1]
#     print(f"Uniform Cost Search Path from {start_node} to {goal_node}: {path_nodes}, Total Cost: {total_cost}")
# else:
#     print(f"No path found from {start_node} to {goal_node}.")

