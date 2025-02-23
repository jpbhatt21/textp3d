def dist(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def getBlankPos(state):
    return next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

def getNeighbors(state):
    i, j = getBlankPos(state)
    neighbors = []
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def solvePuzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    queue = [(dist(initial_state), 0, '', initial_state)]
    explored = set()
    
    while queue:
        _, g, path, state = min(queue)
        queue.remove((_, g, path, state))
        
        if state == goal_state:
            return path
        
        explored.add(tuple(map(tuple, state)))
        
        for neighbor in getNeighbors(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in explored:
                h = dist(neighbor)
                new_g = g + 1
                new_path = path + 'UDLR'[getNeighbors(state).index(neighbor)]
                queue.append((new_g + h, new_g, new_path, neighbor))
    
    return None

initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solvePuzzle(initial_state)
if solution:
    print("Solution found in", len(solution), "moves:")
    print(" -> ".join(solution))
else:
    print("No solution found.")