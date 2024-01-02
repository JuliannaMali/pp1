def f(arr2D):
    sumy = []
    for i in range(0, len(arr2D[0])):
        suma = 0
        for j in range(0, len(arr2D)):
            suma += arr2D[j][i]
        sumy.append(suma)
    for i in sumy:
        if sumy.count(i) > 1:
            return True
    return False

print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]]))
print(f([[3,4],[5,1],[4,7]]))
print(f([[3,4],[5,9],[4,7]]))
