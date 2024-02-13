import numpy as np

x, y = np.array([]), np.array([])
N = int(input('Please input a positive integer: '))
k = int(input('Please input a positive integer: '))
for i in range(N):
    x = np.append(x, int(input(f'Please input x{i}: ')))
    y = np.append(y, int(input(f'Please input y{i}: ')))
X = int(input('Please input X: '))
if k <= N:
    distances = np.array([])
    for n in x:
        distances = np.append(distances, np.linalg.norm(X - n))
    neighbors = sorted(zip(x, y, distances), key=lambda x: x[2])[:k]
    output = np.mean([y[1] for y in neighbors])
    print(output)
else:
    print('Error: k is larger than N')