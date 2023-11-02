def f(n):
    prime = []
    if n!= 1:
        x = 1
        while len(prime) < n:
            divider = []
            y = 1
            while y <= x:
                if x%y == 0:
                    divider.append(y)
                y += 1
            if len(divider) == 2:
                prime.append(x)
            x += 1
        return prime[n-1]
    else:
        return 2


if __name__ == '__main__':
    print(f(1))
    print(f(5))
    print(f(11))