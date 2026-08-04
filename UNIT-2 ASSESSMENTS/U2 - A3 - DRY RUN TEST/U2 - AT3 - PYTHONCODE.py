# ============================================
# ARTIFICIAL INTELLIGENCE LAB PROGRAMS
# 1. A* Search Algorithm
# 2. Minimax with Alpha-Beta Pruning
# ============================================

from heapq import heappush, heappop
import math

# ============================================
# PROGRAM 1 : A* SEARCH ALGORITHM
# ============================================

print("========== A* SEARCH ALGORITHM ==========\n")

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 3), ('D', 7), ('E', 2)],
    'C': [('A', 4), ('B', 3), ('E', 3)],
    'D': [('B', 7), ('E', 2), ('G', 2)],
    'E': [('B', 2), ('C', 3), ('D', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}


def astar(start, goal):
    open_list = []
    heappush(open_list, (heuristic[start], start))

    g = {start: 0}
    parent = {start: None}
    closed = []

    while open_list:

        f, current = heappop(open_list)

        if current in closed:
            continue

        closed.append(current)

        print("Current Node :", current)

        if current == goal:
            break

        for neighbor, cost in graph[current]:

            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + heuristic[neighbor]
                heappush(open_list, (new_f, neighbor))

        print("Open List :", open_list)
        print("Closed List :", closed)
        print()

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Optimal Path :", " -> ".join(path))
    print("Total Cost :", g[goal])


astar('A', 'G')

# ============================================
# PROGRAM 2 : MINIMAX WITH ALPHA-BETA PRUNING
# ============================================

print("\n\n========== MINIMAX WITH ALPHA-BETA PRUNING ==========\n")

tree = [
    [3, 5, 6],     # Left MIN node
    [9, 1, 2]      # Right MIN node
]


def minimax():

    alpha = -math.inf
    beta = math.inf

    # Left MIN
    left = min(tree[0])
    print("Left MIN Value =", left)

    alpha = max(alpha, left)
    print("Alpha =", alpha)

    # Right MIN
    beta = math.inf
    right = math.inf

    for value in tree[1]:

        right = min(right, value)
        beta = min(beta, right)

        print("Visited :", value,
              " Alpha =", alpha,
              " Beta =", beta)

        if beta <= alpha:
            print("Remaining nodes are pruned.")
            break

    result = max(left, right)

    print("\nBest Move for MAX :", left)
    print("Final Minimax Value :", result)


minimax()
