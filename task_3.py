import networkx as nx
import matplotlib.pyplot as plt
import heapq
import pandas as pd

def create_weighted_transportation_network():
    """Create a weighted transportation network graph representing a city's metro system."""
    G = nx.Graph()
    
    # Add stations (nodes)
    stations = [
        "Central Station", "North Terminal", "South Terminal", "East Station", "West Station",
        "University", "Business District", "Shopping Mall", "Airport", "Stadium", 
        "Hospital", "Park", "Residential Area", "Industrial Zone", "Tech Hub"
    ]
    
    G.add_nodes_from(stations)
    
    # Add connections (edges) with weights (distance in minutes)
    weighted_connections = [
        ("Central Station", "North Terminal", 8),
        ("Central Station", "South Terminal", 7),
        ("Central Station", "East Station", 9),
        ("Central Station", "West Station", 10),
        ("Central Station", "Business District", 5),
        ("North Terminal", "University", 6),
        ("North Terminal", "Residential Area", 12),
        ("South Terminal", "Shopping Mall", 4),
        ("South Terminal", "Stadium", 8),
        ("East Station", "Hospital", 7),
        ("East Station", "Tech Hub", 15),
        ("West Station", "Park", 6),
        ("West Station", "Industrial Zone", 14),
        ("Business District", "Tech Hub", 9),
        ("Shopping Mall", "Park", 11),
        ("Airport", "Central Station", 20),
        ("Airport", "Business District", 15),
        ("University", "Hospital", 8),
        ("Tech Hub", "Industrial Zone", 13),
        ("Residential Area", "Park", 7),
    ]
    
    # Add edges with weights
    for u, v, w in weighted_connections:
        G.add_edge(u, v, weight=w)
    
    return G

def dijkstra(graph, start):
    """
    Implementation of Dijkstra's algorithm to find shortest paths
    from start node to all other nodes.
    Returns distances and paths.
    """
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous = {node: None for node in graph.nodes()}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've already found a shorter way to the current node, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous

def reconstruct_path(previous, start, end):
    """Reconstruct the path from start to end using the previous dictionary."""
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
        if current is None:
            return None  # No path exists
    path.append(start)
    
    return path[::-1]  # Reverse to get path from start to end

def visualize_weighted_graph(G):
    """Visualize the weighted transportation network graph."""
    plt.figure(figsize=(14, 12))
    pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue", alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    plt.title("Weighted City Transportation Network", fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("weighted_transportation_network.png")
    plt.show()

def visualize_shortest_path(G, path, title):
    """Visualize a shortest path in the weighted graph."""
    plt.figure(figsize=(14, 12))
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
    nx.draw_networkx_nodes(G, pos, nodelist=[path[0], path[-1]], node_color="red", node_size=900, alpha=0.8)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    plt.title(title, fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower().replace(':', '')}.png")
    plt.show()

def find_all_shortest_paths(G):
    """
    Find shortest paths between all pairs of nodes in the graph.
    Return as a pandas DataFrame for better visualization.
    """
    stations = list(G.nodes())
    
    # Initialize DataFrame
    df = pd.DataFrame(index=stations, columns=stations)
    
    # Find all shortest paths
    for start in stations:
        distances, previous = dijkstra(G, start)
        for end in stations:
            if start == end:
                df.at[start, end] = 0
                continue
                
            path = reconstruct_path(previous, start, end)
            if path:
                df.at[start, end] = distances[end]
            else:
                df.at[start, end] = float('inf')
    
    return df

if __name__ == "__main__":
    # Create weighted transportation network
    G = create_weighted_transportation_network()
    
    # Visualize the weighted graph
    visualize_weighted_graph(G)
    
    # Example of finding shortest path between two stations
    start_station = "Airport"
    end_station = "Hospital"
    
    # Use Dijkstra's algorithm
    distances, previous = dijkstra(G, start_station)
    shortest_path = reconstruct_path(previous, start_station, end_station)
    
    # Print result
    print(f"Shortest path from {start_station} to {end_station}:")
    print(" -> ".join(shortest_path))
    print(f"Total travel time: {distances[end_station]} minutes")
    
    # Visualize the shortest path
    visualize_shortest_path(G, shortest_path, f"Shortest Path: {start_station} to {end_station}")
    
    # Find shortest paths between all station pairs
    all_shortest_paths = find_all_shortest_paths(G)
    
    print("\nShortest paths between all stations (in minutes):")
    print(all_shortest_paths)
    
    # Find and display the station that's most central (shortest average distance to all other stations)
    average_distances = all_shortest_paths.mean(axis=1)
    most_central = average_distances.idxmin()
    print(f"\nMost central station: {most_central} (Average distance: {average_distances[most_central]:.2f} minutes)")
