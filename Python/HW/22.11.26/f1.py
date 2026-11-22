#Задания 1
def x(xx):
    min_x1 = min(xx)
    min_x2 = xx.index(min_x1)
    return min_x2
list1 = [10, 15, 5, 20]
print(x(list1))

#Задания 2
zz1 = []
zz2 = []
def z(z1):
    f = z1.split()
    for z2 in f:
        zz1.append(int(z2))
    zz1.sort()
    for z3 in zz1:
        zz2.append(str(z3))
    return " ".join(zz2)
print(z("10 15 5 20"))
