# --- Fibonacci Recursive Method ---
def fibonacci_recursive(last_element: int):                   # "last_element" - До какого числа[индекса] строим Фибоначчи.
    if last_element < 2:                                      # Если last_element == 0 или last_element == 1, то ---
        return last_element                                   # --- верни 0 или верни 1 (базовые случаи)
    else:                                                     # Пока "last_element" > 2, то
        # Вызываем функцию дважды:
        # — один раз для предыдущего индекса (last_element - 1),
        # — второй раз для позапрошлого индекса (last_element - 2)
        # Складываем эти два значения.
        return fibonacci_recursive(last_element-1) + fibonacci_recursive(last_element-2)

print(fibonacci_recursive(40))





