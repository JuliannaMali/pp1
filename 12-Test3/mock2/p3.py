def f(d):
    avg = sum(d.values()) / len(d.values())
    suma = 0

    for value in d.values():
        if value > avg:
            suma += 1    
    return suma


print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))