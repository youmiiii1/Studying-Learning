def quick_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:                                       # Базовый случай: список из 0 или 1 элемента уже отсортирован
        return lst
    pivot = lst[0]                                          # Переменная (pivot), указатель / метка на нулевой объект списка
    left = [x for x in lst[1:] if x < pivot]                # Переменная (left), помещаем сюда всё что меньше чем объект в (pivot)
    right = [x for x in lst[1:] if x >= pivot]              # Переменная (right), помещаем сюда всё что больше чем объект в (pivot)
    return quick_sort(left) + [pivot] + quick_sort(right)   # Рекурсивно собираем список в отсортированный

temp = [-1,10,5,-10,25,15,11]
print(quick_sort(temp))