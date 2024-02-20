## Список, содержащий рандомные числа
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
## Новый список, содержащий целые части от положительных чисел
newlist = [int(number // 1) for number in numbers if number > 0]
print(newlist)