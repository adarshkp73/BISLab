import math, random

# 1. Define Problem & 2. Initialize Parameters[cite: 3]
cities = [(0, 0), (2, 8), (5, 2), (8, 6), (9, 1)]
n = len(cities)
D = [[math.dist(i, j) for j in cities] for i in cities]
P = [[1.0] * n for _ in range(n)]
best_t, best_l = None, float('inf')

# 5. Iterate[cite: 3]
for _ in range(50):
    tours = []
    # 3. Construct Solutions[cite: 3]
    for _ in range(10):
        t = [random.randint(0, n - 1)]
        while len(t) < n:
            opts = [i for i in range(n) if i not in t]
            w = [P[t[-1]][nxt] * (1.0 / D[t[-1]][nxt])**2 for nxt in opts]
            t.append(random.choices(opts, weights=w)[0])
        
        l = sum(D[t[i]][t[i-1]] for i in range(n))
        tours.append((t, l))
        if l < best_l: best_l, best_t = l, t
            
    # 4. Update Pheromones[cite: 3]
    P = [[P[i][j] * 0.5 for j in range(n)] for i in range(n)] 
    for t, l in tours:
        for i in range(n):
            P[t[i]][t[i-1]] += 1.0 / l
            P[t[i-1]][t[i]] += 1.0 / l

# 6. Output Best Solution[cite: 3]
print(f"Best tour: {best_t}\nLength: {best_l:.4f}")
