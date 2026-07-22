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

print("\n===================================================")
print("QUESTION 1 : DOCTOR SHIFT SCHEDULING")
print("BACKTRACKING SEARCH")
print("===================================================")

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

assignment = {}

def is_valid(doctor, shift):

    # D1 cannot work Night
    if doctor == "D1" and shift == "Night":
        return False

    # D3 cannot work Morning
    if doctor == "D3" and shift == "Morning":
        return False

    # Only one doctor per shift
    if shift in assignment.values():
        return False

    temp = assignment.copy()
    temp[doctor] = shift

    # D2 must work before D3
    if "D2" in temp and "D3" in temp:

        order = {
            "Morning":1,
            "Afternoon":2,
            "Night":3
        }

        if order[temp["D2"]] >= order[temp["D3"]]:
            return False

    return True


def backtrack(index):

    if index == len(doctors):
        return True

    doctor = doctors[index]

    for shift in shifts:

        print(f"Trying {doctor} -> {shift}")

        if is_valid(doctor, shift):

            assignment[doctor] = shift

            if backtrack(index+1):
                return True

            print("Backtracking...\n")
            del assignment[doctor]

    return False


backtrack(0)

print("\nFINAL SCHEDULE")

for d,s in assignment.items():
    print(d,"->",s)



# ==========================================================
# QUESTION 2
# Robot Navigation using Breadth First Search
# ==========================================================

print("\n===================================================")
print("QUESTION 2 : ROBOT NAVIGATION")
print("BREADTH FIRST SEARCH")
print("===================================================")

grid = [

['S','.','.','X','.'],
['.','X','.','X','.'],
['.','X','.','.','.'],
['.','.','X','X','.'],
['.','.','.','.','G']

]

rows = len(grid)
cols = len(grid[0])

start = (0,0)
goal = (4,4)

moves = [

(-1,0),
(1,0),
(0,-1),
(0,1)

]

queue = deque()

queue.append((start,[start]))

visited = set()

visited.add(start)

found = False

while queue:

    node,path = queue.popleft()

    print("Expanding :",node)

    if node == goal:

        print("\nGOAL FOUND")
        print("PATH =",path)
        print("TOTAL COST =",len(path)-1)
        found = True
        break

    for dx,dy in moves:

        nx = node[0]+dx
        ny = node[1]+dy

        if 0<=nx<rows and 0<=ny<cols:

            if grid[nx][ny]!="X" and (nx,ny) not in visited:

                visited.add((nx,ny))
                queue.append(((nx,ny),path+[(nx,ny)]))

if not found:
    print("No Path Found")



# ==========================================================
# QUESTION 3
# Autonomous Rescue Robot
# Uniform Cost Search
# ==========================================================

print("\n===================================================")
print("QUESTION 3 : AUTONOMOUS RESCUE ROBOT")
print("UNIFORM COST SEARCH")
print("===================================================")

grid = [

['S','.','X','.','.'],
['.','R','.','X','.'],
['.','.','.','R','.'],
['X','.','.','.','.'],
['.','X','.','.','G']

]

rows = len(grid)
cols = len(grid)

start = (0,0)
goal = (4,4)

moves = [

(-1,0),
(1,0),
(0,-1),
(0,1)

]

pq = []

heapq.heappush(pq,(0,start,[start]))

visited = {}

while pq:

    cost,node,path = heapq.heappop(pq)

    if node == goal:

        print("\nSURVIVOR REACHED")
        print("Optimal Path")

        for p in path:
            print(p,end=" ")

        print("\nTotal Cost =",cost)
        break

    if node in visited and visited[node] <= cost:
        continue

    visited[node]=cost

    for dx,dy in moves:

        nx=node[0]+dx
        ny=node[1]+dy

        if 0<=nx<rows and 0<=ny<cols:

            if grid[nx][ny]!="X":

                move_cost=1

                if grid[nx][ny]=="R":
                    move_cost+=2

                heapq.heappush(

                    pq,
                    (
                        cost+move_cost,
                        (nx,ny),
                        path+[(nx,ny)]
                    )

                )

print("\n===================================================")
print("ALL THREE PROBLEMS EXECUTED SUCCESSFULLY")
print("===================================================")
