def is_even_number(value):

    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError("Input must be a non-boolean integer")

    return value % 2 == 0