import csv

itog = 0
print("Нужно купить:")
file = open("11.3.csv", "r", encoding="utf-8")
reader = csv.reader(file)
next(reader)

for i in reader:
    name = i[0]
    quantity = int(i[1])
    price = int(i[2])

    print(name, "-", quantity, "шт. за", price, "руб.")
    itog = itog + (quantity * price)

file.close()
print("Итоговая сумма:", itog, "руб.")
