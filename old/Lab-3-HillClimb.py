import random

def evaluate(solution):
    return sum(solution)

def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        neighbor = solution[:]
        neighbor[i] = random.randint(0, 100)
        neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_solution):
    current = initial_solution[:]
    current_value = evaluate(current)
    
    while True:
        neighbors = generate_neighbors(current)
        found_better = False
        
        for neighbor in neighbors:
            neighbor_value = evaluate(neighbor)
            if neighbor_value > current_value:
                current = neighbor
                current_value = neighbor_value
                found_better = True
                break
        
        if not found_better:
            break
    
    return current, current_value

initial_solution = [10, 20, 30, 40, 50]
best_solution, best_value = hill_climbing(initial_solution)
print("Best solution:", best_solution)
print("Value:", best_value)
