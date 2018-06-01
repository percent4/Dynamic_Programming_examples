import numpy as np

def solvepuzzle(n, k):
    numdrops = np.array([[0]*(k+1)]*(n+1))

    for i in range(k+1):
        numdrops[1, i] = i

    for i in range(2, n+1):
        for j in range(1, k+1):
            minimum = float('inf')

            for x in range(1, j+1):
                minimum = min(minimum, (1+max(numdrops[i, j-x], numdrops[i-1, x-1])))

            numdrops[i, j] = minimum

    print(numdrops)
    return numdrops[n, k]

t = solvepuzzle(4, 20)
print(t)

