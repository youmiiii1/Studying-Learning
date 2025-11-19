# Example - 1
import webbrowser

def validate(func):
    def wrapper(url):
        if "." in url:
            func()
        else:
            print("- Wrong link -")
    return wrapper

@validate
def open_url(url):
    webbrowser.open(url)

open_url("https://www.googlecom")

# Example - 2
def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} function called with {','.join(map(str, args))}")
        return func(*args)
    return wrapper

@logger
def say_hello(a,b,c):
    result = a + b + c
    return result
say_hello(1,1,1)

# Example - 3
def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for word in words:
                result = result.replace(word, "*")

            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_sentence(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_sentence("Steve"))

# Example - 4
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Failed: Argument must be of type {type_.__name__}")
                return False

            if len(arg) > max_length:
                print(f"Failed: Argument length must not exceed {max_length}")
                return False

            for symbol in contains:
                if symbol not in arg:
                    print(f"Failed: Argument must contain '{symbol}'")
                    return False

            return func(arg)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))

# Example - 5
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Args in '{func.__name__}' - {args}")
        print(f"Kwargs in '{func.__name__}' - {kwargs}")

        result = func(*args, **kwargs)

        return result
    return wrapper

@decorator
def add_user(name, age, message):
    return f"Name: {name} | Age: {age} | Message: {message}"

print(add_user(name="Varya", age=20, message="I wanna have consultation."))
print("----")
print(add_user("Petro", 55, "I wanna have consultation."))

# Example - 6
def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_n_times(n=3)
def say_hello():
    return print("Hello world!")

@repeat_n_times(2)
def add_numbers(a, b):
    print(a + b)

say_hello()
add_numbers(5,5)