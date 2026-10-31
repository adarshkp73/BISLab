import random

# 1. Define Problem & 2. Initialize Parameters[cite: 5]
fit = lambda x: x**2
n_wolves, iters = 10, 50

# 3. Initialize Population[cite: 5]
wolves = [random.uniform(-10, 10) for _ in range(n_wolves)]

# 6. Iterate[cite: 5]
for t in range(iters):
    # 4. Evaluate Fitness and identify alpha, beta, delta wolves[cite: 5]
    wolves.sort(key=fit)
    alpha, beta, delta = wolves[0], wolves[1], wolves[2]
    
    a = 2 - t * (2 / iters)  # Decreases linearly from 2 to 0
    
    # 5. Update Positions based on alpha, beta, and delta[cite: 5]
    for i in range(n_wolves):
        X_new = 0
        for leader in (alpha, beta, delta):
            A = 2 * a * random.random() - a
            C = 2 * random.random()
            D = abs(C * leader - wolves[i])
            X_new += leader - A * D
            
        wolves[i] = X_new / 3

# 7. Output the Best Solution[cite: 5]
print(f"Best solution: {wolves[0]:.4f}\nMinimum: {fit(wolves[0]):.4f}")
