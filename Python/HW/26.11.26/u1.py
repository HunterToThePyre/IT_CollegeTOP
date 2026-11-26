"""
# Задания 1
x = int(input("Введи x: "))
y = int(input("Введи y: "))
z = 1
for i in range(y):
    z *= x
print(z)

# Задания 2
x1 = 0
for i1 in range(100, 1000):
    z1 = i1 // 100
    z2 = (i1 // 10) % 10
    z3 = i1 % 10
    if z1 == z2 or z1 == z3 or z2 == z3:
        x1 += 1
print("Колво чисел: ", x1)

# Задания 3
x2 = 0
for i2 in range(100, 10000):
    s = str(i2)
    if len(s) == len(set(s)):
        x2 += 1
print("Колво чисел: ", x2)
"""
# Задания 4
x3 = input("Ввод целое число: ")
z3 = ""
for i3 in x3:
    if i3 != "3" and i3 != "6":
        z3 += i3

if z3 == "" or z3 == "-":
    print("Ответ 0")
else:
    print("Ответ ", int(z3))
