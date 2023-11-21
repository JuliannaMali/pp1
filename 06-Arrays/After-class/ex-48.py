def create_2d_arr(x,y):
    arr = [[0 for j in range(0,y)] for i in range(0, x)]
    return arr

print(create_2d_arr(3,5))