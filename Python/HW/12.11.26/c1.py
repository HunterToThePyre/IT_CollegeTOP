# задания 1
list1 = input("Введите строку: ")

x1 = "ПАЛИНДРОМ"
x2 = "палиндром"
x3 = "67676767"

cle_list1 = ""

for z in list1:
    if z in x1:
        index = x1.index(z)
        cle_list1 += x2[index]
    elif z in x2 or z in x3:
        cle_list1 += z

rev_list1 = cle_list1[::-1]

if cle_list1 != "" and cle_list1 == rev_list1:
    print("Строка является палиндромом.")
else:
    print("Строка не является ПАЛИНДРОМОМ.")
