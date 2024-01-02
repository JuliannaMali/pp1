def f(d):
    parking = []

    for cars in d:
        for car in cars:
            if car != "in" and car != "out":
                if car in parking:
                    parking.remove(car)
                else:
                    parking.append(car)
                    
    parking.sort()
    return parking
    
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))

cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))
