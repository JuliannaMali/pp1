def f(x,y):
    ok = []    
    for i in range(x, y+1):
        if i%2 == 0 and i%3 == 0 and i%4 != 0:
            ok.append(i)
    return sum(ok)

if __name__ == '__main__':
    print(f(1, 20))
    print(f(10, 30))