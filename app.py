import streamlit as st
from city_graph import create_base_city, draw_city_graph
from algorithms import ucs_search, astar_search, bfs_search, dfs_search

# Page Configuration
st.set_page_config(page_title="Smart City Navigation", page_icon="🚑", layout="wide")

def main():
    st.title("🚑 Smart City Emergency Navigation")
    st.markdown("Professional pathfinding visualization supporting **A***, **UCS**, **BFS**, and **DFS**.")
    
    # Load Data from city_graph.py
    base_city, positions = create_base_city()
    active_city = base_city.copy()
    
    # Sidebar Controls
    st.sidebar.header("⚙️ Simulation Controls")
    
    algorithm = st.sidebar.selectbox(
        "Select Algorithm", 
        ["A* Search", "Uniform Cost Search (UCS)", "Breadth-First Search (BFS)", "Depth-First Search (DFS)"],
        key="main_algo_select"
    )
    
    scenario = st.sidebar.radio(
        "City Scenario", 
        ["Normal City", "Road Closure (C-G)", "Heavy Traffic (B-C = 8)"],
        key="main_scenario_select"
    )
    
    col_start, col_goal = st.sidebar.columns(2)
    start_node = col_start.selectbox("Start", list(positions.keys()), index=0, key="main_start")
    goal_node = col_goal.selectbox("Goal", list(positions.keys()), index=15, key="main_goal")

    
    # Apply Scenarios
    if scenario == "Road Closure (C-G)":
        if active_city.has_edge("C", "G"):
            active_city.remove_edge("C", "G")
            st.sidebar.warning("🚧 Road C-G is blocked!")
            
    elif scenario == "Heavy Traffic (B-C = 8)":
        if active_city.has_edge("B", "C"):
            active_city["B"]["C"]["weight"] = 8
            st.sidebar.error("🚦 Heavy traffic on B-C!")

    # Execute Selected Algorithm from algorithms.py
    if algorithm == "A* Search":
        path, cost, explored, exec_time = astar_search(active_city, start_node, goal_node, positions)
    elif algorithm == "Uniform Cost Search (UCS)":
        path, cost, explored, exec_time = ucs_search(active_city, start_node, goal_node)
    elif algorithm == "Breadth-First Search (BFS)":
        path, cost, explored, exec_time = bfs_search(active_city, start_node, goal_node)
    elif algorithm == "Depth-First Search (DFS)":
        path, cost, explored, exec_time = dfs_search(active_city, start_node, goal_node)
        
    # Main Dashboard Metrics
    st.subheader(f"Results for {algorithm}")
    m1, m2, m3, m4 = st.columns(4)
    if path:
        m1.metric("Total Path Cost", cost)
        m2.metric("Explored Nodes", explored)
        m3.metric("Execution Time (ms)", f"{exec_time * 1000:.3f}")
        m4.metric("Path Length", len(path))
        st.success(f"**Optimal Route:** {' ➔ '.join(path)}")
    else:
        st.error("No path available between the selected nodes.")
        
    # Visualization
    st.markdown("---")
    st.subheader("🗺️ City Map Visualization")
    fig = draw_city_graph(active_city, positions, path=path, start_node=start_node, goal_node=goal_node)
    st.pyplot(fig)

if __name__ == "__main__":
    main()