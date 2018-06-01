import time

# calculate the number of ways of integer n can be write the sum of 1,3,4
def sum_part_dp(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2

    first = 1
    second = 1
    third = 1
    fourth = 2

    # repeat n-3 times
    for _ in range(n-3):
        answer = first + second + fourth
        first = second
        second = third
        third = fourth
        fourth = answer

    return fourth

n = 40
t1 = time.time()
s = sum_part_dp(n)
t2 = time.time()
print('面额:%s,方法数:%s,耗时：%s'%(n, s, t2-t1))