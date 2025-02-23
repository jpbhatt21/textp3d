import random
def fitness(x):
    return x * x
def generate_population(size):
    population = []
    for i in range(size):
        population.append(random.randint(0, 31))
    return population

def selection(population):
    sorted_population = sorted(population, key=fitness, reverse=True)
    return sorted_population[:2]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 4) 
    mask = (1 << crossover_point) - 1
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return child1, child2

def mutate(individual):
    mutation_point = random.randint(0, 4)
    individual = individual ^ (1 << mutation_point)
    return individual

def genetic_algorithm():
    population_size = 6
    population = generate_population(population_size)
    print("Initial Population:", population)

    generations = 5
    for gen in range(generations):
        print("\nGeneration", gen + 1)
        parents = selection(population)
        print("Selected Parents:", parents)
        offspring = []
        child1, child2 = crossover(parents[0], parents[1])
        offspring.append(child1)
        offspring.append(child2)
        print("Offspring from Crossover:", offspring)
        mutated_offspring = []
        for child in offspring:
            mutated_child = mutate(child)
            mutated_offspring.append(mutated_child)
        print("Mutated Offspring:", mutated_offspring)
        population = parents + mutated_offspring
        print("New Population:", population)
    best_solution = max(population, key=fitness)
    print("\nBest solution found:", best_solution)
    print("Fitness of Best solution (x^2):", fitness(best_solution))
genetic_algorithm()
