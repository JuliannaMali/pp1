import stack
number = int(input("Natural number: "))
while number>=0:
    x = number%2
    stack.push(x)
    number = int(number/2)
    if number == 0:
        break
list1=[]
while stack.empty() == False:
    list1.append(stack.pop())
list2=[]
for x in list1:
    list2.append(str(x))
y=''.join(list2)
print(f'Binary number: {y}')