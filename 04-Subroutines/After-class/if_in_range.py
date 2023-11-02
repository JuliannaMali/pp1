def if_in_range(x, y, z):
    if x in range(y, z):
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(if_in_range(7, 3, 15))
    print(if_in_range(7,3,4))
    