def f(palindrome):
    x = str(palindrome)
    y = 0
    z = -1
    for y in range(0, int((len(palindrome))/2+1)):
        if x[y] == x[z]:
            y += 1
            z -= 1
            if y == int((len(palindrome))/2):
                return True
        else:
            return False
            break
if __name__ == '__main__':
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))