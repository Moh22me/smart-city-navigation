# 🚑 Smart City Emergency Navigation System

An interactive pathfinding visualization and live vehicle simulation dashboard designed to model emergency routing across a dynamic urban grid. Built with **Python**, **NetworkX**, and **Streamlit**.

---

## 📋 Overview
In emergency response scenarios, finding the optimal route under rapidly changing road conditions is critical. This application simulates a 16-intersection smart city network and provides a comparative analysis of classic graph search algorithms alongside a real-time step-by-step vehicle navigation simulation.

---

## ✨ Key Features
* **Multi-Algorithm Pathfinding Engine:** Compare execution metrics (Path Cost, Explored Nodes, Execution Time, and Path Length) across four distinct search strategies:
  * **A* Search:** Informed search utilizing Manhattan Distance heuristic.
  * **Uniform Cost Search (UCS):** Uninformed search guaranteeing the lowest cumulative path cost.
  * **Breadth-First Search (BFS):** Level-by-level exploration finding the path with the fewest intersections.
  * **Depth-First Search (DFS):** Deep-branch exploration demonstrating non-optimal pathing behaviors.
* **Dynamic City Scenarios:** Test algorithm adaptability against real-world disruptions:
  * **Normal City:** Standard baseline traffic weights.
  * **Road Closure:** Simulates complete blockages (e.g., closing road `C-G`).
  * **Heavy Traffic:** Dynamically increases edge weights to simulate severe congestion (e.g., increasing `B-C` cost to `8`).
* **Live Car Simulation (Multi-Page UI):** A dedicated simulation module that animates the emergency vehicle traversing the calculated route node-by-node in real time with adjustable playback speed.

---

## 🏗️ Project Architecture
The codebase follows a clean, modular design separating UI rendering, graph data structures, and algorithmic logic:

```text
Smart City/
│
├── app.py                     # Main Streamlit dashboard & comparative metrics UI
├── algorithms.py              # Core implementations of A*, UCS, BFS, DFS, and Heuristics
├── city_graph.py              # NetworkX graph initialization & Matplotlib rendering engine
├── pages/
│   └── Car_Simulation.py      # Real-time step-by-step vehicle animation page
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
