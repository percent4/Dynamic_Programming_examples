import numpy as np

# A Dynamic Programming solution for subset sum problem
# Returns true if there is a subset of set with sum equal to given sum

def isSubsetSum(st, n, sm):
    # The value of subset[i, j] will be
    # true if there is a subset of
    # set[0..j-1] with sum equal to i
    subset = np.array([[True] * (sm + 1)] * (n + 1))

    # If sum is 0, then answer is true
    for i in range(0, n + 1):
        subset[i, 0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sm + 1):
        subset[0, i] = False

    # Fill the subset table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if j < st[i-1]:
                subset[i, j] = subset[i-1, j]
            if j >= st[i-1]:
                subset[i, j] = subset[i-1, j] or subset[i-1, j-st[i-1]]

    # print the True-False table
    '''
    for i in range(0, n + 1):
        for j in range(0, sm + 1):
            print(subset[i][j], end="  ")
        print(" ")
    '''

    if subset[n, sm]:
        print("Found a subset with given sum")
        sol = []
        # using backtracing to find the solution
        i = n
        while i >= 0:
            if subset[i, sm] and not subset[i-1, sm]:
                sol.append(st[i-1])
                sm -= st[i-1]
            if sm == 0:
                break
            i -= 1
        print('The solution is %s.'%sol)
    else:
        print("No subset with given sum")

    return subset[n, sm]


# Driver program to test above function
st = [2, 3, 7, 9, 4]
n = len(st)
sm = 19
isSubsetSum(st, n, sm)