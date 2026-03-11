# Write a function squaredSum that returns the sum of the squares of an array/list of 
# integers such that squaredSum([2,3,4]) gives 29. Write your solution in pure Python 
# to show the logic in your solution, do not use any library functions.  

def squaredSum(nums):
    sum = 0
    for num in nums:
        sum += num*num
    return sum

print(squaredSum([2,3,4]))
