import networkx as nx
from task_1 import create_transportation_network
import matplotlib.pyplot as plt
from collections import deque

def dfs_paths(graph, start, goal):
    """Find a path using Depth-First Search (DFS)"""
    stack = [(start, [start])]  # (current node, path to current node)
    visited = set()
    
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            # Add neighbors to stack in reverse order to prioritize alphabetical order
            neighbors = sorted(graph[vertex], reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def bfs_paths(graph, start, goal):
    """Find a path using Breadth-First Search (BFS)"""
    queue = deque([(start, [start])])  # (current node, path to current node)
    visited = set([start])
    
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in sorted(graph[vertex]):  # Sort for deterministic behavior
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def visualize_path(G, path, title):
    """Visualize a path in the graph"""
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
    
    # Create a list of edges in the path
    path_edges = list(zip(path, path[1:]))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", alpha=0.8)
    
    # Draw edges not in path
    non_path_edges = [(u, v) for u, v in G.edges() if (u, v) not in path_edges and (v, u) not in path_edges]
    nx.draw_networkx_edges(G, pos, edgelist=non_path_edges, width=1.5, alpha=0.3)
    
    # Draw path edges
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color="red")
    
    # Highlight start and end nodes
    nx.draw_networkx_nodes(G, pos, nodelist=[path[0], path[-1]], node_color="red", alpha=0.8)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    plt.title(title, fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    plt.show()

def compare_algorithms():
    """Compare DFS and BFS on the transportation network"""
    # Create the transportation network
    G = create_transportation_network()
    
    # Define test cases: (start_station, end_station)
    test_cases = [
        ("Central Station", "Tech Hub"),
        ("Airport", "Hospital"),
        ("Residential Area", "Shopping Mall")
    ]
    
    # Run algorithms on test cases
    results = []
    for start, end in test_cases:
        dfs_path = dfs_paths(G, start, end)
        bfs_path = bfs_paths(G, start, end)
        
        results.append({
            'start': start,
            'end': end,
            'dfs_path': dfs_path,
            'dfs_length': len(dfs_path) - 1 if dfs_path else None,
            'bfs_path': bfs_path,
            'bfs_length': len(bfs_path) - 1 if bfs_path else None
        })
        
        # Visualize the paths
        if dfs_path:
            visualize_path(G, dfs_path, f"DFS Path: {start} to {end}")
        if bfs_path:
            visualize_path(G, bfs_path, f"BFS Path: {start} to {end}")
    
    # Print comparison results
    print("\nComparison of DFS and BFS Algorithms:")
    print("=" * 80)
    for result in results:
        print(f"\nPath from {result['start']} to {result['end']}:")
        print(f"DFS Path: {' -> '.join(result['dfs_path'])} (Length: {result['dfs_length']})")
        print(f"BFS Path: {' -> '.join(result['bfs_path'])} (Length: {result['bfs_length']})")
        
        if result['dfs_length'] == result['bfs_length']:
            if result['dfs_path'] == result['bfs_path']:
                print("Both algorithms found the same path with the same length.")
            else:
                print("Both algorithms found different paths but with the same length.")
        else:
            print("BFS found the shortest path as expected, while DFS explored deeper.")

if __name__ == "__main__":
    compare_algorithms()
