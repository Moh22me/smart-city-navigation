import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def create_base_city():
    city = nx.Graph()
    intersections = [
        "A", "B", "C", "D",
        "E", "F", "G", "H",
        "I", "J", "K", "L",
        "M", "N", "O", "P"
    ]
    city.add_nodes_from(intersections)
    
    positions = {
        "A": (0, 3), "B": (1, 3), "C": (2, 3), "D": (3, 3),
        "E": (0, 2), "F": (1, 2), "G": (2, 2), "H": (3, 2),
        "I": (0, 1), "J": (1, 1), "K": (2, 1), "L": (3, 1),
        "M": (0, 0), "N": (1, 0), "O": (2, 0), "P": (3, 0)
    }

    roads = [
        ("A", "B", 1), ("B", "C", 3), ("C", "D", 1),
        ("E", "F", 1), ("F", "G", 5), ("G", "H", 1),
        ("I", "J", 3), ("J", "K", 1), ("K", "L", 1),
        ("M", "N", 1), ("N", "O", 3), ("O", "P", 1),
        ("A", "E", 1), ("B", "F", 1), ("C", "G", 1), ("D", "H", 3),
        ("E", "I", 1), ("F", "J", 3), ("G", "K", 1), ("H", "L", 1),
        ("I", "M", 5), ("J", "N", 1), ("K", "O", 3), ("L", "P", 1)
    ]
    
    for start, end, cost in roads:
        city.add_edge(start, end, weight=cost)
        
    return city, positions

# ... (Keep create_base_city function as is) ...

def draw_city_graph(city_graph, positions, path=None, start_node="A", goal_node="P", car_position=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Draw base nodes and edges
    nx.draw_networkx_nodes(city_graph, positions, node_color="lightblue", node_size=1200, ax=ax)
    nx.draw_networkx_edges(city_graph, positions, edge_color="gray", width=2, ax=ax)
    
    # Highlight the path if found
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(city_graph, positions, edgelist=path_edges, edge_color="red", width=4, ax=ax)
    
    # Highlight start and goal nodes
    nx.draw_networkx_nodes(city_graph, positions, nodelist=[start_node], node_color="green", node_size=1300, ax=ax)
    nx.draw_networkx_nodes(city_graph, positions, nodelist=[goal_node], node_color="orange", node_size=1300, ax=ax)
    
    # Draw Car Simulation Position
    if car_position:
        nx.draw_networkx_nodes(city_graph, positions, nodelist=[car_position], node_color="yellow", node_size=1800, node_shape='s', ax=ax)
    
    # Labels and Weights
    nx.draw_networkx_labels(city_graph, positions, font_weight="bold", ax=ax)
    edge_labels = nx.get_edge_attributes(city_graph, "weight")
    nx.draw_networkx_edge_labels(city_graph, positions, edge_labels=edge_labels, ax=ax)
    
    ax.axis("off")
    return fig