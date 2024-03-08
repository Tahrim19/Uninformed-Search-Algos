# import required library and functions
import tkinter as tk
from DFS import DFS , visited , stack  
from BFS import BFS , visited , queue 
from UCS import UCS
from IDS import iterative_deepening_search, depth_limited_search

# function to see what button is clicked so that it executes that specific function
def on_button_click(button_text):
    # user input of start node and to be searched node
    start_value = start_entry.get().upper()
    search_value = search_entry.get().upper()

    if button_text == "Depth-First Search":
        result = DFS(graph1, start_value, search_value, visited, stack)
    elif button_text == "Breadth-First Search":
        result = BFS(graph1, start_value, search_value, visited, queue) 
    elif button_text == "Uniform Cost Search":
        result = UCS(graph2, start_value, search_value)
        if result:
            path_nodes = [node for node, cost in result]
            total_cost = result[-1][1]
            result_label.config(text=f"Uniform Cost Search Path from {start_value} to {search_value}: {path_nodes}, Total Cost: {total_cost}")
            return
    elif button_text == "Iterative Deepening Search":
        result = iterative_deepening_search(graph3, start_value, search_value)
        if result:
            result_label.config(text=f"Path from {start_value} to {search_value}: {result}")
    else:
        return False    
        
    if result:
        result_label.config(text=f"{button_text}: {search_value} is found starting from {start_value}.")
    else:
        result_label.config(text=f"{button_text}: {search_value} is not found starting from {start_value}.")

# Create the main window
window = tk.Tk()
window.title("Graph Search GUI")
window.geometry("400x400")

# Create Entry widgets for user input
start_label = tk.Label(text="Enter the start value:")
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack()

search_label = tk.Label(text="Enter the search value:")
search_label.pack()

search_entry = tk.Entry(window)
search_entry.pack()

option = tk.Label(text="Choose one of the following:")
option.pack()

# Create buttons for DFS and BFS
algorithm_buttons = [
    "Depth-First Search",
    "Breadth-First Search",  
    "Random Search",
    "Uniform Cost Search",
    "Iterative Deepening Search"
]

# Create buttons dynamically
for text in algorithm_buttons:
    tk.Button(
        text=text,
        width=50,
        height=3,
        bg="light blue",
        fg="black",
        command=lambda t=text: on_button_click(t)
    ).pack()

# Create a label to display the result
result_label = tk.Label(text="")
result_label.pack()

# Add your graph, visited, and stack variables here
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph2 = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

graph3 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Start the GUI event loop
window.mainloop()
