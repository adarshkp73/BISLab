import random

# 1. Define the Problem: Create a mathematical function to optimize[cite: 2]
def fitness(x):
    return x**2  # Finding the minimum of x^2

# 2. Initialize Parameters: Set number of particles, inertia, cognitive and social coefficients[cite: 2]
NUM_PARTICLES, W, C1, C2, ITERATIONS = 20, 0.5, 1.5, 1.5, 50

# 3. Initialize Particles: Generate random positions and velocities[cite: 2]
particles = [{"pos": random.uniform(-10, 10), "vel": random.uniform(-1, 1), 
              "pbest": None, "pbest_val": float('inf')} for _ in range(NUM_PARTICLES)]
gbest, gbest_val = None, float('inf')

# 6. Iterate: Repeat evaluation, updating, and position adjustment[cite: 2]
for _ in range(ITERATIONS):
    for p in particles:
        # 4. Evaluate Fitness[cite: 2]
        val = fitness(p["pos"])
        
        if val < p["pbest_val"]:
            p["pbest_val"], p["pbest"] = val, p["pos"]
        if val < gbest_val:
            gbest_val, gbest = val, p["pos"]
            
    # 5. Update Velocities and Positions based on own best and global best[cite: 2]
    for p in particles:
        r1, r2 = random.random(), random.random()
        p["vel"] = (W * p["vel"] + 
                    C1 * r1 * (p["pbest"] - p["pos"]) + 
                    C2 * r2 * (gbest - p["pos"]))
        p["pos"] += p["vel"]

# 7. Output the Best Solution: Track and output the best solution found[cite: 2]
print(f"Best solution found: x = {gbest:.4f}")
print(f"Minimum value: {gbest_val:.4f}")
