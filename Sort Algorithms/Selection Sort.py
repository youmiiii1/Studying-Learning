def selection_sort(lst: list[int]) -> list[int]:
    lst_len = len(lst)                                  # Переменная (lst_len), в ней храним количество объектов из списка.

    for i in range(lst_len):                            # Внешний цикл выполняется столько раз, сколько элементов в списке
        min_idx = i                                     # Переменная (min_idx), в ней храним число (i) на каждой итерации
        for x in range(i+1, lst_len):                   # Здесь (x) индекс текущего элемента, проходим по всем объектам в списке
            if lst[x] < lst[min_idx]:                   # Если объект за текущим индексом (x) МЕНЬШЕ ЧЕМ объект за индексом (min_idx)
                min_idx = x                             # В переменную (min_idx) перезаписываем текущий элемент из переменной (x)

        lst[i], lst[min_idx] = lst[min_idx], lst[i]     # Меняем числа местами
    return lst

temp = [50, 25, 10, 30, 15]
print(selection_sort(temp))