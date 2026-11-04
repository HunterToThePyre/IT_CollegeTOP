
# 1 Задания
a = int(input("Введите первое число: "))
s = int(input("Введите второе число: "))
star = min(a, s)
end = max(a, s)
z = 0
z1 = 0
x = 0
x1 = 0
c = 0
c1 = 0
for d in range(star, end + 1):
  if d % 2 == 0:
    z += d
    z1 += 1
  else:
    x += d
    x1 += 1

  if d % 9 == 0:
    c += d
    c1 += 1

if z1 > 0:
    z3 = z / z1
else:
    z3 = 0
    
if x1 > 0:
    x3 = x / x1
else:
    x3 = 0
    
if c1 > 0:
    c3 = c / c1
else:
    c3 = 0

print("Четные числа:",z,"среднее:",z3)
print("Нечетные числа:",x,"среднее:",x3)
print("Кратно 9:",c,"среднее:",c3)

# 2 Задания
x1 = int(input("Введите длину: "))
x2 = input("Введите букву: ")

for x in range(x1):
    print(x2)

# 3 Задания
print("Если ввести число <7> то цикл закончится")
while True:
    x = int(input("Введите число: "))
    
    if x == 7:
        print("Good bye!")
        break
    elif x > 0:
        print("Number is positive")
    elif x < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

# 4 Задания
z = 0
x1 = 0
x2 = 0
is_x = True
print("Если ввести число <7> то цикл закончится")
while True:
  x = int(input("Введите число: "))
  
  if x == 7:
    print("Good bye!")
    break
  z += x
  if is_x:
    x1 = x
    x2 = x
    is_x = False
  else:
    if x > x1:
      x1 = x
    if x < x2:
      x2 = x

print("Сумма: ",z)
print("Максимум: ",x1)
print("Минимум: ",x2)
