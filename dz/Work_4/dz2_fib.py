def fib(n: int) -> None:
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print("Числа Фибоначчи:")
for f in range(20):
    print(fib(f+1), end = ' ')