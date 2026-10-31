import random

# 1. Define Problem & 2. Initialize Parameters[cite: 4]
fit = lambda x: x**2
n, pa, iters = 15, 0.25, 100

# 3. Initialize Population[cite: 4]
nests = [random.uniform(-10, 10) for _ in range(n)]

# 7. Iterate[cite: 4]
for _ in range(iters):
    # 5. Generate New Solutions via Lévy flights[cite: 4]
    for i in range(n):
        step = random.gauss(0, 1) / (abs(random.gauss(0, 1)) ** 1.5)
        new_nest = nests[i] + 0.1 * step
        
        # 4. Evaluate Fitness[cite: 4]
        if fit(new_nest) < fit(nests[i]): 
            nests[i] = new_nest
        
    # 6. Abandon Worst Nests[cite: 4]
    nests.sort(key=fit)
    for i in range(int((1 - pa) * n), n):
        nests[i] = random.uniform(-10, 10)

# 8. Output Best Solution[cite: 4]
best = min(nests, key=fit)
print(f"Best solution: {best:.4f}\nMinimum: {fit(best):.4f}")
