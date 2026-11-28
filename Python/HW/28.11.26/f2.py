"""
# Задания 1
def v():
    print("“ Don't compare yourself with anyone in this world…")
    print("if you do so, you are insulting yourself.”")
    print("                                        Bill Gates")
v()

# Задания 2
def x(x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(x1 + 1, x2):
        if i % 2 == 0:
            print(i, end=", ")
    print()
x(2, 11)

# Задания 3
def z(z1, z2, z3):
    for i1 in range(z1):
        if z3 or i1 == 0 or i1 == z1 - 1:
            print(z2 * z1)
        else:
            print(z2 + " " * (z1 - 2) + z2)
z(4, "*", True)
print()
z(4, "*", False)

# Задания 4
def a(a, aa, aaa, aaaa, aaaaa):
    return min(a, aa, aaa, aaaa, aaaaa)
print(a(19, 6, 7, -67, 52))

# Задания 5
def d(s1, s2):
    if s1 > s2:
        s1, s2 = s2, s1
    d1 = 1
    for i3 in range(s1, s2 + 1):
        d1 = d1 * i3
    return d1
print(d(67, 52))

# Задания 6
def f(f1):
    return len(str(abs(f1)))
print(f(3456))
"""
# Задания 7
def g(g1):
    if g1 < 0:
        return False
    g2 = g1
    g3 = 0
    while g1 > 0:
        g4 = g1 % 10
        g3 = g3 * 10 + g4
        g1 //= 10
    return g2 == g3
print(g(123321))
print(g(421987))
