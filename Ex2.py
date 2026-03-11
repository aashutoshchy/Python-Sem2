# Write a function myPow(x, n) that returns 𝑥𝑛, where and n is a non-negative integer. Do not use the ** operator or the math.pow function - use one while loop.

def myPow(x, n):
    idx = 0
    ans = 1
    while idx < n:
        ans = ans * x
        idx += 1
    return ans


print(myPow(2,3))