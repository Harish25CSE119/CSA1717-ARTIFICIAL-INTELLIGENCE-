"""
===========================================================
ARTIFICIAL INTELLIGENCE - ASSESSMENT II
===========================================================

1. Doctor Shift Scheduling using Backtracking Search
2. Robot Navigation using Breadth First Search (BFS)
3. Autonomous Rescue Robot using Uniform Cost Search (UCS)

===========================================================
"""

from collections import deque
import heapq

# ==========================================================
# QUESTION 1
# Doctor Shift Scheduling using Backtracking Search
# ==========================================================

# Hospital Doctor Scheduling using Backtracking

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

# Store assigned shifts
assignment = {}

# Check whether assigning a shift to a doctor is valid
def is_valid(doctor, shift):

    # Constraint 1: D1 cannot work Night
    if doctor == "D1" and shift == "Night":
        return False

    # Constraint 2: D3 cannot work Morning
    if doctor == "D3" and shift == "Morning":
        return False

    # Constraint 3: Only one doctor per shift
    if shift in assignment.values():
        return False

    return True


# Backtracking Function
def backtrack(index):

    # All doctors assigned
    if index == len(doctors):

        # Constraint 4: D2 must work before D3
        order = {
            "Morning": 1,
            "Afternoon": 2,
            "Night": 3
        }

        if order[assignment["D2"]] < order[assignment["D3"]]:
            return True
        else:
            return False

    doctor = doctors[index]

    for shift in shifts:

        print(f"Trying {doctor} -> {shift}")

        if is_valid(doctor, shift):

            assignment[doctor] = shift
            print("Accepted:", assignment)

            if backtrack(index + 1):
                return True

            # Backtracking
            print("Backtracking from", doctor)
            del assignment[doctor]

        else:
            print("Rejected")

    return False


# Main Program
if backtrack(0):

    print("\n===== FINAL SCHEDULE =====")

    for doctor in doctors:
        print(doctor, "->", assignment[doctor])

else:
    print("No Valid Schedule Found.")



# ==========================================================
# QUESTION 2
# Robot Navigation using Breadth First Search
# ==========================================================

from collections import deque

# 5x5 Grid
grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['#', '.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

# Find Start and Goal
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Manhattan Distance Heuristic
def manhattan(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

# BFS Algorithm
def bfs(start, goal):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        print("Expanded Node:", current,
              " Heuristic =", manhattan(current, goal))

        if current == goal:
            return path

        row, col = current

        # Up, Down, Left, Right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if (0 <= nr < ROWS and
                0 <= nc < COLS and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                queue.append(((nr, nc), path + [(nr, nc)]))

        print("Queue:", [item[0] for item in queue])

    return None


# Main Program
path = bfs(start, goal)

print("\n========== RESULT ==========")

if path:
    print("Shortest Path:")
    print(path)
    print("Total Cost:", len(path)-1)
else:
    print("No Path Found.")



# ==========================================================
# QUESTION 3
# Autonomous Rescue Robot
# Uniform Cost Search
# ==========================================================

import heapq

# Building Grid
grid = [
    ['S', '.', '.', 'R', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', 'R', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

# Find Start and Goal
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Cost Function
def get_cost(cell):
    if cell == 'R':      # Risky Zone
        return 3         # 1 movement + 2 extra risk cost
    return 1             # Normal movement

# Uniform Cost Search
def uniform_cost_search(start, goal):

    priority_queue = [(0, start, [start])]
    visited = {}

    while priority_queue:

        cost, current, path = heapq.heappop(priority_queue)

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        print("Expanded:", current, " Cost:", cost)

        if current == goal:
            return path, cost

        row, col = current

        # Up, Down, Left, Right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:

                if grid[nr][nc] != '#':

                    new_cost = cost + get_cost(grid[nr][nc])

                    heapq.heappush(
                        priority_queue,
                        (new_cost, (nr, nc), path + [(nr, nc)])
                    )

        print("Priority Queue:",
              [(item[1], item[0]) for item in priority_queue])

    return None, None


# Main Program
path, total_cost = uniform_cost_search(start, goal)

print("\n========== RESULT ==========")

if path:
    print("Optimal Path:")
    print(path)
    print("Minimum Cost:", total_cost)
else:
    print("No Path Found")