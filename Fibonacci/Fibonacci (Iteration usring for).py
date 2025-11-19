# --- Fibonacci Iterative Method ---
def fibonacci_iterative(last_element: int) -> int:           # "Last_element" - До какого числа[индекса] строим Фибоначчи.
    if last_element <= 1:
        return last_element

    sequence = [0,1]

    for _ in range(2, last_element+1):                        # От 2 до "Last_element"+1.
        sequence.append(sequence[-1] + sequence[-2])          # Добавляем +1 число, которое будет суммой двух последних.
    return sequence[-1]

print(fibonacci_iterative(7))



