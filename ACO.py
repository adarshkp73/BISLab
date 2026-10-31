import math
import random

# 1. Define the Problem: Create a set of cities with their coordinates[cite: 3]
cities = [(0, 0), (2, 8), (5, 2), (8, 6), (9, 1)]
n = len(cities)
dist = [[math.dist(c1, c2) for c2 in cities] for c1 in cities]

# 2. Initialize Parameters: Set ants, alpha, beta, rho, and initial pheromone[cite: 3]
num_ants = 10
alpha, beta, rho, init_phero = 1.0, 2.0, 0.5, 1.0
pheromones = [[init_phero] * n for _ in range(n)]
best_tour, best_len = None, float('inf')

# 5. Iterate: Repeat construction and updating process[cite: 3]
for _ in range(50):
    all_tours = []
    
    # 3. Construct Solutions: Choose next city probabilistically[cite: 3]
    for _ in range(num_ants):
        tour = [random.randint(0, n - 1)]
        while len(tour) < n:
            curr = tour[-1]
            probs = [(nxt, (pheromones[curr][nxt]**alpha) * ((1.0 / dist[curr][nxt])**beta)) 
                     for nxt in range(n) if nxt not in tour]
            
            tot = sum(p for _, p in probs)
            r = random.uniform(0, tot)
            for nxt, p in probs:
                r -= p
                if r <= 0:
                    tour.append(nxt)
                    break
        
        # Calculate tour length (returning to origin)
        tour_len = sum(dist[tour[i]][tour[i-1]] for i in range(n))
        all_tours.append((tour, tour_len))
        
        if tour_len < best_len:
            best_len, best_tour = tour_len, tour
            
    # 4. Update Pheromones: Based on evaporation and solution quality[cite: 3]
    for i in range(n):
        for j in range(n):
            pheromones[i][j] *= (1 - rho) 
            
    for tour, tour_len in all_tours:
        for i in range(n):
            pheromones[tour[i]][tour[i-1]] += 1.0 / tour_len
            pheromones[tour[i-1]][tour[i]] += 1.0 / tour_len 

# 6. Output the Best Solution: Track and output best solution[cite: 3]
print(f"Best tour sequence: {best_tour}")
print(f"Shortest route length: {best_len:.4f}")
