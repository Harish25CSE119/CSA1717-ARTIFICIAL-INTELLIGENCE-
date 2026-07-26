"""
ARTIFICIAL INTELLIGENCE LAB ASSIGNMENT

1. Water Jug Problem
2. Mars Rover Intelligent Agent
3. 8 Queens Problem
4. OLA Cab Booking Agent
5. Uniform Cost Search

Author:
"""

# ============================================================
# QUESTION 1 - WATER JUG PROBLEM
# ============================================================

from collections import deque

# Function to solve Water Jug Problem using BFS
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Initial state (0,0)
    queue.append(((0, 0), []))

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Skip if already visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Goal check
        if jug1 == target or jug2 == target:
            return path

        # Possible operations
        next_states = [
            (jug1_capacity, jug2),                 # Fill Jug1
            (jug1, jug2_capacity),                 # Fill Jug2
            (0, jug2),                            # Empty Jug1
            (jug1, 0),                            # Empty Jug2
        ]

        # Pour Jug1 -> Jug2
        transfer = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - transfer, jug2 + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + transfer, jug2 - transfer))

        # Add unvisited states
        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None


# Main Program
jug1_capacity = 4
jug2_capacity = 3
target = 2

solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)

if solution:
    print("Solution Found!\n")
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug1 = {state[0]} gallons, Jug2 = {state[1]} gallons")
else:
    print("No solution exists.")


# ============================================================
# QUESTION 2 - MARS ROVER AGENT
# ============================================================

import random

class MarsRover:
    def __init__(self):
        self.energy = 100
        self.samples_collected = 0
        self.data_transmitted = 0
        self.position = (0, 0)

    # Perceive the environment
    def perceive(self):
        percept = {
            "terrain": random.choice(["Rocky", "Sandy", "Flat"]),
            "rock_detected": random.choice([True, False]),
            "temperature": random.randint(-90, 20),
            "obstacle": random.choice([True, False])
        }
        print("\nPercepts:", percept)
        return percept

    # Move to a new position
    def move(self, direction):
        x, y = self.position

        if direction == "North":
            self.position = (x, y + 1)
        elif direction == "South":
            self.position = (x, y - 1)
        elif direction == "East":
            self.position = (x + 1, y)
        elif direction == "West":
            self.position = (x - 1, y)

        self.energy -= 5
        print("Moved", direction, "to", self.position)

    # Analyze rock sample
    def analyze_sample(self):
        self.samples_collected += 1
        self.energy -= 10
        print("Rock sample analyzed.")

    # Send collected data
    def transmit_data(self):
        self.data_transmitted += 1
        self.energy -= 2
        print("Data transmitted to Earth.")

    # Performance evaluation
    def performance(self):
        score = (self.samples_collected * 20) + \
                (self.data_transmitted * 10) + \
                self.energy

        print("\nPerformance Report")
        print("------------------")


# ============================================================
# QUESTION 3 - 8 QUEENS PROBLEM
# ============================================================

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()


# Function to check if a queen can be placed safely
def is_safe(board, row, col, n):

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Backtracking function
def solve_queens(board, col, n):

    # Base case: All queens placed
    if col >= n:
        return True

    # Try placing queen in each row
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_queens(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main Program
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_queens(board, 0, n):
    print("Solution Found:\n")
    print_board(board)
else:
    print("No Solution Exists.")


# ============================================================
# QUESTION 4 - OLA CAB BOOKING
# ============================================================

# OLA Cab Booking using Goal-Based Agent

def ola_booking():

    # Available cab types
    cabs = {
        1: ("Micro", 120),
        2: ("Mini", 180),
        3: ("Sedan", 250),
        4: ("Prime", 350),
        5: ("Shared", 100)
    }

    print("========= OLA CAB BOOKING =========")

    source = input("Enter Pickup Location: ")
    destination = input("Enter Destination: ")

    print("\nAvailable Cabs")
    print("---------------------------")

    for key, value in cabs.items():
        print(f"{key}. {value[0]} - Rs.{value[1]}")

    choice = int(input("\nSelect Cab Type (1-5): "))

    if choice in cabs:
        cab, fare = cabs[choice]

        print("\nBooking Successful!")
        print("---------------------------")
        print("Pickup      :", source)
        print("Destination :", destination)
        print("Cab Type    :", cab)
        print("Estimated Fare : Rs.", fare)
        print("Status      : Driver Assigned")
        print("Goal Achieved: Customer reaches destination successfully.")
    else:
        print("Invalid Cab Selection!")


# Main Program
ola_booking()


# ============================================================
# QUESTION 5 - UNIFORM COST SEARCH
# ============================================================

import heapq

# Graph represented as an adjacency list
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

# Uniform Cost Search Algorithm
def uniform_cost_search(graph, start, goal):

    # Priority Queue: (cost, current_node, path)
    priority_queue = [(0, start, [])]

    visited = set()

    while priority_queue:

        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        print(f"Visited: {node}, Cost: {cost}")

        # Goal Test
        if node == goal:
            return path, cost

        # Expand neighbors
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (cost + edge_cost, neighbor, path))

    return None, float('inf')


# Main Program
start = 'S'
goal = 'G'

path, cost = uniform_cost_search(graph, start, goal)

print("\n========== RESULT ==========")
print("Least Cost Path :", " -> ".join(path))
print("Total Cost      :", cost)