# Example - 1
def counter(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for num in counter(0, 10):
    print(num)

# Example - 2
def filter_by_length(items: list, min_length: int):
    for item in items:
        if len(item) > min_length:
            yield item

temp = ["apple", "banana", "cat", "dog", "elephant"]

for element in filter_by_length(temp, min_length=4):
    print(element)

# Example - 3
def extract_names(users: list):
    for user_dict in users:
        yield user_dict.get('name')

users_data = [
    {'id': 1, 'name': 'Alice', 'role': 'admin'},
    {'id': 2, 'name': 'Bob', 'role': 'user'},
    {'id': 3, 'name': 'Charlie', 'role': 'guest'}
]

for name in extract_names(users_data):
    print(name)


