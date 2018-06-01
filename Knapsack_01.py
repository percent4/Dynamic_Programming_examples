import numpy as np

W = 22 # weight bound
w = (1, 2, 5, 6, 7, 9) # weight of items
v = (1, 6, 18, 22, 28, 38) # value of items

# dynamic programming for 0-1 Knapsack Problem
# n: number of items
# W: weight bound
# w: weight of item
# v: value of item
# return: dp[0][W]: maximum value of 0-1 Knapsack Problem
def Knapsack_01(n, W, w, v):
    dp = np.array([[0]*(W+1)]*(n+1))

    for i in range(n, -1, -1):
        for j in range(W + 1):
            if i == n:
                dp[i, j] = 0 # initial condition
            else:
                choices = []
                choices.append(dp[i+1, j])
                if j >= w[i]:
                    choices.append(dp[i+1, j-w[i]]+v[i])

                dp[i,j] = max(choices)

    return dp[0][W]

n = len(w)
max_value = Knapsack_01(n, W, w, v)
print(max_value)




