import networkx as nx
import matplotlib.pyplot as plt

def create_transportation_network():
    """Create a transportation network graph representing a city's metro system."""
    G = nx.Graph()
    
    # Add stations (nodes)
    stations = [
        "Central Station", "North Station", "South Station", "East Station", "West Station",
        "University", "Business District", "Shopping Mall", "Airport", "Stadium", 
        "Hospital", "Park", "Residential Area", "Industrial Zone", "Tech Hub", "Conference hub"
    ]
    
    G.add_nodes_from(stations)
    
    # Add connections (edges)
    connections = [
        ("Central Station", "North Station"),
        ("Central Station", "South Station"),
        ("Central Station", "East Station"),
        ("Central Station", "West Station"),
        ("Central Station", "Business District"),
        ("North Station", "University"),
        ("North Station", "Residential Area"),
        ("South Station", "Shopping Mall"),
        ("South Station", "Stadium"),
        ("East Station", "Park"),
        ("East Station", "Conference hub"),
        ("West Station", "Hospital"),
        ("West Station", "Industrial Zone"),
        ("Business District", "Tech Hub"),
        ("Shopping Mall", "Park"),
        ("Airport", "Central Station"),
        ("Airport", "Business District"),
        ("University", "Hospital"),
        ("Tech Hub", "Industrial Zone"),
        ("Residential Area", "Park"),
    ]
    
    G.add_edges_from(connections)
    return G

def analyze_graph(G):
    """Analyze and print basic characteristics of the graph."""
    print(f"Graph analysis of the transportation network:")
    print(f"Number of stations (nodes): {G.number_of_nodes()}")
    print(f"Number of connections (edges): {G.number_of_edges()}")
    
    degrees = dict(G.degree())
    print("\nStation connectivity (degree):")
    for station, degree in sorted(degrees.items(), key=lambda x: x[1], reverse=True):
        print(f"{station}: {degree} connections")
    
    print(f"\nAverage connections per station: {sum(degrees.values()) / len(degrees):.2f}")
    print(f"Maximum connections: {max(degrees.values())}")
    print(f"Minimum connections: {min(degrees.values())}")

def visualize_graph(G):
    """Visualize the transportation network graph."""
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
    
    # Draw nodes with different sizes based on degree
    degrees = dict(G.degree())
    node_sizes = [degrees[node] * 150 for node in G.nodes()]
    
    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="lightblue", alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    plt.title("City Transportation Network", fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("transportation_network.png")
    plt.show()

if __name__ == "__main__":
    # Create the transportation network graph
    G = create_transportation_network()
    
    # Analyze the graph
    analyze_graph(G)
    
    # Visualize the graph
    visualize_graph(G)
