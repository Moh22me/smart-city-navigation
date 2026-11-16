import heapq
import time

def heuristic(node, goal, positions):
    x1, y1 = positions[node]
    x2, y2 = positions[goal]
    return abs(x1 - x2) + abs(y1 - y2)

def ucs_search(graph, start, goal):
    start_time = time.time()
    frontier = []
    heapq.heappush(frontier, (0, start))
    best_cost = {start: 0}
    came_from = {}
    explored = set()

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_cost > best_cost[current_node]:
            continue

        if current_node == goal:
            path = []
            node = goal
            while node != start:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, current_cost, len(explored), time.time() - start_time

        explored.add(current_node)

        for neighbor, data in graph[current_node].items():
            road_cost = data["weight"]
            new_cost = current_cost + road_cost

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(frontier, (new_cost, neighbor))

    return None, float("inf"), len(explored), time.time() - start_time

def astar_search(graph, start, goal, positions):
    start_time = time.time()
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal, positions), 0, start))
    g_score = {start: 0}
    came_from = {}
    explored = set()

    while frontier:
        f_score, current_cost, current_node = heapq.heappop(frontier)

        if current_cost > g_score[current_node]:
            continue

        if current_node == goal:
            path = []
            node = goal
            while node != start:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, current_cost, len(explored), time.time() - start_time

        explored.add(current_node)

        for neighbor, data in graph[current_node].items():
            road_cost = data["weight"]
            tentative_g = current_cost + road_cost

            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current_node
                h_score = heuristic(neighbor, goal, positions)
                f_score = tentative_g + h_score
                heapq.heappush(frontier, (f_score, tentative_g, neighbor))

    return None, float("inf"), len(explored), time.time() - start_time

import heapq
import time
from collections import deque

# ... (Keep existing heuristic, ucs_search, and astar_search functions here) ...

def bfs_search(graph, start, goal):
    start_time = time.time()
    frontier = deque([start])
    came_from = {start: None}
    explored = set()

    while frontier:
        current_node = frontier.popleft()

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            
            # Calculate total cost for the path
            cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
            return path, cost, len(explored), time.time() - start_time

        explored.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in explored and neighbor not in frontier:
                came_from[neighbor] = current_node
                frontier.append(neighbor)

    return None, float("inf"), len(explored), time.time() - start_time


def dfs_search(graph, start, goal):
    start_time = time.time()
    frontier = [start]  # Using a list as a Stack
    came_from = {start: None}
    explored = set()

    while frontier:
        current_node = frontier.pop()

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            
            # Calculate total cost for the path
            cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
            return path, cost, len(explored), time.time() - start_time

        explored.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                came_from[neighbor] = current_node
                frontier.append(neighbor)

    return None, float("inf"), len(explored), time.time() - start_time