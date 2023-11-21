arr= [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

beginner = 1

for i in arr:
    for j in i:
        if i.index(j) == 0:
            i[0] = beginner
            beginner +=1
        else:
            x = i.index(j)
            i[x] = i[0]*(x+1)

print(arr)