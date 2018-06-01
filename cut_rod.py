import time
# 使用动态规划法(dynamic programming)解决钢条切割问题

# 钢条长度与对应的收益
length = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
profit = (1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 31, 33, 33, 35, 37, 40, 40, 41, 42, 44, 45, 47, 48, 49, 51, 53, 55, 56, 57, 59)

# 递归法(recursive)解决办法
# 运行时间: 指数
# 参数：profit: 收益列表, n: 钢条总长度
# 返回参数: q: 最大收益
def cut_rod(profit, n):

    if n == 0:
        return 0

    q = float('-inf')

    for i in range(1, n+1):
        q = max(q, profit[length.index(i)]+cut_rod(profit, n-i))

    return q

'''
for i in range(1, 31):
    t1 = time.time()
    money = cut_rod(profit, i)
    t2 = time.time()
    print('profit of %d is %d. Cost time is %ss.'%(i, money, t2-t1))
'''

# 动态归纳法，自顶向下的CUT-ROD过程，加入备忘机制
# 运行时间: 多项式
# 参数：profit: 收益列表, n: 钢条总长度
# 返回参数: q: 最大收益
def memoized_cut_rod(profit, n):

    r = [float('-inf') for _ in range(n+1)]
    return memoized_cut_rod_aux(profit, n, r)

# 引入备忘机制的cut_rod()版本
def memoized_cut_rod_aux(profit, n, r):

    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, profit[length.index(i)]+memoized_cut_rod_aux(profit, n-i, r))

    r[n] = q

    return q

'''
for i in range(1, 31):
    t1 = time.time()
    money = memoized_cut_rod(profit, i)
    t2 = time.time()
    print('profit of %d is %d. Cost time is %ss.'%(i, money, t2-t1))
'''

# 动态归纳法，自底向上的CUT-ROD过程，加入备忘机制
# 运行时间: 多项式
# 参数：profit: 收益列表, n: 钢条总长度
# 返回参数: q: 最大收益
def bottom_up_cut_rod(profit, n):

    r = [0]
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, profit[length.index(i)]+r[j-i])
        r.append(q)
    return r[n]

for i in range(1, 31):
    t1 = time.time()
    money = bottom_up_cut_rod(profit, i)
    t2 = time.time()
    print('profit of %d is %d. Cost time is %ss.'%(i, money, t2-t1))