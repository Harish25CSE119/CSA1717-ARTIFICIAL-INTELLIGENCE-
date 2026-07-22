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

print("\n==============================")
print("QUESTION 1 : WATER JUG PROBLEM")
print("==============================")

states = [
    (0,0),
    (0,3),
    (3,0),
    (3,3),
    (4,2),
    (0,2),
    (2,0)
]

actions = [
    "Initial State",
    "Fill 3-Gallon Jug",
    "Pour 3 -> 4",
    "Fill 3-Gallon Jug",
    "Pour 3 -> 4 until Full",
    "Empty 4-Gallon Jug",
    "Pour remaining 2 gallons to 4-Gallon Jug (Goal)"
]

for s,a in zip(states,actions):
    print(f"{a:35} {s}")

print("\nGoal Achieved : 2 gallons in 4-gallon jug")


# ============================================================
# QUESTION 2 - MARS ROVER AGENT
# ============================================================

print("\n==============================")
print("QUESTION 2 : MARS ROVER AGENT")
print("==============================")

class MarsRover:

    def perceive(self):
        print("\nPercepts")
        print("Camera : Rocks detected")
        print("Temperature : -55 C")
        print("Battery : 82%")
        print("Obstacle : None")

    def decide(self):
        print("\nDecision")
        print("Move Forward")
        print("Collect Rock Sample")

    def act(self):
        print("\nActions")
        print("Moving...")
        print("Collecting Sample...")
        print("Analyzing Sample...")
        print("Sending Data to Earth")

rover = MarsRover()
rover.perceive()
rover.decide()
rover.act()


# ============================================================
# QUESTION 3 - 8 QUEENS PROBLEM
# ============================================================

print("\n==============================")
print("QUESTION 3 : 8 QUEENS PROBLEM")
print("==============================")

N = 8

board = [[0]*N for _ in range(N)]

def isSafe(board,row,col):

    for i in range(col):
        if board[row][i]:
            return False

    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]:
            return False
        i-=1
        j-=1

    i=row
    j=col
    while i<N and j>=0:
        if board[i][j]:
            return False
        i+=1
        j-=1

    return True


def solve(board,col):

    if col>=N:
        return True

    for i in range(N):

        if isSafe(board,i,col):

            board[i][col]=1

            if solve(board,col+1):
                return True

            board[i][col]=0

    return False

solve(board,0)

print("\nSolution\n")

for row in board:
    print(row)


# ============================================================
# QUESTION 4 - OLA CAB BOOKING
# ============================================================

print("\n==============================")
print("QUESTION 4 : OLA CAB BOOKING")
print("==============================")

pickup = "College"
destination = "Railway Station"

cab_types = {
    "Mini":120,
    "Micro":100,
    "Sedan":180,
    "Prime":250,
    "Shared":80
}

print("\nPickup :",pickup)
print("Destination :",destination)

print("\nAvailable Cabs")

for cab,fare in cab_types.items():
    print(cab,"- Rs",fare)

selected = min(cab_types,key=cab_types.get)

print("\nSelected Cab :",selected)
print("Estimated Fare :",cab_types[selected])

print("\nDriver Assigned")
print("Ride Started")
print("Ride Completed")


# ============================================================
# QUESTION 5 - UNIFORM COST SEARCH
# ============================================================

print("\n==============================")
print("QUESTION 5 : UNIFORM COST SEARCH")
print("==============================")

from queue import PriorityQueue

graph = {
'S':[('A',1),('G',12)],
'A':[('B',3),('C',1)],
'B':[('D',3)],
'C':[('D',1),('G',2)],
'D':[('G',3)],
'G':[]
}

def ucs(start,goal):

    pq = PriorityQueue()

    pq.put((0,start,[start]))

    visited={}

    while not pq.empty():

        cost,node,path = pq.get()

        if node==goal:
            return cost,path

        if node in visited and visited[node]<=cost:
            continue

        visited[node]=cost

        for nxt,w in graph[node]:

            pq.put((cost+w,nxt,path+[nxt]))

cost,path = ucs('S','G')

print("\nOptimal Path")

print(" -> ".join(path))

print("Minimum Cost =",cost)

print("\nAssignment Completed Successfully")
