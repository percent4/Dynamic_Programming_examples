# using Dynamic Programming to solve edit distance problem
# str1, str2 are two strings
# m,n are length of each string
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # using DP in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # isnert all characters of second string, thus the
            # min opration is j
            if i == 0:
                dp[i][j] = j

            # If second string is empty, only option is to
            # remove all characters of second string, thus the
            # min opration is i
            elif j == 0:
                dp[i][j] = i

            # If last characters are same, ignore last character
            # and recursive for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum of inserting, removing, replacing
            else:
                dp[i][j] = 1 + min(dp[i][j-1],  # Insert
                                   dp[i-1][j],  # Remove
                                   dp[i-1][j-1])  # Replace

    return dp[m][n]


# Driver program
str1 = "sunday"
str2 = "saturday"

str1 = 'cat'
str2 = 'cut'

print(editDistDP(str1, str2, len(str1), len(str2)))
