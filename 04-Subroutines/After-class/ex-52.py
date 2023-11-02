def power(x, n):

    if n==0 or x==1:
        return 1
    if n==1:
        return x
    # n! = n * (n-1)!
    if n > 1:
        return x * x**(n-1)
if __name__ == '__main__':
    print(power(5,3))