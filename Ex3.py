# Write a function SumDigits(n) that displays the sum of digits of “n”. Hint: SumDigits(234) will be 2+3+4=9 

def sumDigits(n):
    sum = 0
    while n != 0:
        rem = n%10
        sum += rem
        n = n//10
    print(sum)

sumDigits(234)