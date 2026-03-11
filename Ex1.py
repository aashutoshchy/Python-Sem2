# Write a function fib (n) that prompts the number of terms “n” from the user and displays first “n” terms of Fibonacci sequence iteratively.

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(0, n):
        c = a+b
        print(c)

        a = b
        b = c

n = int(input("Enter any number: "))
fib(n)