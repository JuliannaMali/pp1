meat = open('MeatAndFish.txt', 'r')
bread = open('GrainsAndBread.txt', 'r')
allproducts = open('allproducts.txt', 'a')

fish = meat.read()
grains = bread.read()

allproducts.write(fish)
allproducts.write("")
allproducts.write(grains)