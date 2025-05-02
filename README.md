# City Transportation Network Analysis

This project analyzes a city transportation network using graph theory algorithms.
The network represents a metro transit system connecting various points of in a generalized city.

A transportation network was modeled as a graph where:

- Nodes represent stations or key locations (e.g., Central Station, Airport, Shopping Mall)
- Edges represent direct transportation connections between locations

### Key characteristics of the network:

- 16 stations (nodes)
- 20 connections (edges)
- The Central Station is the most connected hub with 5 direct connections
- Average connections per station: 2.67

The visualization shows the network layout with node sizes representing their connectivity degree.

Two fundamental graph traversal algorithms were implemented to find paths between stations:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)

### Comparison of DFS and BFS:

1. **Path Finding Approach**:

   - DFS explores as far as possible along each branch before backtracking, often finding longer, less direct paths
   - BFS explores all neighbors at the present depth before moving to nodes at the next depth level, guaranteeing shortest paths in unweighted graphs

2. **Key Differences**:

   - DFS tends to find paths that "wander" through the network following a deeper exploration pattern
   - BFS always finds the shortest path in terms of number of edges (stations to visit)
   - When multiple paths with the same length exist, the algorithms may find different routes

3. **Results from Test Cases**:
   - For nearby stations, both algorithms often find the same path
   - For distant stations, DFS typically finds longer paths than BFS
   - BFS is more appropriate when finding the path with fewest station transfers

## Conclusion

This analysis demonstrates the application of graph theory to model and analyze transportation networks. The comparison of different path-finding algorithms reveals their strengths and weaknesses:

- **DFS**: Useful for exploring all possible paths but not optimal for finding shortest routes
- **BFS**: Ideal for finding paths with the minimum number of transfers in unweighted networks
- **Dijkstra's Algorithm**: Essential for finding the fastest routes when travel times vary between connections

The weighted graph analysis provides valuable insights for transit planning, highlighting central nodes and potential bottlenecks in the transportation system.
