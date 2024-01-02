def f(n):
    n = list(str(n))
    list1 = []
    for i in n:
        if int(i)%2!=0:
            list1.append(int(i))
    if len(list1)==0:
        return -1
    else:
      return max(list1)-min(list1)
    
print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))