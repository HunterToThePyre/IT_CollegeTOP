# Задания 1
try:
    x = int(input("Введи число: "))
    print(x ** 2)
except ValueError:
    print("Не то число")
    
    
# Задания 2
try:
    x1 = int(input("Введи 1 число: "))
    x2 = int(input("Введи 2 число: "))
    z = x1 / x2
    print(z)
except ValueError:
    print("Не то число")
except ZeroDivisionError:
    print("на 0 нельзя")
    
    
# Задания 3
list1 = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
try:
    x1 = input("Введи день: ")
    x2 = int(x1) 
    if not (1 <= x2 <= 7):
        raise IndexError
    print(list1[x2 - 1])
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")