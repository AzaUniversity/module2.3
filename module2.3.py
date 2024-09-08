my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  
count = 0
print('Список', my_list, '\nПоложительные числа из списка')

while count < len(my_list):
    numb = my_list[count]
    count = count + 1
    if numb == 0:
        continue
    elif numb < 0:
        print('Найдено отрицательное число:', numb)
        break
    elif count == len(my_list):
        print(numb)
        print('Список закончился')
    else:
        print(numb)