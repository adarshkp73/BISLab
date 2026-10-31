import random

# 1. Define the Problem: Mathematical function to maximize
def evaluate_fitness(x):
    return -(x - 10)**2 + 100  # Peak is at x = 10

# 2. Initialize Parameters
POP_SIZE = 20
MUTATION_RATE = 0.1
GENERATIONS = 100

# 3. Create Initial Population
population = [random.uniform(0, 20) for _ in range(POP_SIZE)]

# 8. Iteration
for generation in range(GENERATIONS):
    
    # 4. Evaluate Fitness & 5. Selection (Keep top 50%)
    population.sort(key=evaluate_fitness, reverse=True)
    survivors = population[:POP_SIZE // 2]
    next_generation = list(survivors)
    
    # Generate offspring to restore population size
    while len(next_generation) < POP_SIZE:
        # 6. Crossover: Average of two random parents
        parent1, parent2 = random.sample(survivors, 2)
        child = (parent1 + parent2) / 2.0 
        
        # 7. Mutation: Add random noise
        if random.random() < MUTATION_RATE:
            child += random.uniform(-1.0, 1.0)
            
        next_generation.append(child)
        
    population = next_generation

# 9. Output the Best Solution
best_solution = max(population, key=evaluate_fitness)
print(f"Best solution found: x = {best_solution:.4f}")
print(f"Maximum value: {evaluate_fitness(best_solution):.4f}")
