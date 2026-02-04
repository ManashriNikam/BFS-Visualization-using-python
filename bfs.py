import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

G = nx.Graph()
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)
print("BFS Graph with Queue Visualization")

def bfs_visual(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    plt.figure(figsize=(7, 5))

    while queue:
        node = queue.popleft()

        plt.clf()

        
        nx.draw(
            G, pos,
            with_labels=True,
            node_color=[
                'green' if n in visited else 'gray'
                for n in G.nodes()
            ],
            node_size=1500
        )

        
        plt.title(f"Visiting Node: {node}")

        
        queue_text = "Queue: " + " → ".join(queue) if queue else "Queue: Empty"
        plt.text(
            0.02, 0.02,
            queue_text,
            transform=plt.gca().transAxes,
            fontsize=12,
            bbox=dict(facecolor='lightyellow', edgecolor='black')
        )

        plt.pause(2)

        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    plt.show()

bfs_visual(graph, 'A')
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

G = nx.Graph()
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)
print("BFS Graph with FULL Queue Visualization")

def bfs_visual(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    plt.figure(figsize=(8, 6))

    while queue:
       
        queue_before = list(queue)

        node = queue.popleft()

        plt.clf()

       
        nx.draw(
            G, pos,
            with_labels=True,
            node_color=[
                'green' if n in visited else 'gray'
                for n in G.nodes()
            ],
            node_size=1500
        )

        
        plt.title(f"Processing Node: {node}")

        
        plt.text(
            0.02, 0.85,
            "Queue (before pop): " + " → ".join(queue_before),
            transform=plt.gca().transAxes,
            fontsize=11,
            bbox=dict(facecolor='lightblue', edgecolor='black')
        )

        added_nodes = []
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                added_nodes.append(neighbor)

        
        queue_after = list(queue)
        plt.text(
            0.02, 0.75,
            "Queue (after add): " + (" → ".join(queue_after) if queue_after else "Empty"),
            transform=plt.gca().transAxes,
            fontsize=11,
            bbox=dict(facecolor='lightyellow', edgecolor='black')
        )

        added_text = "Added: " + (", ".join(added_nodes) if added_nodes else "None")
        plt.text(
            0.02, 0.65,
            added_text,
            transform=plt.gca().transAxes,
            fontsize=11,
            bbox=dict(facecolor='lightgreen', edgecolor='black')
        )

        plt.pause(5)

    plt.show()

bfs_visual(graph, 'A')
