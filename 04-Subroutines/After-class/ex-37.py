def f(n):
    fib = [0, 1]
    x = 0
    while len(fib) <= n:
        y = fib[x] + fib[x+1]
        fib.append(y)
        x += 1
    return fib[n-1]

if __name__ == '__main__':
    print(f(5))
    print(f(9))